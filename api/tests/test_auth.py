"""Tests for authentication endpoints."""

import pytest
from fastapi import status


class TestUserRegistration:
    """Test user registration endpoint."""

    def test_register_success(self, client, test_user_data):
        """Test successful user registration."""
        response = client.post("/api/v1/auth/register", json=test_user_data)

        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["email"] == test_user_data["email"]
        assert data["username"] == test_user_data["username"]
        assert data["full_name"] == test_user_data["full_name"]
        assert data["is_active"] is True
        assert data["is_verified"] is False
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data
        assert "password" not in data  # Password should not be returned

    def test_register_duplicate_email(self, client, test_user_data):
        """Test registration with duplicate email."""
        # Register first user
        client.post("/api/v1/auth/register", json=test_user_data)

        # Try to register with same email
        response = client.post("/api/v1/auth/register", json=test_user_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "Email already registered" in response.json()["detail"]

    def test_register_duplicate_username(self, client, test_user_data):
        """Test registration with duplicate username."""
        # Register first user
        client.post("/api/v1/auth/register", json=test_user_data)

        # Try to register with same username but different email
        duplicate_user = test_user_data.copy()
        duplicate_user["email"] = "different@example.com"

        response = client.post("/api/v1/auth/register", json=duplicate_user)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "Username already taken" in response.json()["detail"]

    def test_register_invalid_email(self, client, test_user_data):
        """Test registration with invalid email format."""
        invalid_user = test_user_data.copy()
        invalid_user["email"] = "invalid-email"

        response = client.post("/api/v1/auth/register", json=invalid_user)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_register_short_password(self, client, test_user_data):
        """Test registration with password too short."""
        short_pass_user = test_user_data.copy()
        short_pass_user["password"] = "short"

        response = client.post("/api/v1/auth/register", json=short_pass_user)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_register_missing_fields(self, client):
        """Test registration with missing required fields."""
        response = client.post("/api/v1/auth/register", json={
            "email": "test@example.com"
        })

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestUserLogin:
    """Test user login endpoint."""

    def test_login_success(self, client, test_user_data):
        """Test successful login."""
        # Register user first
        client.post("/api/v1/auth/register", json=test_user_data)

        # Login
        login_data = {
            "email": test_user_data["email"],
            "password": test_user_data["password"]
        }
        response = client.post("/api/v1/auth/login", json=login_data)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert len(data["access_token"]) > 0

    def test_login_invalid_email(self, client, test_user_data):
        """Test login with non-existent email."""
        login_data = {
            "email": "nonexistent@example.com",
            "password": "password123"
        }
        response = client.post("/api/v1/auth/login", json=login_data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "Incorrect email or password" in response.json()["detail"]

    def test_login_wrong_password(self, client, test_user_data):
        """Test login with wrong password."""
        # Register user first
        client.post("/api/v1/auth/register", json=test_user_data)

        # Login with wrong password
        login_data = {
            "email": test_user_data["email"],
            "password": "wrongpassword"
        }
        response = client.post("/api/v1/auth/login", json=login_data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "Incorrect email or password" in response.json()["detail"]

    def test_login_missing_fields(self, client):
        """Test login with missing fields."""
        response = client.post("/api/v1/auth/login", json={
            "email": "test@example.com"
        })

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestGetCurrentUser:
    """Test get current user endpoint."""

    def test_get_current_user_success(self, client, test_user_data):
        """Test getting current user with valid token."""
        # Register and login
        client.post("/api/v1/auth/register", json=test_user_data)
        login_response = client.post("/api/v1/auth/login", json={
            "email": test_user_data["email"],
            "password": test_user_data["password"]
        })
        token = login_response.json()["access_token"]

        # Get current user
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": f"Bearer {token}"}
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["email"] == test_user_data["email"]
        assert data["username"] == test_user_data["username"]
        assert data["full_name"] == test_user_data["full_name"]
        assert "password" not in data

    def test_get_current_user_no_token(self, client):
        """Test getting current user without token."""
        response = client.get("/api/v1/auth/me")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_invalid_token(self, client):
        """Test getting current user with invalid token."""
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": "Bearer invalid_token"}
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_malformed_header(self, client):
        """Test getting current user with malformed auth header."""
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": "InvalidFormat token"}
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestAuthenticationFlow:
    """Test complete authentication flow."""

    def test_full_auth_flow(self, client, test_user_data):
        """Test complete registration -> login -> get user flow."""
        # 1. Register
        register_response = client.post("/api/v1/auth/register", json=test_user_data)
        assert register_response.status_code == status.HTTP_201_CREATED
        user_id = register_response.json()["id"]

        # 2. Login
        login_response = client.post("/api/v1/auth/login", json={
            "email": test_user_data["email"],
            "password": test_user_data["password"]
        })
        assert login_response.status_code == status.HTTP_200_OK
        token = login_response.json()["access_token"]

        # 3. Get current user
        me_response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert me_response.status_code == status.HTTP_200_OK
        assert me_response.json()["id"] == user_id

    def test_multiple_users(self, client, test_user_data, test_user_data_2):
        """Test that multiple users can register and login independently."""
        # Register two users
        client.post("/api/v1/auth/register", json=test_user_data)
        client.post("/api/v1/auth/register", json=test_user_data_2)

        # Login as user 1
        login1 = client.post("/api/v1/auth/login", json={
            "email": test_user_data["email"],
            "password": test_user_data["password"]
        })
        token1 = login1.json()["access_token"]

        # Login as user 2
        login2 = client.post("/api/v1/auth/login", json={
            "email": test_user_data_2["email"],
            "password": test_user_data_2["password"]
        })
        token2 = login2.json()["access_token"]

        # Verify each token returns correct user
        me1 = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token1}"})
        me2 = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token2}"})

        assert me1.json()["email"] == test_user_data["email"]
        assert me2.json()["email"] == test_user_data_2["email"]
        assert me1.json()["id"] != me2.json()["id"]
