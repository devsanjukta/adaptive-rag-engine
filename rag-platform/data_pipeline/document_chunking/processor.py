import tiktoken

from data_pipeline.document_chunking.chunk_model import (
    DocumentChunk,
    ProcessedTrialRecord,
)
from data_pipeline.document_processing.processed_trial_model import ProcessedTrial


class DocumentChunkingProcessor:
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    def __init__(self) -> None:
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def process_all(
        self,
        trials: list[ProcessedTrialRecord],
    ) -> list[list[DocumentChunk]]:
        return [self.process(trial, trial.id) for trial in trials]

    def process(self, trial: ProcessedTrial, trial_id: int) -> list[DocumentChunk]:
        chunks = []
        chunk_index = 0

        for section, value in trial.model_dump(exclude={"nct_id"}, mode="json").items():
            text = self._to_text(value)

            if not text:
                continue

            section_chunks = self._split_text(text)

            for content in section_chunks:
                chunks.append(
                    DocumentChunk(
                        trial_id=trial_id,
                        chunk_index=chunk_index,
                        content=content,
                        section=section,
                    )
                )
                chunk_index += 1

        return chunks

    def _to_text(self, value: object) -> str:
        if value is None:
            return ""

        if isinstance(value, (dict, list)):
            if isinstance(value, dict):
                parts = [f"{key}: {self._to_text(item)}" for key, item in value.items()]
                return "\n".join(parts)

            return "\n".join(self._to_text(item) for item in value)

        return str(value).strip()

    def _split_text(self, text: str) -> list[str]:
        tokens = self.tokenizer.encode(text)

        if not tokens:
            return []

        chunks = []
        start = 0
        step = self.CHUNK_SIZE - self.CHUNK_OVERLAP

        while start < len(tokens):
            end = start + self.CHUNK_SIZE
            chunk_tokens = tokens[start:end]

            chunks.append(self.tokenizer.decode(chunk_tokens))

            start += step

        return chunks
