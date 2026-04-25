# Service Layer Organization - Best Practices

Guide for organizing the services layer as your FastAPI application grows.

---

## Current Structure (Small Project)

```
app/
├── services/
│   ├── __init__.py
│   └── auth_service.py
```

**When to use:** Projects with 1-10 services

**Pros:**
- Simple and flat
- Easy to navigate
- No complexity

**Cons:**
- Hard to scale beyond 10 services
- No logical grouping
- Services become cluttered

---

## Evolution Path: How Services Grow

### **Stage 1: Flat Structure (Current - 1-10 services)**

```
app/
├── services/
│   ├── __init__.py
│   ├── auth_service.py          # Authentication logic
│   ├── card_service.py          # Business card CRUD
│   ├── qr_service.py            # QR code generation
│   ├── pdf_service.py           # PDF generation
│   ├── storage_service.py       # File upload/storage
│   └── template_service.py      # Template management
```

**Use when:** You have fewer than 10 service files

---

### **Stage 2: Domain-Driven Structure (10-30 services)**

Group services by **business domain** (feature area):

```
app/
├── services/
│   ├── __init__.py
│   │
│   ├── auth/                    # Authentication domain
│   │   ├── __init__.py
│   │   ├── auth_service.py     # Login, register, JWT
│   │   ├── password_service.py # Password reset, change
│   │   └── session_service.py  # Session management
│   │
│   ├── cards/                   # Business cards domain
│   │   ├── __init__.py
│   │   ├── card_service.py     # CRUD operations
│   │   ├── card_validator.py   # Card validation logic
│   │   └── card_sharing.py     # Sharing & privacy
│   │
│   ├── generation/              # Content generation domain
│   │   ├── __init__.py
│   │   ├── qr_service.py       # QR code generation
│   │   ├── pdf_service.py      # PDF generation
│   │   └── image_service.py    # Image processing
│   │
│   ├── storage/                 # Storage domain
│   │   ├── __init__.py
│   │   ├── file_service.py     # File operations
│   │   ├── supabase_service.py # Supabase client
│   │   └── cdn_service.py      # CDN management
│   │
│   └── templates/               # Templates domain
│       ├── __init__.py
│       ├── template_service.py # Template CRUD
│       └── layout_service.py   # Layout management
```

**Use when:** You have 10-30 services and clear domain boundaries

**Benefits:**
- Logical grouping by business domain
- Easy to find related services
- Clear separation of concerns
- Better for team collaboration

---

### **Stage 3: Layered Architecture (30+ services)**

Add **sub-layers** within services for complex business logic:

```
app/
├── services/
│   ├── __init__.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── service.py          # Public API (main service)
│   │   ├── repository.py       # Database operations
│   │   ├── validator.py        # Business validation
│   │   └── helpers.py          # Helper functions
│   │
│   ├── cards/
│   │   ├── __init__.py
│   │   ├── service.py          # Main business logic
│   │   ├── repository.py       # Database layer
│   │   ├── cache.py            # Caching layer
│   │   ├── validator.py        # Validation rules
│   │   └── transformers.py     # Data transformation
│   │
│   └── notifications/
│       ├── __init__.py
│       ├── service.py          # Notification orchestration
│       ├── email_provider.py   # Email sending
│       ├── sms_provider.py     # SMS sending
│       └── queue.py            # Queue management
```

**Use when:** You have 30+ services or very complex business logic

**Layers explained:**

1. **`service.py`** - Main service (public API)
   - Orchestrates business logic
   - Called by routers
   - High-level operations

2. **`repository.py`** - Database layer
   - All database queries
   - CRUD operations
   - Query optimization

3. **`validator.py`** - Business validation
   - Complex validation rules
   - Business rule checks
   - Data integrity

4. **`cache.py`** - Caching layer
   - Redis/memcached operations
   - Cache invalidation
   - Performance optimization

5. **`helpers.py`** - Utilities
   - Common helper functions
   - Formatting, parsing
   - Non-business logic

---

## Best Practice Examples

### **Example 1: Simple Service (Stage 1)**

