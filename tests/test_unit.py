import pytest
from pydantic import ValidationError
from app.models import User
from app.schemas import UserCreate, CalculationCreate
from app.calculator import CalculationFactory, CalculationType

# ---- 密码哈希测试 ----
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

# ---- User Schema 测试 ----
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

# ---- 工厂模式测试 ----
def test_factory_add():
    op = CalculationFactory.create(CalculationType.ADD)
    assert op.calculate(3, 4) == 7

def test_factory_subtract():
    op = CalculationFactory.create(CalculationType.SUBTRACT)
    assert op.calculate(10, 3) == 7

def test_factory_multiply():
    op = CalculationFactory.create(CalculationType.MULTIPLY)
    assert op.calculate(3, 4) == 12

def test_factory_divide():
    op = CalculationFactory.create(CalculationType.DIVIDE)
    assert op.calculate(10, 2) == 5

def test_factory_divide_by_zero():
    op = CalculationFactory.create(CalculationType.DIVIDE)
    with pytest.raises(ValueError):
        op.calculate(10, 0)

# ---- Calculation Schema 测试 ----
def test_calculation_create_valid():
    calc = CalculationCreate(a=10, b=2, type="Add")
    assert calc.a == 10

def test_calculation_create_divide_by_zero():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=0, type="Divide")

def test_calculation_create_invalid_type():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=2, type="InvalidOp")
