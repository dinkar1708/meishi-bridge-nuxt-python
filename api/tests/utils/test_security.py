"""Tests for utility functions."""

import pytest
from datetime import timedelta
from jose import jwt

from app.config import settings
from app.utils.security import (
    create_access_token,
    get_password_hash,
    verify_password,
)


class TestPasswordHashing:
    """Test password hashing utilities."""

    def test_password_hashing(self):
        """Test password hashing and verification."""
        password = "testpassword123"
        hashed = get_password_hash(password)

        assert hashed != password
        assert verify_password(password, hashed) is True
        assert verify_password("wrongpassword", hashed) is False


class TestJWTTokens:
    """Test JWT token creation and decoding."""

    def test_create_token(self):
        """Test creating JWT tokens."""
        data = {"sub": "123", "email": "test@example.com"}
        token = create_access_token(data)

        assert token is not None
        assert len(token) > 0

        # Decode token manually to verify
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        assert decoded["sub"] == "123"
        assert decoded["email"] == "test@example.com"
        assert "exp" in decoded

    def test_create_token_with_custom_expiry(self):
        """Test creating token with custom expiration."""
        data = {"sub": "456", "email": "test2@example.com"}
        expires_delta = timedelta(minutes=15)
        token = create_access_token(data, expires_delta=expires_delta)

        # Decode to verify
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        assert decoded["sub"] == "456"
        assert "exp" in decoded

    def test_token_expiration_time(self):
        """Test token contains expiration time."""
        data = {"sub": "789"}
        token = create_access_token(data)

        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        assert "exp" in decoded
        assert decoded["exp"] > 0