```python
# app/services/card_service.py
"""Business card service - all operations in one file."""

from sqlalchemy.orm import Session
from app.models.card import BusinessCard
from app.schemas.card import CardCreate, CardUpdate

class CardService:
    """Handle all business card operations."""

    @staticmethod
    def create(db: Session, user_id: int, card_data: CardCreate):
        """Create new business card."""
        card = BusinessCard(**card_data.dict(), user_id=user_id)
        db.add(card)
        db.commit()
        db.refresh(card)
        return card

    @staticmethod
    def get_all(db: Session, user_id: int):
        """Get all cards for user."""
        return db.query(BusinessCard).filter(
            BusinessCard.user_id == user_id
        ).all()

    @staticmethod
    def delete(db: Session, card_id: int, user_id: int):
        """Delete business card."""
        card = db.query(BusinessCard).filter(
            BusinessCard.id == card_id,
            BusinessCard.user_id == user_id
        ).first()
        if card:
            db.delete(card)
            db.commit()
        return card
```

---

### **Example 2: Domain-Driven Service (Stage 2)**

```python
# app/services/cards/card_service.py
"""Main card service - orchestrates card operations."""

from sqlalchemy.orm import Session
from app.schemas.card import CardCreate
from .card_validator import CardValidator
from .card_sharing import CardSharingService

class CardService:
    """Main business card service."""

    @staticmethod
    def create(db: Session, user_id: int, card_data: CardCreate):
        """Create new business card with validation."""
        # Validate card data
        CardValidator.validate_create(card_data)

        # Create card
        card = BusinessCard(**card_data.dict(), user_id=user_id)
        db.add(card)
        db.commit()
        db.refresh(card)

        # Generate sharing URL
        CardSharingService.generate_url(db, card)

        return card
```

```python
# app/services/cards/card_validator.py
"""Card validation logic."""

from fastapi import HTTPException
from app.schemas.card import CardCreate

class CardValidator:
    """Validate business card data."""

    @staticmethod
    def validate_create(card_data: CardCreate):
        """Validate card creation data."""
        # Validate email format
        if card_data.email and not "@" in card_data.email:
            raise HTTPException(400, "Invalid email format")

        # Validate phone number
        if card_data.phone and len(card_data.phone) < 10:
            raise HTTPException(400, "Invalid phone number")

        # Validate required kanji fields
        if not card_data.name_kanji:
            raise HTTPException(400, "Name in kanji is required")
```

```python
# app/services/cards/card_sharing.py
"""Card sharing and privacy logic."""

import secrets
from sqlalchemy.orm import Session
from app.models.card import BusinessCard

class CardSharingService:
    """Handle card sharing and privacy."""

    @staticmethod
    def generate_url(db: Session, card: BusinessCard):
        """Generate unique sharing URL."""
        card.card_url = secrets.token_urlsafe(16)
        db.commit()
        return card.card_url

    @staticmethod
    def toggle_public(db: Session, card_id: int, is_public: bool):
        """Toggle card public/private status."""
        card = db.query(BusinessCard).filter_by(id=card_id).first()
        if card:
            card.is_public = is_public
            db.commit()
        return card
```

**Directory structure:**
```python
# app/services/cards/__init__.py
"""Card services package."""

from .card_service import CardService
from .card_validator import CardValidator
from .card_sharing import CardSharingService

__all__ = ["CardService", "CardValidator", "CardSharingService"]
```

---

### **Example 3: Layered Architecture (Stage 3)**

```python
# app/services/cards/service.py
"""Main card service - orchestrates all operations."""

from sqlalchemy.orm import Session
from app.schemas.card import CardCreate
from .repository import CardRepository
from .validator import CardValidator
from .cache import CardCache
from ..generation.qr_service import QRService

class CardService:
    """High-level card operations."""

    @staticmethod
    def create(db: Session, user_id: int, card_data: CardCreate):
        """Create business card with full workflow."""
        # Step 1: Validate
        CardValidator.validate_create(card_data)

        # Step 2: Create in database
        card = CardRepository.create(db, user_id, card_data)

        # Step 3: Generate QR code
        qr_url = QRService.generate(card)
        CardRepository.update_qr_url(db, card.id, qr_url)

        # Step 4: Cache the card
        CardCache.set(card.id, card)

        return card

    @staticmethod
    def get_by_id(db: Session, card_id: int, user_id: int):
        """Get card by ID with caching."""
        # Try cache first
        cached = CardCache.get(card_id)
        if cached:
            return cached

        # Fetch from database
        card = CardRepository.get_by_id(db, card_id, user_id)

        # Cache for next time
        if card:
            CardCache.set(card_id, card)

        return card
```

