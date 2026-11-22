import logging

from data_pipeline.embedding_generation.embedding_model import (
    DocumentEmbedding,
)
from data_pipeline.embedding_generation.repository import EmbeddingRepository
from shared.sentence_transformer_client import SentenceTransformerClient
from shared.utils import Utils

logger = logging.getLogger(__name__)


class EmbeddingService:
    def __init__(
        self,
        repository: EmbeddingRepository,
        transformer_client: SentenceTransformerClient,
    ) -> None:
        self.repository = repository
        self.transformer_client = transformer_client

    def generate_embeddings(self) -> int:
        try:
            chunks = self.repository.get_all_chunks()

            if not chunks:
                logger.info("No document chunks found for embedding generation")
                return 0

            inputs = [
                Utils.create_embedding_input(chunk.id, chunk.content)
                for chunk in chunks
            ]

            outputs = self.transformer_client.generate_embeddings(inputs)

            embeddings = [
                DocumentEmbedding(
                    chunk_id=output.chunk_id,
                    embedding=output.embedding,
                    model=self.transformer_client.MODEL_NAME,
                )
                for output in outputs
            ]

            if not self.repository.save_all(embeddings):
                return 0

            return len(embeddings)

        except Exception:
            logger.exception("Failed to generate document embeddings")
            return 0
