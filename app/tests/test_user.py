from fastapi.testclient import TestClient

from app.main import app

# from app.deps import engine, SessionDep
# from app.crud import get_users

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200


# def test_database_connection() -> None:
#     users = get_users(session=SessionDep)

#     print(users)
