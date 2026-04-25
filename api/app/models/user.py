"""User model for authentication and profile management."""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    """User model for authentication."""

    __tablename__ = "users"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Authentication
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    # Profile
    full_name = Column(String(255), nullable=True)

    # Account Status
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships (to be added later)
    # business_cards = relationship("BusinessCard", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        """String representation of User."""
        return f"<User(id={self.id}, email='{self.email}', username='{self.username}')>"
