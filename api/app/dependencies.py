"""FastAPI dependencies for authentication and database."""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models.user import User
from app.schemas.auth import TokenData
from app.services.auth_service import AuthService

# OAuth2 scheme for bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> User:
    """Get current authenticated user from JWT token.

    Args:
        token: JWT access token
        db: Database session

    Returns:
        User: Current authenticated user

    Raises:
        HTTPException: If token is invalid or user not found
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode JWT token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id_str: str = payload.get("sub")

        if user_id_str is None:
            raise credentials_exception

        user_id = int(user_id_str)
        email: str = payload.get("email")

        token_data = TokenData(user_id=user_id, email=email)

    except (JWTError, ValueError):
        raise credentials_exception

    # Get user from database
    user = AuthService.get_user_by_id(db, user_id=token_data.user_id)

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive",
        )

    return user


def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    """Get current active user (alias for get_current_user).

    Args:
        current_user: Current authenticated user

    Returns:
        User: Current active user
    """
    return current_user
