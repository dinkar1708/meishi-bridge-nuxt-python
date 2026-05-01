"""Authentication service layer for user registration and login."""

from datetime import timedelta
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import LoginRequest, Token
from app.schemas.user import UserCreate, UserResponse
from app.utils.security import create_access_token, get_password_hash, verify_password
from app.config import settings


class AuthService:
    """Service class for authentication operations."""

    @staticmethod
    def register_user(db: Session, user_data: UserCreate) -> UserResponse:
        """Register a new user.

        Args:
            db: Database session
            user_data: User registration data

        Returns:
            UserResponse: Created user data

        Raises:
            HTTPException: If email or username already exists
        """
        try:
            # Check if email already exists
            existing_email = db.query(User).filter(User.email == user_data.email).first()
            if existing_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered",
                )

            # Check if username already exists
            existing_username = db.query(User).filter(User.username == user_data.username).first()
            if existing_username:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already taken",
                )

            # Create new user
            hashed_password = get_password_hash(user_data.password)
            db_user = User(
                email=user_data.email,
                username=user_data.username,
                hashed_password=hashed_password,
                full_name=user_data.full_name,
            )

            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        except HTTPException:
            db.rollback()
            raise
        except IntegrityError:
            db.rollback()
            # Covers edge cases where a concurrent request inserts the same
            # email/username between uniqueness check and commit.
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email or username already exists",
            )
        except SQLAlchemyError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Registration failed due to a database error",
            )
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Registration failed",
            )

        return UserResponse.model_validate(db_user)

    @staticmethod
    def login_user(db: Session, login_data: LoginRequest) -> Token:
        """Authenticate user and return JWT token.

        Args:
            db: Database session
            login_data: Login credentials

        Returns:
            Token: JWT access token

        Raises:
            HTTPException: If credentials are invalid
        """
        # Find user by email
        user = db.query(User).filter(User.email == login_data.email).first()

        # Verify user exists and password is correct
        if not user or not verify_password(login_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Check if user is active
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive",
            )

        # Create access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(user.id), "email": user.email},
            expires_delta=access_token_expires,
        )

        return Token(access_token=access_token, token_type="bearer")

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID.

        Args:
            db: Database session
            user_id: User ID

        Returns:
            Optional[User]: User object or None
        """
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email.

        Args:
            db: Database session
            email: User email

        Returns:
            Optional[User]: User object or None
        """
        return db.query(User).filter(User.email == email).first()
