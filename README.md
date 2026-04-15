# Module 10 & 11: Secure User Model & Calculation System

## Overview
A FastAPI application with secure user authentication and a calculation system using SQLAlchemy, Pydantic, bcrypt, and a factory design pattern.

## How to Run Tests Locally

### 1. Start the database
```bash
docker-compose up -d db
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run unit tests (no database needed)
```bash
pytest tests/test_unit.py -v
```

### 4. Run integration tests (requires database)
```bash
TEST_DATABASE_URL=postgresql://user:password@localhost:5432/appdb pytest tests/test_integration.py -v
```

### 5. Run all tests
```bash
TEST_DATABASE_URL=postgresql://user:password@localhost:5432/appdb pytest -v
```

## Docker Hub
https://hub.docker.com/r/xing583/module10-is601

## Pull and run the image
```bash
docker pull xing583/module10-is601:latest
docker run -p 8000:8000 xing583/module10-is601:latest
```
