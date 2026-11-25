from pathlib import Path

import pandas as pd

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

    @staticmethod
    def load_dataset(dataset_path: Path) -> list[dict]:
        if not dataset_path.exists():
            raise FileNotFoundError(f"Dataset file not found: {dataset_path}")

        df = pd.read_csv(dataset_path)

        if df.empty:
            raise ValueError("Dataset is empty.")

        return df.to_dict(orient="records")

    @staticmethod
    def export_dataset(dataset_path: Path, records: list[dict]):
        if not records:
            raise ValueError("records are empty")

        dataset_path.parent.mkdir(parents=True, exist_ok=True)

        df = pd.DataFrame(records)
        df.to_csv(dataset_path, index=False)
