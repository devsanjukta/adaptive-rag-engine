from collections import defaultdict

from reranker.reranker import Reranker
from retrieval.query_classifier import QueryClassifier
from retrieval.query_type import QueryType
from retrieval.retrieval_model import RetrievedTrial, SearchRequest
from retrieval.strategies.base import RetrievalStrategy


class RetrievalService:
    def __init__(
        self,
        query_classifier: QueryClassifier,
        strategies: dict[QueryType, RetrievalStrategy],
        reranker: Reranker,
    ):
        self.query_classifier = query_classifier
        self.strategies = strategies
        self.reranker = reranker

    def search(self, request: SearchRequest) -> list[RetrievedTrial]:

        # 1. Classify query
        query_type = self.query_classifier.classify(request.query)

        # 2. Select retrieval strategy
        strategy = self.strategies[query_type]

        # 3. Retrieve chunks
        chunks = strategy.search(
            request.query,
            request.top_k,
        )

        # 4. Rerank chunks
        ranked_chunks = self.reranker.rerank(
            request.query,
            chunks,
        )

        # 5. Group chunks by trial
        grouped_trials = defaultdict(list)

        for chunk in ranked_chunks:
            grouped_trials[chunk.nct_id].append(chunk)

        return [
            RetrievedTrial(nct_id=nct_id, chunks=trial_chunks)
            for nct_id, trial_chunks in grouped_trials.items()
        ]
