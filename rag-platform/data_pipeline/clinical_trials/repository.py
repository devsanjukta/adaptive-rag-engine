from sqlalchemy import bindparam, text
from sqlalchemy.dialects.postgresql import JSONB

from data_pipeline.models.clinical_trials import (
    IngestionCheckpoint,
    RawClinicalTrialDTO,
)
from data_pipeline.models.schema import SaveResult
from shared.database_repository import DatabaseRepository


class ClinicalTrialsRepository:
    UPSERT_QUERY = text("""
        INSERT INTO raw_clinical_trials (
            nct_id,
            raw_data,
            source_updated_at,
            fetched_at
        )
        VALUES (
            :nct_id,
            :raw_data,
            :source_updated_at,
            CURRENT_TIMESTAMP
        )
        ON CONFLICT (nct_id)
        DO UPDATE SET
            raw_data = EXCLUDED.raw_data,
            source_updated_at = EXCLUDED.source_updated_at,
            fetched_at = CURRENT_TIMESTAMP
        WHERE raw_clinical_trials.raw_data
            IS DISTINCT FROM EXCLUDED.raw_data
        RETURNING nct_id
    """).bindparams(bindparam("raw_data", type_=JSONB))

    def __init__(self, db: DatabaseRepository) -> None:
        self.db = db

    def save_studies(
        self,
        studies: list[RawClinicalTrialDTO],
    ) -> SaveResult:
        changed = 0
        unchanged = 0

        for study in studies:
            result = self.db.execute_returning(
                self.UPSERT_QUERY,
                {
                    "nct_id": study.nct_id,
                    "raw_data": study.raw_data,
                    "source_updated_at": study.source_updated_at,
                },
            )

            if result is not None:
                changed += 1
            else:
                unchanged += 1

        return SaveResult(
            processed=len(studies),
            changed=changed,
            unchanged=unchanged,
        )

    def get_latest_checkpoint(
        self,
        query: str,
    ) -> IngestionCheckpoint | None:
        return self.db.fetch_one(
            """
            SELECT *
            FROM ingestion_checkpoints
            WHERE query = :query
            ORDER BY page_order DESC
            LIMIT 1
            """,
            IngestionCheckpoint,
            {"query": query},
        )

    def save_checkpoint(
        self,
        query: str,
        next_page_token: str | None,
        page_order: int,
    ) -> None:
        self.db.execute(
            """
            INSERT INTO ingestion_checkpoints (
                query,
                next_page_token,
                page_order
            )
            VALUES (
                :query,
                :next_page_token,
                :page_order
            )
            """,
            {
                "query": query,
                "next_page_token": next_page_token,
                "page_order": page_order,
            },
        )
