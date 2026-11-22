from functools import lru_cache

from data_pipeline.embedding_generation.repository import EmbeddingRepository
from data_pipeline.embedding_generation.service import EmbeddingService
from shared.database_repository import DatabaseRepository
from shared.sentence_transformer_client import SentenceTransformerClient


@lru_cache
def provide_sentence_transformer_client() -> SentenceTransformerClient:
    return SentenceTransformerClient()


def provide_embedding_repository(
    db: DatabaseRepository,
) -> EmbeddingRepository:
    return EmbeddingRepository(db)


def provide_embedding_service(
    repository: DatabaseRepository, client: SentenceTransformerClient
) -> EmbeddingService:
    return EmbeddingService(repository, client)
