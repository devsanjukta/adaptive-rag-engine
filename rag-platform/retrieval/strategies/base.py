from abc import ABC, abstractmethod

from retrieval.retrieval_model import RetrievedChunk


class RetrievalStrategy(ABC):
    @abstractmethod
    def search(
        self,
        query: str,
        top_k: int,
    ) -> list[RetrievedChunk]:
        raise NotImplementedError
