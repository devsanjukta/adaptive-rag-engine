from pathlib import Path

from sklearn.model_selection import GroupShuffleSplit

from reranker.dataset_utils import DatasetUtils
from reranker.models import RerankerDatasetRecord
from shared.config import (
    RERANKER_FULL_DATASET_PATH,
    RERANKING_TEST_PATH,
    RERANKING_TRAINING_PATH,
    RERANKING_VALIDATION_PATH,
)
from shared.utils import Utils


class DatasetSplitter:
    GROUP_COLUMN = "nct_id"

    TRAIN_RATIO = 0.70
    VALIDATION_RATIO = 0.15
    TEST_RATIO = 0.15

    RANDOM_STATE = 42

    def __init__(self):
        self.input_path = RERANKER_FULL_DATASET_PATH
        self.records: list[RerankerDatasetRecord] = []

        self._validate_ratios()

    def _validate_ratios(self):
        ratios = [
            self.TRAIN_RATIO,
            self.VALIDATION_RATIO,
            self.TEST_RATIO,
        ]

        if any(ratio <= 0 or ratio >= 1 for ratio in ratios):
            raise ValueError("Each split ratio must be greater than 0 and less than 1.")

        if not abs(sum(ratios) - 1.0) < 1e-9:
            raise ValueError("Split ratios must add up to 1.0.")

    def _load_dataset(self):
        try:
            self.records = DatasetUtils.fetch_reranker_records(self.input_path)
        except Exception as ex:
            print(f"Error loading dataset: {ex!s}")
            raise

    def _save_datasets(self, indices: list[int], dataset_path: Path) -> None:
        records = [self.records[index].model_dump() for index in indices]

        Utils.export_dataset(dataset_path, records)

        print(f"Saved {len(records)} records to {dataset_path}")

    def _split_dataset(self) -> tuple[list[int], list[int], list[int]]:
        if not self.records:
            raise ValueError("Records are empty. Load the dataset first.")

        groups = [record.nct_id for record in self.records]

        train_splitter = GroupShuffleSplit(
            n_splits=1,
            train_size=self.TRAIN_RATIO,
            random_state=self.RANDOM_STATE,
        )

        train_indices, remaining_indices = next(
            train_splitter.split(self.records, groups=groups)
        )

        remaining_records = [self.records[i] for i in remaining_indices]
        remaining_groups = [record.nct_id for record in remaining_records]

        validation_ratio = self.VALIDATION_RATIO / (
            self.VALIDATION_RATIO + self.TEST_RATIO
        )

        remaining_splitter = GroupShuffleSplit(
            n_splits=1,
            train_size=validation_ratio,
            random_state=self.RANDOM_STATE,
        )

        validation_indices, test_indices = next(
            remaining_splitter.split(remaining_records, groups=remaining_groups)
        )

        return (
            train_indices.tolist(),
            remaining_indices[validation_indices].tolist(),
            remaining_indices[test_indices].tolist(),
        )

    def run(self) -> None:
        self._load_dataset()
        training_indices, validation_indices, test_indices = self._split_dataset()

        self._save_datasets(training_indices, RERANKING_TRAINING_PATH)
        self._save_datasets(validation_indices, RERANKING_VALIDATION_PATH)
        self._save_datasets(test_indices, RERANKING_TEST_PATH)