```python
# app/services/cards/repository.py
"""Database operations for cards."""

from sqlalchemy.orm import Session
from app.models.card import BusinessCard
from app.schemas.card import CardCreate

class CardRepository:
    """Database layer for business cards."""

    @staticmethod
    def create(db: Session, user_id: int, card_data: CardCreate):
        """Insert card into database."""
        card = BusinessCard(**card_data.dict(), user_id=user_id)
        db.add(card)
        db.commit()
        db.refresh(card)
        return card

    @staticmethod
    def get_by_id(db: Session, card_id: int, user_id: int):
        """Fetch card by ID."""
        return db.query(BusinessCard).filter(
            BusinessCard.id == card_id,
            BusinessCard.user_id == user_id
        ).first()

    @staticmethod
    def update_qr_url(db: Session, card_id: int, qr_url: str):
        """Update QR code URL."""
        card = db.query(BusinessCard).filter_by(id=card_id).first()
        if card:
            card.qr_code_url = qr_url
            db.commit()
        return card

    @staticmethod
    def get_all_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
        """Get all cards for user with pagination."""
        return db.query(BusinessCard).filter(
            BusinessCard.user_id == user_id
        ).offset(skip).limit(limit).all()
```

```python
# app/services/cards/validator.py
"""Business validation rules for cards."""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.card import CardCreate, CardUpdate
from .repository import CardRepository

class CardValidator:
    """Card validation logic."""

    @staticmethod
    def validate_create(card_data: CardCreate):
        """Validate card creation."""
        # Required fields
        if not card_data.name_kanji:
            raise HTTPException(400, "Name in kanji is required")

        if not card_data.company_kanji:
            raise HTTPException(400, "Company in kanji is required")

        # Email format
        if card_data.email and "@" not in card_data.email:
            raise HTTPException(400, "Invalid email format")

        # Phone validation
        if card_data.phone:
            phone = card_data.phone.replace("-", "").replace(" ", "")
            if not phone.isdigit() or len(phone) < 10:
                raise HTTPException(400, "Invalid phone number")

    @staticmethod
    def validate_update(card_data: CardUpdate):
        """Validate card update."""
        # Similar validation rules for updates
        pass

    @staticmethod
    def validate_ownership(db: Session, card_id: int, user_id: int):
        """Verify user owns the card."""
        card = CardRepository.get_by_id(db, card_id, user_id)
        if not card:
            raise HTTPException(404, "Card not found")
        return card
```

```python
# app/services/cards/cache.py
"""Caching layer for cards."""

import json
from typing import Optional
from app.models.card import BusinessCard

# Simple in-memory cache (replace with Redis in production)
_cache = {}

class CardCache:
    """Card caching operations."""

    @staticmethod
    def get(card_id: int) -> Optional[dict]:
        """Get card from cache."""
        return _cache.get(f"card:{card_id}")

    @staticmethod
    def set(card_id: int, card: BusinessCard, ttl: int = 300):
        """Cache card for TTL seconds."""
        # Convert SQLAlchemy model to dict
        card_dict = {
            "id": card.id,
            "name_kanji": card.name_kanji,
            "company_kanji": card.company_kanji,
            # ... other fields
        }
        _cache[f"card:{card_id}"] = card_dict

    @staticmethod
    def delete(card_id: int):
        """Remove card from cache."""
        key = f"card:{card_id}"
        if key in _cache:
            del _cache[key]

    @staticmethod
    def clear_user_cache(user_id: int):
        """Clear all cached cards for user."""
        # In production with Redis:
        # redis.delete_pattern(f"card:user:{user_id}:*")
        pass
```

