from retrieval.repository import RetrievalRepository
from retrieval.retrieval_model import RetrievedChunk
from retrieval.strategies.base import RetrievalStrategy
from shared.sentence_transformer_client import SentenceTransformerClient


class SemanticStrategy(RetrievalStrategy):
    def __init__(
        self,
        retrieval_repository: RetrievalRepository,
        sentence_transformer_client: SentenceTransformerClient,
    ):
        self.retrieval_repository = retrieval_repository
        self.sentence_transformer_client = sentence_transformer_client

    def search(
        self,
        query: str,
        top_k: int,
    ) -> list[RetrievedChunk]:

        query_embedding = self.sentence_transformer_client.generate_query_embedding(
            query
        )

        return self.retrieval_repository.search_similar_chunks(
            query_embedding,
            top_k,
        )
