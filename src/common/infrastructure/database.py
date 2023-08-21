from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from ..dependencies import get_settings

Base = declarative_base()

__SETTINGS = get_settings()

engine = create_engine(__SETTINGS.db_url)

SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)


def get_session() -> Iterator[Session]:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
