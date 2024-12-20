from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_profile_success():
    response = client.post(
        "/profiles/",
        json={
            "name": "Shadiya Best",
            "email": "shadiyabest@example.com",
            "phone": "1234567890",
            "password": "Strong@123"
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Shadiya Best"

def test_create_profile_password_policy():
    response = client.post(
        "/profiles/",
        json={
            "name": "Shadiya B",
            "email": "shadiya@example.com",
            "phone": "1234567890",
            "password": "weakpass"
        }
    )
    assert response.status_code == 400
    assert "Password must" in response.json()["detail"]
