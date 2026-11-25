from collections import defaultdict

from reranker.reranker import Reranker
from retrieval.repository import RetrievalRepository
from retrieval.retrieval_model import RetrievedChunk, RetrievedTrial, SearchRequest
from shared.sentence_transformer_client import SentenceTransformerClient


class RetrievalService:
    def __init__(
        self,
        retrieval_repository: RetrievalRepository,
        sentence_transformer_client: SentenceTransformerClient,
    ):
        self.retrieval_repository = retrieval_repository
        self.sentence_transformer_client = sentence_transformer_client
        self.reranker = Reranker()

    def search(self, request: SearchRequest) -> list[RetrievedChunk]:
        query_embedding = self.sentence_transformer_client.generate_query_embedding(
            request.query
        )
        chunks = self.retrieval_repository.search_similar_chunks(
            query_embedding,
            request.top_k,
        )

        ranked_chunks = self.reranker.rerank(request.query, chunks)

        grouped_trials = defaultdict(list)
        for chunk in ranked_chunks:
            grouped_trials[chunk.nct_id].append(chunk)

        results = [
            RetrievedTrial(nct_id=nct_id, chunks=chunks)
            for nct_id, chunks in grouped_trials.items()
        ]

        print("after rank and grouping")
        print(results)
        return results
