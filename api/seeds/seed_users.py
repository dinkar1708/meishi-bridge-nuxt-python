"""Database seeding script for test accounts.

Run this script to create test accounts in the database:
    python seeds/seed_users.py

Test accounts will be created with known credentials for development/testing.
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import app modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app.models.user import User, Base
from app.services.auth_service import AuthService
from app.schemas.user import UserCreate


def create_test_accounts(db: Session):
    """Create test accounts for development."""

    test_users = [
        {
            "email": "test@example.com",
            "username": "testuser",
            "password": "test123",
            "full_name": "Test User"
        },
        {
            "email": "admin@example.com",
            "username": "admin",
            "password": "admin123",
            "full_name": "Admin User"
        },
        {
            "email": "demo@example.com",
            "username": "demouser",
            "password": "demo123",
            "full_name": "Demo User"
        }
    ]

    print("Creating test accounts...")
    print("-" * 50)

    for user_data in test_users:
        # Check if user already exists
        existing_user = db.query(User).filter(
            (User.email == user_data["email"]) |
            (User.username == user_data["username"])
        ).first()

        if existing_user:
            print(f"✓ User already exists: {user_data['email']}")
            continue

        # Create new user
        try:
            user_create = UserCreate(**user_data)
            AuthService.register_user(db, user_create)
            print(f"✓ Created user: {user_data['email']} (password: {user_data['password']})")
        except Exception as e:
            print(f"✗ Failed to create {user_data['email']}: {str(e)}")

    print("-" * 50)
    print("Seeding complete!")


def main():
    """Main function to run seeding."""
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # Create database session
    db = SessionLocal()

    try:
        create_test_accounts(db)
        db.commit()
    except Exception as e:
        print(f"Error during seeding: {str(e)}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
