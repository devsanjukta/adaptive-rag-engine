from sentence_transformers import CrossEncoder

from reranker.models import RerankedChunk
from retrieval.retrieval_model import RetrievedChunk
from shared.config import RERANKING_TRAINED_MODEL_PATH


class Reranker:
    model_path = RERANKING_TRAINED_MODEL_PATH

    def __init__(self):
        self.model = CrossEncoder(str(self.model_path))

    def rerank(
        self, query: str, documents: list[RetrievedChunk]
    ) -> list[RerankedChunk]:
        if not documents:
            return []

        pairs = [(query, document.content) for document in documents]

        scores = self.model.predict(pairs)

        reranked_documents = [
            RerankedChunk(
                **document.model_dump(),
                reranking_score=float(score),
            )
            for document, score in zip(documents, scores)
        ]

        reranked_documents.sort(
            key=lambda item: item.reranking_score,
            reverse=True,
        )

        return reranked_documents
