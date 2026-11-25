from pathlib import Path

from sentence_transformers import CrossEncoder, InputExample
from sentence_transformers.cross_encoder.evaluation import (
    CEBinaryClassificationEvaluator,
)
from torch.utils.data import DataLoader

from reranker.dataset_utils import DatasetUtils
from reranker.models import RerankerDatasetRecord
from shared.config import (
    RERANKING_TRAINED_MODEL_PATH,
    RERANKING_TRAINING_MODEL_NAME,
    RERANKING_TRAINING_PATH,
    RERANKING_VALIDATION_PATH,
)


class ModelTrainer:
    model_name = RERANKING_TRAINING_MODEL_NAME

    training_path: Path = RERANKING_TRAINING_PATH
    validation_path: Path = RERANKING_VALIDATION_PATH

    output_path: Path = RERANKING_TRAINED_MODEL_PATH

    batch_size = 16
    epochs = 3
    evaluation_steps = 50

    def __init__(self):
        self.model = CrossEncoder(
            self.model_name,
            num_labels=1,
        )
        self.training_data: list[RerankerDatasetRecord] = []
        self.validation_data: list[RerankerDatasetRecord] = []

    def _load_datasets(self) -> None:
        self.training_data = DatasetUtils.fetch_reranker_records(self.training_path)
        self.validation_data = DatasetUtils.fetch_reranker_records(self.validation_path)

    def _create_training_dataloader(self) -> DataLoader:
        training_examples = [
            InputExample(
                texts=[row.query, row.document],
                label=float(row.label),
            )
            for row in self.training_data
        ]

        return DataLoader(
            training_examples,
            shuffle=True,
            batch_size=self.batch_size,
        )

    def _create_validation_evaluator(self):
        return CEBinaryClassificationEvaluator(
            sentence_pairs=[[row.query, row.document] for row in self.validation_data],
            labels=[row.label for row in self.validation_data],
            name="clinical_trials_validation",
        )

    def _train_model(self) -> None:
        train_dataloader = self._create_training_dataloader()
        evaluator = self._create_validation_evaluator()

        warmup_steps = int(len(train_dataloader) * self.epochs * 0.1)

        self.output_path.mkdir(parents=True, exist_ok=True)

        self.model.fit(
            train_dataloader=train_dataloader,
            evaluator=evaluator,
            epochs=self.epochs,
            evaluation_steps=self.evaluation_steps,
            warmup_steps=warmup_steps,
            output_path=str(self.output_path),
            save_best_model=True,
            show_progress_bar=True,
        )

    def run(self) -> None:
        self._load_datasets()
        self._train_model()

        print("Model training completed successfully.")
        print(f"Trained model saved at: {self.output_path}")
