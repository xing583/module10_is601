import pytest
from pydantic import ValidationError
from app.models import User
from app.schemas import UserCreate

def test_hash_password_not_plain():
    hashed = User.hash_password("mypassword")
    assert hashed != "mypassword"

def test_verify_password_correct():
    hashed = User.hash_password("mypassword")
    assert User.verify_password("mypassword", hashed) is True

def test_verify_password_wrong():
    hashed = User.hash_password("mypassword")
    assert User.verify_password("wrongpassword", hashed) is False

def test_hash_is_unique():
    h1 = User.hash_password("same_password")
    h2 = User.hash_password("same_password")
    assert h1 != h2

def test_user_create_valid():
    user = UserCreate(username="alice", email="alice@example.com", password="secure123")
    assert user.username == "alice"

def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="bob", email="not-an-email", password="secure123")

def test_user_create_short_password():
    with pytest.raises(ValidationError):
        UserCreate(username="bob", email="bob@example.com", password="123")

def test_user_create_short_username():
    with pytest.raises(ValidationError):
        UserCreate(username="ab", email="bob@example.com", password="secure123")
