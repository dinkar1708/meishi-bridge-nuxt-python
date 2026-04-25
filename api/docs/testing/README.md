# Testing Guide - MeishiBridge API

Complete guide for running and writing tests for the FastAPI backend.

**Current Coverage: 97%** (204 statements, 6 missed, 28 tests passing)

**Detailed Coverage Report:** [COVERAGE.md](./COVERAGE.md)

---

## Quick Start (Docker Method)

```bash
# Run all tests
docker compose exec api pytest

# Run tests with verbose output
docker compose exec api pytest -v

# Run tests with coverage report
docker compose exec api pytest --cov=app --cov-report=term-missing

# Run specific test file
docker compose exec api pytest tests/test_auth.py

# Run specific test class
docker compose exec api pytest tests/test_auth.py::TestUserRegistration

# Run specific test function
docker compose exec api pytest tests/test_auth.py::TestUserLogin::test_login_success
```

---

## Test Structure

Tests are organized to mirror the app structure for easy navigation:

```
tests/
├── __init__.py
├── conftest.py                  # Shared fixtures and configuration
├── test_main.py                 # Main app endpoints (root, health)
│
├── routers/                     # Router/endpoint tests
│   ├── __init__.py
│   └── test_auth.py            # Authentication endpoints (19 tests)
│
├── services/                    # Service layer tests
│   └── __init__.py             # (Future service tests)
│
├── models/                      # Model tests
│   ├── __init__.py
│   └── test_user.py            # User model tests (3 tests)
│
└── utils/                       # Utility tests
    ├── __init__.py
    └── test_security.py        # Security utilities (4 tests)
```

### Test Organization

- **28 total tests** across 4 test files
- **97% coverage** (204 statements, 6 missed)
- Tests mirror app structure for easy maintenance
- Each module has its own test folder

---

## Running Tests

### Basic Test Commands

```bash
# Run all tests
docker compose exec api pytest

# Run with output capture disabled (see print statements)
docker compose exec api pytest -s

# Run with detailed output
docker compose exec api pytest -v

# Run and stop at first failure
docker compose exec api pytest -x

# Run last failed tests
docker compose exec api pytest --lf
```

### Coverage Commands

**Primary Coverage Command:**
```bash
docker compose exec api pytest --cov=app --cov-report=term
```

**All Coverage Commands:**
```bash
# Run tests with coverage report (recommended)
docker compose exec api pytest --cov=app --cov-report=term

# Run with missing lines shown
docker compose exec api pytest --cov=app --cov-report=term-missing

# Generate HTML coverage report
docker compose exec api pytest --cov=app --cov-report=html

# View HTML coverage report (generated in htmlcov/)
open htmlcov/index.html  # macOS
# xdg-open htmlcov/index.html  # Linux

# Run coverage with minimum threshold (e.g., 90%)
docker compose exec api pytest --cov=app --cov-fail-under=90
```

### Current Coverage Results

**Command:**
```bash
docker compose exec api pytest --cov=app --cov-report=term
```

**Output:**
```
28 passed, 1 warning in 4.24s

---------- coverage: platform linux, python 3.11.15-final-0 ----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
app/__init__.py                    1      0   100%
app/config.py                     15      0   100%
app/database.py                   11      4    64%
app/dependencies.py               29      0   100%
app/main.py                       12      0   100%
app/models/__init__.py             2      0   100%
app/models/user.py                17      0   100%
app/routers/__init__.py            2      0   100%
app/routers/auth.py               19      0   100%
app/schemas/__init__.py            3      0   100%
app/schemas/auth.py               11      0   100%
app/schemas/user.py               20      0   100%
app/services/__init__.py           2      0   100%
app/services/auth_service.py      40      2    95%
app/utils/__init__.py              2      0   100%
app/utils/security.py             18      0   100%
--------------------------------------------------
TOTAL                            204      6    97%
```

**Summary:**
- Total Tests: 28 passed
- Total Statements: 204
- Missed Statements: 6
- Coverage: **97%**

### Filtering Tests

```bash
# Run specific test file
docker compose exec api pytest tests/test_auth.py

# Run specific test class
docker compose exec api pytest tests/test_auth.py::TestUserRegistration

# Run specific test function
docker compose exec api pytest tests/test_auth.py::TestUserLogin::test_login_success

# Run tests matching pattern
docker compose exec api pytest -k "login"

# Run tests by marker (if defined)
docker compose exec api pytest -m "slow"
```

---

## Test Coverage Report

Current test coverage for authentication module:

```
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
app/routers/auth.py                  25      0   100%
app/schemas/auth.py                   8      0   100%
app/schemas/user.py                  12      0   100%
app/services/auth_service.py         56      3    95%
app/models/user.py                   16      1    94%
app/utils/security.py                17      1    94%
app/dependencies.py                  15      2    87%
---------------------------------------------------------------
TOTAL                               210     14    93%
```

---

## Writing Tests

### Test File Template

