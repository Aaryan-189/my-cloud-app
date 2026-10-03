from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Test 1: Verify the root endpoint returns the correct welcome message
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from Cloud App!"}

# Test 2: Verify the health check endpoint for load balancers/container orchestration
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# Test 3: Verify dynamic routing works with an integer item_id
def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "description": "This is a sample item"}

# Test 4: Verify the server correctly accepts and processes POST request payloads
def test_echo_data():
    payload = {"name": "Assessment User", "project": "Docker Deployment"}
    response = client.post("/echo", json=payload)
    assert response.status_code == 200
    assert response.json() == {"echo": payload}