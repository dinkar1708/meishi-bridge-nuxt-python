"""Card (meishi) business logic."""

from typing import List, Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.card import Card
from app.schemas.card import CardCreate, CardUpdate


class CardService:
    @staticmethod
    def create_card(db: Session, user_id: int, data: CardCreate) -> Card:
        card = Card(user_id=user_id, **data.model_dump())
        db.add(card)
        db.commit()
        db.refresh(card)
        return card

    @staticmethod
    def list_user_cards(db: Session, user_id: int) -> List[Card]:
        return (
            db.query(Card)
            .filter(Card.user_id == user_id)
            .order_by(Card.created_at.desc())
            .all()
        )

    @staticmethod
    def get_user_card(db: Session, user_id: int, card_id: int) -> Card:
        card = db.query(Card).filter(Card.id == card_id, Card.user_id == user_id).first()
        if card is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
        return card

    @staticmethod
    def get_public_card(db: Session, slug: str) -> Card:
        card = db.query(Card).filter(Card.public_slug == slug).first()
        if card is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
        return card

    @staticmethod
    def update_card(db: Session, user_id: int, card_id: int, data: CardUpdate) -> Card:
        card = CardService.get_user_card(db, user_id, card_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(card, field, value)
        db.commit()
        db.refresh(card)
        return card

    @staticmethod
    def delete_card(db: Session, user_id: int, card_id: int) -> None:
        card = CardService.get_user_card(db, user_id, card_id)
        db.delete(card)
        db.commit()
