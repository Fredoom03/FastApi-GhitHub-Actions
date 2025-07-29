# Internal Modules
from app.deps import get_session
from app.main import app

# External Modules
from sqlmodel import SQLModel, create_engine, Session, StaticPool
from fastapi.testclient import TestClient
from typing import Generator
import pytest 


TEST_URL = "sqlite:///test.db"

engine = create_engine(
    TEST_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

def db() -> Generator[Session, None, None]:
    with Session(engine) as e:
        yield e

@pytest.fixture(scope="module")
def setup_and_teardown():
    SQLModel.metadata.create_all(engine)
    yield 
    SQLModel.metadata.drop_all(engine) 


@pytest.fixture(scope="module")
def session_db() -> Generator[Session, None, None]:
    with Session(engine) as e: 
        yield e   

app.dependency_overrides[get_session] = db

@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c