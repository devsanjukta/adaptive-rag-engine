from pathlib import Path

from reranker.dataset_record_validator import DatasetRecordValidator
from reranker.dataset_utils import DatasetUtils
from reranker.models import (
    DatasetValidationResult,
    RecordValidationResult,
    RerankerDatasetRecord,
)
from shared.config import RERANKER_FULL_DATASET_PATH


class DatasetValidator:
    def __init__(self, dataset_path: Path):
        self.dataset_path = RERANKER_FULL_DATASET_PATH
        self.records: list[RerankerDatasetRecord] = []

    def _load_dataset(self) -> None:
        try:
            self.records = DatasetUtils.fetch_reranker_records(self.dataset_path)

            print(f"Dataset loaded successfully: {len(self.records)} records")

        except Exception as ex:
            print(f"Error loading dataset: {ex!s}")
            raise

    def _validate_data(self) -> DatasetValidationResult:
        if not self.records:
            raise ValueError("Records are empty, please load dataset first.")

        validation_results: list[RecordValidationResult] = []

        for record in self.records:
            result = DatasetRecordValidator.validate(record)
            validation_results.append(result)

        valid_records = sum(result.is_valid for result in validation_results)

        invalid_records = len(validation_results) - valid_records

        validation_result = DatasetValidationResult(
            total_records=len(self.records),
            valid_records=valid_records,
            invalid_records=invalid_records,
            record_results=validation_results,
        )

        print("Dataset validation completed.")
        print(f"Total records: {validation_result.total_records}")
        print(f"Valid records: {validation_result.valid_records}")
        print(f"Invalid records: {validation_result.invalid_records}")

        if invalid_records > 0:
            error_messages = []

            for result in validation_results:
                if not result.is_valid:
                    errors = (
                        result.missing_fields_errors
                        + result.negative_type_errors
                        + result.label_errors
                    )

                    error_messages.append(
                        f"Excel row {result.excel_row_number}: {', '.join(errors)}"
                    )

            raise ValueError("Dataset validation failed:\n" + "\n".join(error_messages))

        print("All dataset records are valid.")

        return validation_result

    def run(self):
        self._load_dataset()
        return self._validate_data()