---

## Recommended Structure for MeishiBridge

Based on your project scope, I recommend **Stage 2: Domain-Driven Structure**:

```
app/
├── services/
│   ├── __init__.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── auth_service.py
│   │
│   ├── cards/
│   │   ├── __init__.py
│   │   ├── card_service.py      # CRUD operations
│   │   ├── card_validator.py    # Validation logic
│   │   └── card_sharing.py      # Public sharing
│   │
│   ├── generation/
│   │   ├── __init__.py
│   │   ├── qr_service.py        # QR code generation
│   │   └── pdf_service.py       # PDF generation
│   │
│   ├── storage/
│   │   ├── __init__.py
│   │   └── supabase_service.py  # File storage
│   │
│   └── templates/
│       ├── __init__.py
│       └── template_service.py  # Template management
```

**Why this structure?**
- Clear business domains (auth, cards, generation, storage, templates)
- Room to grow within each domain
- Not over-engineered (no need for repository pattern yet)
- Easy to understand and maintain

---

## Migration Guide: Flat -> Domain-Driven

### **Step 1: Create domain folders**

```bash
mkdir -p app/services/auth
mkdir -p app/services/cards
mkdir -p app/services/generation
mkdir -p app/services/storage
mkdir -p app/services/templates
```

### **Step 2: Move existing services**

```bash
# Move auth service
mv app/services/auth_service.py app/services/auth/auth_service.py

# Create __init__.py files
touch app/services/auth/__init__.py
touch app/services/cards/__init__.py
# ... etc
```

### **Step 3: Update imports in __init__.py**

```python
# app/services/auth/__init__.py
"""Authentication services."""

from .auth_service import AuthService

__all__ = ["AuthService"]
```

### **Step 4: Update imports in routers**

**Before:**
```python
from app.services.auth_service import AuthService
```

**After:**
```python
from app.services.auth import AuthService
```

### **Step 5: Update main services __init__.py**

```python
# app/services/__init__.py
"""Services package."""

from .auth import AuthService

__all__ = ["AuthService"]
```

---

## When to Use Each Pattern

| Pattern | Services | Complexity | Team Size | Example Projects |
|---------|----------|------------|-----------|------------------|
| **Flat** | 1-10 | Low | 1-2 | MVP, Prototype, Small API |
| **Domain-Driven** | 10-30 | Medium | 2-5 | MeishiBridge, E-commerce API |
| **Layered** | 30+ | High | 5+ | Enterprise, Large SaaS |

---

## Anti-Patterns to Avoid

###  **Don't: Over-engineer early**

```python
# TOO COMPLEX for a simple service
app/services/auth/domain/entities/user_entity.py
app/services/auth/domain/repositories/user_repository_interface.py
app/services/auth/infrastructure/repositories/user_repository_impl.py
app/services/auth/application/use_cases/login_use_case.py
```

###  **Do: Start simple, evolve as needed**

```python
# GOOD: Simple and clear
app/services/auth/auth_service.py
```

---

###  **Don't: Mix database operations in routers**

```python
# BAD: Router doing database queries
@router.post("/cards")
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    new_card = BusinessCard(**card.dict())
    db.add(new_card)
    db.commit()
    return new_card
```

###  **Do: Use service layer**

```python
# GOOD: Router delegates to service
@router.post("/cards")
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    return CardService.create(db, card)
```

---

## Summary: Recommended Approach

**For MeishiBridge (current stage):**

1. **Now:** Use **Domain-Driven Structure** (Stage 2)
2. **Start with:** `auth/`, `cards/`, `generation/`, `storage/`, `templates/`
3. **Add layers later:** Only when you have 30+ services or complex caching/validation needs
4. **Keep it simple:** Don't over-engineer until you need it

**Evolution path:**
- 1-10 services -> Flat structure  (You're here)
- 10-30 services -> Domain-driven  (Move here soon)
- 30+ services -> Layered architecture (Future)

---

## References

- [Clean Architecture by Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Domain-Driven Design by Eric Evans](https://martinfowler.com/bliki/DomainDrivenDesign.html)
- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
