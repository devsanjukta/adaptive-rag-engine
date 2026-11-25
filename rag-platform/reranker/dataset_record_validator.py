from reranker.models import (
    RecordValidationResult,
    RerankerDatasetRecord,
)


class DatasetRecordValidator:
    @staticmethod
    def validate(
        record: RerankerDatasetRecord,
    ) -> RecordValidationResult:

        result = RecordValidationResult(row_number=record.row_number)

        DatasetRecordValidator._validate_required_fields(record, result)
        DatasetRecordValidator._validate_negative_type(record, result)
        DatasetRecordValidator._validate_label(record, result)

        return result

    @staticmethod
    def _validate_required_fields(
        record: RerankerDatasetRecord,
        result: RecordValidationResult,
    ):

        required_fields = {
            "query": record.query,
            "document": record.document,
            "nct_id": record.nct_id,
        }

        for field, value in required_fields.items():
            if not value or not value.strip():
                result.missing_fields_errors.append(f"{field} is missing")

    @staticmethod
    def _validate_negative_type(
        record: RerankerDatasetRecord,
        result: RecordValidationResult,
    ):

        negative_type = record.negative_type

        if record.label == 0:
            if not negative_type or not negative_type.strip():
                result.negative_type_errors.append(
                    "negative_type is missing for negative example"
                )
            elif negative_type not in ["easy", "hard"]:
                result.negative_type_errors.append(
                    f"Invalid negative_type: {negative_type}"
                )

        elif record.label == 1 and negative_type:
            result.negative_type_errors.append(
                "negative_type should be empty for positive example"
            )

    @staticmethod
    def _validate_label(
        record: RerankerDatasetRecord,
        result: RecordValidationResult,
    ) -> None:

        if record.label not in [0, 1]:
            result.label_errors.append(f"Invalid label: {record.label}")

    @staticmethod
    def validate_columns(records: list[dict]) -> None:
        if not records:
            raise ValueError("Dataset is empty.")

        required_columns = {
            "query",
            "document",
            "label",
            "nct_id",
            "negative_type",
        }

        available_columns = set(records[0].keys())
        missing_columns = required_columns - available_columns

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing_columns))}"
            )
