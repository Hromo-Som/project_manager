from typing import Generator

import pytest

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.models import Base


@pytest.fixture(scope='session')
def test_engine(
    tmp_path_factory: pytest.TempPathFactory
) -> Generator[Engine, None, None]:
    database_dir = tmp_path_factory.mktemp('database')

    database_path = database_dir / 'test.sqlite3'

    engine = create_engine(
        f'sqlite+pysqlite:///{database_path}',
        echo=False,
    )

    Base.metadata.create_all(engine)

    try:
        yield engine
    finally:
        Base.metadata.drop_all(engine)
        engine.dispose()


@pytest.fixture
def db_session(
    test_engine: Engine
) -> Generator[Session, None, None]:
    with Session(
        test_engine,
        expire_on_commit=False,
    ) as session:
        try:
            yield session
        finally:
            session.rollback()
