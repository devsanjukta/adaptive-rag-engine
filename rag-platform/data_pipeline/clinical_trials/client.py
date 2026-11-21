from types import TracebackType
from typing import Self

import requests

from data_pipeline.models.schema import StudiesResponse
from shared.external_endpoints import CLINICAL_TRIALS_API_BASE_URL


# Fetch data from ClinicalTrials.gov
class ClinicalTrialsClient:
    """Client for the ClinicalTrials.gov API."""

    STUDIES_ENDPOINT = f"{CLINICAL_TRIALS_API_BASE_URL}/studies"

    def __init__(self, timeout: int = 30) -> None:
        self.timeout = timeout
        self.session = requests.Session()

    def fetch_studies_page(
        self,
        condition: str,
        page_size: int = 100,
        page_token: str | None = None,
    ) -> StudiesResponse:
        """Fetch one page of clinical trials."""

        if not condition.strip():
            raise ValueError("Condition cannot be empty.")

        if not 1 <= page_size <= 1000:
            raise ValueError("Page size must be between 1 and 1000.")

        params = {
            "query.cond": condition,
            "pageSize": page_size,
            "format": "json",
        }

        if page_token:
            params["pageToken"] = page_token

        response = self.session.get(
            self.STUDIES_ENDPOINT,
            params=params,
            timeout=self.timeout,
        )
        response.raise_for_status()

        return StudiesResponse.model_validate(response.json())

    def close(self) -> None:
        """Close the HTTP session."""
        self.session.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()
