import logging

from data_pipeline.document_chunking.chunk_model import DocumentChunk
from data_pipeline.embedding_generation.embedding_model import DocumentEmbedding
from shared.database_repository import DatabaseRepository

logger = logging.getLogger(__name__)


class EmbeddingRepository:
    def __init__(self, db: DatabaseRepository) -> None:
        self.db = db

    def get_all_chunks(self) -> list[DocumentChunk]:
        query = """
            SELECT *
            FROM document_chunks
            ORDER BY id
        """

        return self.db.fetch_all(query, DocumentChunk)

    def save_all(self, embeddings: list[DocumentEmbedding]) -> bool:
        try:
            self.db.execute("DELETE FROM document_embeddings")

            if not embeddings:
                return True

            query = """
                INSERT INTO document_embeddings (
                    chunk_id,
                    embedding,
                    model
                )
                VALUES (
                    :chunk_id,
                    CAST(:embedding AS VECTOR),
                    :model
                )
            """

            params = [
                {
                    "chunk_id": embedding.chunk_id,
                    "embedding": str(embedding.embedding),
                    "model": embedding.model,
                }
                for embedding in embeddings
            ]

            self.db.execute_many(query, params)

            return True

        except Exception:
            logger.exception("Failed to save document embeddings")
            return False
