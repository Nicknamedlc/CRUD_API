from contextlib import contextmanager
from datetime import datetime

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from fast_zero.app import app
from fast_zero.models import User, table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///memory')
    table_registry.metadata.create_all(engine)
    with Session(engine) as s:
        yield s

    table_registry.metadata.drop_all(engine)


@contextmanager
def _mock_db_time(*, model=User, time=datetime.now()):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time
        if hasattr(target, 'updated_at'):
            target.updated_at = time

    event.listen(User, 'before_insert', fake_time_hook)

    yield time

    event.remove(User, 'before_insert', fake_time_hook)


@pytest.fixture
def mock_db_time():
    return _mock_db_time
