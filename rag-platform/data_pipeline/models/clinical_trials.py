from datetime import datetime
from typing import Any

from pydantic import BaseModel


class RawClinicalTrialDTO(BaseModel):
    nct_id: str
    raw_data: dict[str, Any]
    source_updated_at: datetime | None = None


class IngestionCheckpoint(BaseModel):
    id: int | None = None
    query: str
    next_page_token: str | None = None
    page_order: int
