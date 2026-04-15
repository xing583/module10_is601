import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from app.database import Base, get_db

TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql://user:password@localhost:5432/appdb"
)

engine = create_engine(TEST_DATABASE_URL)
TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = TestingSession()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_create_user_success(client):
    response = client.post("/users", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepass"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert "password_hash" not in data

def test_duplicate_username(client):
    client.post("/users", json={"username": "dupuser", "email": "a@example.com", "password": "pass1234"})
    response = client.post("/users", json={"username": "dupuser", "email": "b@example.com", "password": "pass1234"})
    assert response.status_code == 409

def test_duplicate_email(client):
    client.post("/users", json={"username": "user1", "email": "same@example.com", "password": "pass1234"})
    response = client.post("/users", json={"username": "user2", "email": "same@example.com", "password": "pass1234"})
    assert response.status_code == 409

def test_get_user_not_found(client):
    response = client.get("/users/9999")
    assert response.status_code == 404
