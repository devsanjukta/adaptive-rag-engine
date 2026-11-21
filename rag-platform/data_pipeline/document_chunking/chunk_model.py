from datetime import datetime

from pydantic import BaseModel, Field

from data_pipeline.document_processing.processed_trial_model import ProcessedTrial


class DocumentChunk(BaseModel):
    id: int | None = None
    trial_id: int
    chunk_index: int
    content: str
    section: str
    metadata: dict = Field(default_factory=dict)
    created_at: datetime | None = None


class ProcessedTrialRecord(ProcessedTrial):
    id: int
