from typing import Literal

from pydantic import BaseModel, Field

from retrieval.retrieval_model import RetrievedChunk


class RerankedChunk(RetrievedChunk):
    reranking_score: float


class RerankerDatasetRecord(BaseModel):
    row_number: int
    query: str
    document: str
    label: int
    nct_id: str
    negative_type: str | None = None


class RecordValidationResult(BaseModel):
    row_number: int

    missing_fields_errors: list[str] = Field(default_factory=list)
    negative_type_errors: list[str] = Field(default_factory=list)
    label_errors: list[str] = Field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return not (
            self.missing_fields_errors or self.negative_type_errors or self.label_errors
        )


class DatasetValidationResult(BaseModel):
    total_records: int
    valid_records: int
    invalid_records: int
    record_results: list[RecordValidationResult]


ReviewDecision = Literal["suspicious", "uncertain"]

REVIEW_DECISIONS = {"suspicious", "uncertain"}


class AIReviewResult(BaseModel):
    nct_id: str
    query: str
    document: str
    original_label: int
    review_decision: ReviewDecision
    explanation: str


class AIReviewAssessment(BaseModel):
    review_decision: Literal["correct", "suspicious", "uncertain"]
    explanation: str
