from datetime import UTC, datetime
from typing import Any

from data_pipeline.clinical_trials.client import ClinicalTrialsClient
from data_pipeline.clinical_trials.repository import ClinicalTrialsRepository
from data_pipeline.models.clinical_trials import (
    RawClinicalTrialDTO,
)
from data_pipeline.models.schema import SaveResult


class ClinicalTrialsService:
    """Coordinates clinical trial ingestion."""

    PAGE_SIZE = 100
    MAX_RECORDS = 500

    def __init__(
        self,
        client: ClinicalTrialsClient,
        repository: ClinicalTrialsRepository,
    ) -> None:
        self.client = client
        self.repository = repository

    @staticmethod
    def _transform_study(
        study: dict[str, Any],
    ) -> RawClinicalTrialDTO:
        protocol_section = study.get("protocolSection", {})

        identification = protocol_section.get("identificationModule", {})
        status = protocol_section.get("statusModule", {})

        nct_id = identification.get("nctId")

        if not isinstance(nct_id, str) or not nct_id.strip():
            raise ValueError("Clinical study is missing a valid NCT ID.")

        date_value = status.get("studyLastUpdatePostDateStruct", {}).get("date")

        source_updated_at = None

        if isinstance(date_value, str):
            try:
                source_updated_at = datetime.fromisoformat(date_value).replace(
                    tzinfo=UTC
                )
            except ValueError:
                pass

        return RawClinicalTrialDTO(
            nct_id=nct_id,
            raw_data=study,
            source_updated_at=source_updated_at,
        )

    def ingest_studies(self, condition: str) -> SaveResult:
        latest_checkpoint = self.repository.get_latest_checkpoint(condition)

        page_token = (
            latest_checkpoint.next_page_token if latest_checkpoint is not None else None
        )

        page_order = (
            latest_checkpoint.page_order if latest_checkpoint is not None else 0
        )

        processed = page_order * self.PAGE_SIZE
        changed = 0
        unchanged = 0

        while processed < self.MAX_RECORDS:
            remaining = self.MAX_RECORDS - processed
            page_size = min(self.PAGE_SIZE, remaining)

            response = self.client.fetch_studies_page(
                condition=condition,
                page_size=page_size,
                page_token=page_token,
            )

            studies = [self._transform_study(study) for study in response.studies]

            save_result = self.repository.save_studies(studies)

            processed += save_result.processed
            changed += save_result.changed
            unchanged += save_result.unchanged

            page_order += 1
            page_token = response.next_page_token

            self.repository.save_checkpoint(
                query=condition,
                next_page_token=page_token,
                page_order=page_order,
            )

            if page_token is None or not studies:
                break

        return SaveResult(
            processed=processed,
            changed=changed,
            unchanged=unchanged,
        )
