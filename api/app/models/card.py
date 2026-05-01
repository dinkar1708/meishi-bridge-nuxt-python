"""Business card (meishi) model."""

import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


def _new_slug() -> str:
    return uuid.uuid4().hex[:12]


class Card(Base):
    """Business card belonging to a user."""

    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    public_slug = Column(String(32), unique=True, index=True, nullable=False, default=_new_slug)

    name = Column(String(255), nullable=False)
    name_kana = Column(String(255), nullable=True)
    name_en = Column(String(255), nullable=True)
    title = Column(String(255), nullable=True)
    company = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(64), nullable=True)
    website = Column(String(255), nullable=True)
    address = Column(String(500), nullable=True)
    bio = Column(Text, nullable=True)
    locale = Column(String(8), nullable=False, default="ja")

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    user = relationship("User", backref="cards")

    def __repr__(self):
        return f"<Card(id={self.id}, name='{self.name}', user_id={self.user_id})>"
