from retrieval.repository import RetrievalRepository
from retrieval.retrieval_model import RetrievedChunk
from retrieval.strategies.base import RetrievalStrategy
from shared.sentence_transformer_client import SentenceTransformerClient


class HybridStrategy(RetrievalStrategy):
    RRF_K = 60

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

        semantic_results = self.retrieval_repository.search_similar_chunks(
            query_embedding,
            top_k,
        )

        keyword_results = self.retrieval_repository.search_keyword_chunks(
            query,
            top_k,
        )

        # Calculate RRF scores and deduplicate chunks.
        rrf_scores: dict[int, float] = {}
        chunks_by_id: dict[int, RetrievedChunk] = {}

        for results in (semantic_results, keyword_results):
            for rank, chunk in enumerate(results, start=1):
                chunk_id = chunk.chunk_id

                rrf_scores[chunk_id] = rrf_scores.get(chunk_id, 0.0) + 1.0 / (
                    self.RRF_K + rank
                )

                chunks_by_id[chunk_id] = chunk

        # Sort by combined RRF score.
        ranked_chunks = sorted(
            chunks_by_id.values(),
            key=lambda chunk: rrf_scores[chunk.chunk_id],
            reverse=True,
        )

        return ranked_chunks[:top_k]
