from retrieval.repository import RetrievalRepository
from retrieval.retrieval_model import RetrievedChunk
from retrieval.strategies.base import RetrievalStrategy


class KeywordStrategy(RetrievalStrategy):
    def __init__(
        self,
        retrieval_repository: RetrievalRepository,
    ):
        self.retrieval_repository = retrieval_repository

    def search(
        self,
        query: str,
        top_k: int,
    ) -> list[RetrievedChunk]:

        return self.retrieval_repository.search_keyword_chunks(
            query,
            top_k,
        )
