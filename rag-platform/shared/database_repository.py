from typing import Any, TypeVar

from sqlalchemy import text
from sqlalchemy.orm import Session

T = TypeVar("T")


class DatabaseRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def execute(
        self,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> None:
        self.session.execute(text(query), params or {})

    def execute_returning(
        self,
        query: Any,
        params: dict[str, Any] | None = None,
    ) -> Any | None:
        result = self.session.execute(query, params or {})
        return result.scalar_one_or_none()

    def fetch_one(
        self,
        query: str,
        model: type[T],
        params: dict[str, Any] | None = None,
    ) -> T | None:
        result = self.session.execute(text(query), params or {})
        row = result.mappings().one_or_none()

        if row is None:
            return None

        return model(**dict(row))

    def fetch_all(
        self,
        query: str,
        model: type[T],
        params: dict[str, Any] | None = None,
    ) -> list[T]:
        result = self.session.execute(text(query), params or {})

        return [model(**dict(row)) for row in result.mappings().all()]

    def execute_many(self, query: str, params: list[dict[str, Any]]) -> None:
        self.session.execute(text(query), params)
