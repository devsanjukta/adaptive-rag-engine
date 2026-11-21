from sqlalchemy.orm import Session

from shared.database_repository import DatabaseRepository


def provide_database_repository(session: Session) -> DatabaseRepository:
    return DatabaseRepository(session)
