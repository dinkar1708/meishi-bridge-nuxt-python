"""Card (meishi) schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class CardBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    name_kana: Optional[str] = Field(None, max_length=255)
    name_en: Optional[str] = Field(None, max_length=255)
    title: Optional[str] = Field(None, max_length=255)
    company: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=64)
    website: Optional[str] = Field(None, max_length=255)
    address: Optional[str] = Field(None, max_length=500)
    bio: Optional[str] = None
    locale: str = Field("ja", pattern="^(ja|en)$")


class CardCreate(CardBase):
    pass


class CardUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    name_kana: Optional[str] = Field(None, max_length=255)
    name_en: Optional[str] = Field(None, max_length=255)
    title: Optional[str] = Field(None, max_length=255)
    company: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=64)
    website: Optional[str] = Field(None, max_length=255)
    address: Optional[str] = Field(None, max_length=500)
    bio: Optional[str] = None
    locale: Optional[str] = Field(None, pattern="^(ja|en)$")


class CardResponse(CardBase):
    id: int
    user_id: int
    public_slug: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CardPublicResponse(CardBase):
    """Public-facing card response (no internal IDs)."""

    public_slug: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
