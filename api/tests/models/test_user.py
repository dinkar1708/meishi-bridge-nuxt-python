"""Tests for database models."""

import pytest
from datetime import datetime

from app.models.user import User


class TestUserModel:
    """Test User model."""

    def test_user_creation(self, db_session):
        """Test creating a user model."""
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashed_password_here",
            full_name="Test User"
        )

        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        assert user.id is not None
        assert user.email == "test@example.com"
        assert user.username == "testuser"
        assert user.is_active is True
        assert user.is_verified is False
        assert isinstance(user.created_at, datetime)
        assert isinstance(user.updated_at, datetime)

    def test_user_repr(self, db_session):
        """Test User __repr__ method."""
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashed",
            full_name="Test User"
        )

        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        # Test __repr__ method
        repr_str = repr(user)
        assert "User" in repr_str
        assert user.email in repr_str
        assert user.username in repr_str
        assert str(user.id) in repr_str

    def test_user_defaults(self, db_session):
        """Test User model default values."""
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashed"
        )

        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        # Test defaults
        assert user.full_name is None
        assert user.is_active is True
        assert user.is_verified is False
