from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ApiModel(BaseModel):
    """Base configuration for external API response models."""

    model_config = ConfigDict(extra="ignore")


class StudiesResponse(ApiModel):
    studies: list[dict[str, Any]]
    next_page_token: str | None = Field(default=None, alias="nextPageToken")


class SaveResult(BaseModel):
    processed: int
    changed: int
    unchanged: int
