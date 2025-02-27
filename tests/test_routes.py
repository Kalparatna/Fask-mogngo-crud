import pytest
from app import create_app
from app import mongo

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    yield client

def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200

def test_create_user(client):
    response = client.post("/users", json={"name": "John", "email": "john@example.com", "password": "123456"})
    assert response.status_code == 201

def test_update_user(client):
    user = mongo.db.users.find_one()
    user_id = str(user["_id"])
    response = client.put(f"/users/{user_id}", json={"name": "Updated Name"})
    assert response.status_code == 200

def test_delete_user(client):
    user = mongo.db.users.find_one()
    user_id = str(user["_id"])
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
