import requests

from reranker.dataset_utils import DatasetUtils
from reranker.models import (
    REVIEW_DECISIONS,
    AIReviewAssessment,
    AIReviewResult,
    RerankerDatasetRecord,
)
from shared.config import Settings


class AILabelReviewer:
    def __init__(
        self,
        settings: Settings,
    ):
        self.records: list[RerankerDatasetRecord] = []
        self.model_name = settings.OLLAMA_MODEL_NAME
        self.ollama_url = settings.OLLAMA_URL

        self.system_instruction = self._get_system_instruction()

    def _load_dataset(self) -> None:
        try:
            self.records = DatasetUtils.fetch_reranker_records(self.dataset_path)
        except Exception as ex:
            print(f"Error loading dataset: {ex!s}")
            raise

    def _get_system_instruction(self):
        return """You are an AI assistant reviewing labels in a clinical trial search dataset.
                OBJECTIVE:
                Determine whether an existing relevance label is correct.

                LABEL MEANING:
                - 1 = Relevant to the user's query.
                - 0 = Not relevant to the user's query.

                REVIEW PROCESS:

                Step 1: Understand the user query.

                Step 2: Understand the clinical trial:
                - What disease does it study?
                - What treatment or research is being investigated?
                - Is the requested treatment a main part of the study or only mentioned as background or previous treatment?

                Step 3: Determine actual relevance WITHOUT considering the existing label.

                Choose one:
                - Relevant
                - Not relevant
                - Uncertain

                Step 4: Compare actual relevance with the existing label.

                Decision rules:
                - Relevant + label 1 = correct
                - Not relevant + label 0 = correct
                - Relevant + label 0 = suspicious
                - Not relevant + label 1 = suspicious
                - Uncertain relevance = uncertain

                IMPORTANT:
                - Judge the entire query against the entire trial.
                - Do not assume radiation is being studied just because it is mentioned.
                - Do not invent trial details.
                - Do not modify the existing label.
                - Make the final decision consistent with your explanation.

                OUTPUT FORMAT:
                Return ONLY a valid JSON object with these fields:
                {
                    "review_decision": "correct",
                    "explanation": "Brief explanation of the decision."
                }
                
                Rules:
                - review_decision must be exactly one of:
                    correct, suspicious, uncertain.
                - explanation must briefly explain the decision.
                - Do not include markdown or code fences.
                - Do not include any text outside the JSON object.
                - Ensure the decision is consistent with your relevance assessment and existing label.
                """

    def _build_prompt(self, record: RerankerDatasetRecord) -> str:
        return f"""
                    Review this clinical trial using the instructions provided.

                    User query:
                    {record.query}

                    Clinical trial document:
                    {record.document}

                    Trial ID:
                    {record.nct_id}

                    Existing label:
                    {record.label}

                      Follow the required review process and return the result in the required JSON format.
                """

    def _call_ollama(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "system",
                    "content": self.system_instruction,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "stream": False,
            "keep_alive": "10m",
            "options": {
                "temperature": 0,
            },
        }

        response = requests.post(
            self.ollama_url,
            json=payload,
            timeout=300,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]

    def _review_records(self) -> list[AIReviewResult]:
        records_requiring_review = []

        for index, record in enumerate(self.records):
            prompt = self._build_prompt(record)
            response = self._call_ollama(prompt)

            assessment = AIReviewAssessment.model_validate_json(response)
            review_decision = assessment.review_decision
            explanation = assessment.explanation

            if review_decision in REVIEW_DECISIONS:
                records_requiring_review.append(
                    AIReviewResult(
                        nct_id=record.nct_id,
                        query=record.query,
                        document=record.document,
                        original_label=record.label,
                        review_decision=review_decision,
                        explanation=explanation,
                    )
                )

        return records_requiring_review

    def run(self):
        self._load_dataset()
        self._review_records()
