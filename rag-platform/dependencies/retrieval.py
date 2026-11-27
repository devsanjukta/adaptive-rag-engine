from reranker.reranker import Reranker
from retrieval.query_classifier import QueryClassifier
from retrieval.query_type import QueryType
from retrieval.repository import RetrievalRepository
from retrieval.service import RetrievalService
from retrieval.strategies.hybrid import HybridStrategy
from retrieval.strategies.keyword import KeywordStrategy
from retrieval.strategies.semantic import SemanticStrategy
from shared.database_repository import DatabaseRepository
from shared.ollama_client import OllamaClient
from shared.sentence_transformer_client import SentenceTransformerClient


def provide_reranker() -> Reranker:
    return Reranker()


def provide_retrieval_repository(
    db: DatabaseRepository,
) -> RetrievalRepository:
    return RetrievalRepository(db)


def provide_query_classifier(
    ollama_client: OllamaClient,
) -> QueryClassifier:
    return QueryClassifier(ollama_client)


def provide_retrieval_service(
    repository: RetrievalRepository,
    client: SentenceTransformerClient,
    query_classifier: QueryClassifier,
) -> RetrievalService:
    semantic_strategy = SemanticStrategy(
        repository,
        client,
    )

    keyword_strategy = KeywordStrategy(
        repository,
    )

    hybrid_strategy = HybridStrategy(
        repository,
        client,
    )

    strategies = {
        QueryType.SEMANTIC: semantic_strategy,
        QueryType.KEYWORD: keyword_strategy,
        QueryType.HYBRID: hybrid_strategy,
    }

    return RetrievalService(
        query_classifier=query_classifier,
        strategies=strategies,
    )
