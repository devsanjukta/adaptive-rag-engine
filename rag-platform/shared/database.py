from collections.abc import Generator, Iterator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from shared.config import get_settings

settings = get_settings()

# Create the PostgreSQL database engine.
engine = create_engine(settings.DATABASE_URL)

# Factory for creating database sessions.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    """Base class for all database models."""


def get_db() -> Generator[Session, None, None]:
    """Provide a database session and close it after use."""
    with SessionLocal() as session:
        yield session


@contextmanager
def provide_db_session() -> Iterator[Session]:
    with SessionLocal.begin() as session:
        yield session
