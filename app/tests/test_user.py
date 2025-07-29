from fastapi.testclient import TestClient

def test_health(client: TestClient) -> None:
    response = client.get("/health")
    
    assert response.status_code == 200  
    
def test_create_user(client: TestClient, setup_and_teardown) -> None:
    response = client.post("/user/", json={"name": "John Doe", "age": 30})

    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John Doe", "age": 30, "id": 1}
    
def test_get_users(client: TestClient, setup_and_teardown) -> None: 
    response = client.get("/user/")
    
    assert response.status_code == 200
    assert response.json() is not None
    
def test_get_user_by_id(client: TestClient, setup_and_teardown) -> None: 
    response = client.get("/user/1")
    print(response.json())
    assert response.status_code == 200