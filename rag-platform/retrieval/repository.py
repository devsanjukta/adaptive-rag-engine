from sqlalchemy import text

from retrieval.retrieval_model import RetrievedChunk
from shared.database_repository import DatabaseRepository


class RetrievalRepository:
    def __init__(self, database_repository: DatabaseRepository):
        self.database_repository = database_repository

    def search_similar_chunks(
        self,
        query_embedding: list[float],
        top_k: int = 5,
    ) -> list[RetrievedChunk]:

        query = """
            SELECT
                dc.id AS chunk_id,
                dc.trial_id,
                dc.chunk_index,
                dc.content,
                dc.section,
                dc.metadata,
                pct.nct_id,
                1 - (de.embedding <=> CAST(:query_embedding AS vector))
                    AS similarity_score
            FROM document_embeddings de
            JOIN document_chunks dc ON dc.id = de.chunk_id
            JOIN processed_clinical_trials pct ON pct.id = dc.trial_id
            ORDER BY de.embedding <=> CAST(:query_embedding AS vector)
            LIMIT :top_k
        """

        params = {
            "query_embedding": str(query_embedding),
            "top_k": top_k,
        }

        return self.database_repository.fetch_all(query, RetrievedChunk, params)
