"""Card (meishi) router."""

from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.card import CardCreate, CardPublicResponse, CardResponse, CardUpdate
from app.services.card_service import CardService

router = APIRouter(prefix="/api/v1/cards", tags=["cards"])


@router.post("", response_model=CardResponse, status_code=status.HTTP_201_CREATED)
def create_card(
    data: CardCreate,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return CardService.create_card(db, current_user.id, data)


@router.get("", response_model=List[CardResponse])
def list_cards(
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return CardService.list_user_cards(db, current_user.id)


@router.get("/public/{slug}", response_model=CardPublicResponse)
def get_public_card(
    slug: str,
    db: Annotated[Session, Depends(get_db)],
):
    return CardService.get_public_card(db, slug)


@router.get("/{card_id}", response_model=CardResponse)
def get_card(
    card_id: int,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return CardService.get_user_card(db, current_user.id, card_id)


@router.patch("/{card_id}", response_model=CardResponse)
def update_card(
    card_id: int,
    data: CardUpdate,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return CardService.update_card(db, current_user.id, card_id, data)


@router.delete("/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_card(
    card_id: int,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    CardService.delete_card(db, current_user.id, card_id)