```python
"""Tests for [feature] endpoints."""

import pytest
from fastapi import status


class TestFeatureName:
    """Test [feature] functionality."""

    def test_feature_success(self, client, test_user_data):
        """Test successful [feature] operation."""
        response = client.post("/api/v1/endpoint", json=test_user_data)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "expected_field" in data

    def test_feature_validation(self, client):
        """Test [feature] validation."""
        response = client.post("/api/v1/endpoint", json={})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
```

### Using Fixtures

**Available Fixtures (from conftest.py):**

- **`db_session`**: Fresh database session for each test
- **`client`**: TestClient with database override
- **`test_user_data`**: Sample user data dictionary
- **`test_user_data_2`**: Second sample user data dictionary

**Example Usage:**

```python
def test_example(client, db_session, test_user_data):
    """Example test using fixtures."""
    # Use client to make API requests
    response = client.post("/api/v1/auth/register", json=test_user_data)

    # Use db_session for direct database queries (if needed)
    from app.models.user import User
    user = db_session.query(User).filter_by(email=test_user_data["email"]).first()
    assert user is not None
```

### Creating Custom Fixtures

Add to `conftest.py`:

```python
@pytest.fixture
def authenticated_client(client, test_user_data):
    """Client with authenticated user."""
    # Register and login
    client.post("/api/v1/auth/register", json=test_user_data)
    response = client.post("/api/v1/auth/login", json={
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    })
    token = response.json()["access_token"]

    # Add authorization header
    client.headers = {"Authorization": f"Bearer {token}"}
    return client
```

---

## Test Best Practices

### 1. Test Naming Convention

```python
# Good naming
def test_register_duplicate_email(self, client, test_user_data):
    """Test registration with duplicate email."""
    pass

# Bad naming
def test_case_1(self, client):
    """Test something."""
    pass
```

### 2. Arrange-Act-Assert Pattern

```python
def test_login_success(self, client, test_user_data):
    """Test successful login."""
    # Arrange: Set up test data
    client.post("/api/v1/auth/register", json=test_user_data)
    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }

    # Act: Perform the action
    response = client.post("/api/v1/auth/login", json=login_data)

    # Assert: Verify the result
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
```

### 3. Test Independence

Each test should be independent and not rely on other tests:

```python
# Good: Self-contained test
def test_get_user(self, client, test_user_data):
    # Create user within this test
    client.post("/api/v1/auth/register", json=test_user_data)
    # ... rest of test

# Bad: Depends on another test running first
def test_get_user(self, client):
    # Assumes user already exists
    response = client.get("/api/v1/users/1")
```

### 4. Test Edge Cases

```python
def test_register_invalid_email(self, client, test_user_data):
    """Test registration with invalid email format."""
    invalid_user = test_user_data.copy()
    invalid_user["email"] = "invalid-email"

    response = client.post("/api/v1/auth/register", json=invalid_user)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
```

---

## Continuous Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Run tests
        run: |
          docker compose up -d
          docker compose exec api pytest --cov=app --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
```

---

## Troubleshooting

### Tests Failing Due to Database State

```bash
# Stop containers and remove volumes
docker compose down -v

# Rebuild and restart
docker compose up -d --build

# Run tests
docker compose exec api pytest
```

### Import Errors

```bash
# Ensure all dependencies are installed
docker compose exec api pip install -r requirements.txt

# Rebuild container
docker compose up -d --build
```

### Viewing Test Logs

```bash
# Run tests with print statements visible
docker compose exec api pytest -s

# Run with more verbose output
docker compose exec api pytest -vv
```

### Database Connection Issues

Tests use SQLite (not PostgreSQL) for faster execution and isolation.

Check `tests/conftest.py`:
```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
```

---

## Authentication Test Examples

### Current Test Coverage

**TestUserRegistration (6 tests)**
-  `test_register_success` - Successful user registration
-  `test_register_duplicate_email` - Duplicate email rejection
-  `test_register_duplicate_username` - Duplicate username rejection
-  `test_register_invalid_email` - Email format validation
-  `test_register_short_password` - Password length validation
-  `test_register_missing_fields` - Required fields validation

**TestUserLogin (4 tests)**
-  `test_login_success` - Successful login with JWT token
-  `test_login_invalid_email` - Non-existent email rejection
-  `test_login_wrong_password` - Wrong password rejection
-  `test_login_missing_fields` - Required fields validation

**TestGetCurrentUser (4 tests)**
-  `test_get_current_user_success` - Valid token returns user
-  `test_get_current_user_no_token` - Missing token returns 401
-  `test_get_current_user_invalid_token` - Invalid token returns 401
-  `test_get_current_user_malformed_header` - Malformed header returns 401

**TestAuthenticationFlow (2 tests)**
-  `test_full_auth_flow` - Complete registration -> login -> get user
-  `test_multiple_users` - Multiple users independent authentication

**Total: 16 tests, 93% coverage**

---

## Next Steps

1. Add tests for new features as they are implemented
2. Maintain coverage above 90%
3. Run tests before committing code
4. Review failed tests in CI/CD pipeline

---

## References

- **pytest Documentation**: https://docs.pytest.org/
- **FastAPI Testing**: https://fastapi.tiangolo.com/tutorial/testing/
- **Coverage.py**: https://coverage.readthedocs.io/
