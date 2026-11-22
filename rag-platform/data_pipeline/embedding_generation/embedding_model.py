from datetime import datetime

from pydantic import BaseModel


class EmbeddingInput(BaseModel):
    chunk_id: int
    content: str


class EmbeddingOutput(BaseModel):
    chunk_id: int
    embedding: list[float]


class DocumentEmbedding(BaseModel):
    id: int | None = None
    chunk_id: int
    embedding: list[float]
    model: str
    created_at: datetime | None = None
