from sentence_transformers import SentenceTransformer

from data_pipeline.embedding_generation.embedding_model import (
    EmbeddingInput,
    EmbeddingOutput,
)


class SentenceTransformerClient:
    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    EMBEDDING_DIMENSIONS = 384

    def __init__(self) -> None:
        self.model = SentenceTransformer(self.MODEL_NAME)

    def generate_embeddings(
        self,
        inputs: list[EmbeddingInput],
    ) -> list[EmbeddingOutput]:
        if not inputs:
            return []

        outputs: list[EmbeddingOutput] = []

        batch_size = 32
        total_inputs = len(inputs)
        for start in range(0, total_inputs, batch_size):
            batch = inputs[start : start + batch_size]

            vectors = self.model.encode(
                [item.content for item in batch],
                convert_to_numpy=True,
                normalize_embeddings=True,
                show_progress_bar=False,
            )

            outputs.extend(
                EmbeddingOutput(
                    chunk_id=item.chunk_id,
                    embedding=vector.tolist(),
                )
                for item, vector in zip(batch, vectors)
            )

        return outputs
