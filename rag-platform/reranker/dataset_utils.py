from pathlib import Path

import pandas as pd

from reranker.dataset_record_validator import DatasetRecordValidator
from reranker.models import RerankerDatasetRecord
from shared.utils import Utils


class DatasetUtils:
    @staticmethod
    def fetch_reranker_records(
        dataset_path: Path,
    ) -> list[RerankerDatasetRecord]:

        records = Utils.load_dataset(dataset_path)
        DatasetRecordValidator.validate_columns(records)

        return [
            RerankerDatasetRecord(
                row_number=index + 2,
                query=row["query"],
                document=row["document"],
                label=row["label"],
                nct_id=row["nct_id"],
                negative_type=(
                    None
                    if row["negative_type"] is None or pd.isna(row["negative_type"])
                    else row["negative_type"]
                ),
            )
            for index, row in enumerate(records)
        ]
