"""Authentication router for user registration and login."""

from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.auth import LoginRequest, Token
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/api/v1/auth", tags=["authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
    user_data: UserCreate,
    db: Annotated[Session, Depends(get_db)],
):
    """Register a new user.

    Args:
        user_data: User registration data
        db: Database session

    Returns:
        UserResponse: Created user data

    Raises:
        HTTPException 400: If email or username already exists
    """
    return AuthService.register_user(db, user_data)


@router.post("/login", response_model=Token)
def login(
    login_data: LoginRequest,
    db: Annotated[Session, Depends(get_db)],
):
    """Login and get JWT access token.

    Args:
        login_data: Login credentials
        db: Database session

    Returns:
        Token: JWT access token

    Raises:
        HTTPException 401: If credentials are invalid
        HTTPException 403: If account is inactive
    """
    return AuthService.login_user(db, login_data)


@router.get("/me", response_model=UserResponse)
def get_current_user_profile(
    current_user: Annotated[User, Depends(get_current_user)],
):
    """Get current authenticated user profile.

    Args:
        current_user: Current authenticated user

    Returns:
        UserResponse: Current user data
    """
    return UserResponse.model_validate(current_user)
