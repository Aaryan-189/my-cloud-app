from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from Cloud App!"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "version": "1.1.0"}

def test_read_item_success():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "description": "This is a sample item"}

def test_read_item_failure():
    # Verify the application correctly rejects invalid IDs
    response = client.get("/items/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Item ID must be positive"}

def test_echo_data():
    payload = {"name": "Assessment User", "project": "Docker Deployment"}
    response = client.post("/echo", json=payload)
    assert response.status_code == 200
    assert response.json() == {"echo": payload}