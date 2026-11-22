from retrieval.repository import RetrievalRepository
from retrieval.service import RetrievalService
from shared.database_repository import DatabaseRepository
from shared.sentence_transformer_client import SentenceTransformerClient


def provide_retrieval_repository(
    db: DatabaseRepository,
) -> RetrievalRepository:
    return RetrievalRepository(db)


def provide_retrieval_service(
    repository: RetrievalRepository,
    client: SentenceTransformerClient,
) -> RetrievalService:
    return RetrievalService(repository, client)
