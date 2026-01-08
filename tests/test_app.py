import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Basketball" in data

def test_signup_and_unregister():
    # Use a unique email to avoid conflicts
    test_email = "pytestuser@mergington.edu"
    activity = "Basketball"
    # Signup
    response = client.post(f"/activities/{activity}/signup?email={test_email}")
    assert response.status_code in (200, 400)  # 400 if already signed up
    # Unregister
    response = client.delete(f"/activities/{activity}/unregister?email={test_email}")
    assert response.status_code in (200, 404)  # 404 if not found
