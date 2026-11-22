from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int = Field(default=5, gt=0)


class RetrievedChunk(BaseModel):
    chunk_id: int
    trial_id: int
    nct_id: str
    chunk_index: int
    content: str
    section: str
    metadata: dict
    similarity_score: float
