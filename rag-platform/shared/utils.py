from data_pipeline.embedding_generation.embedding_model import EmbeddingInput


class Utils:
    @staticmethod
    def create_embedding_input(
        chunk_id: int,
        content: str,
    ) -> EmbeddingInput:
        return EmbeddingInput(
            chunk_id=chunk_id,
            content=content,
        )
