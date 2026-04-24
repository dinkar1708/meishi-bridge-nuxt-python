# API Backend - Python FastAPI

**MeishiBridge REST API**

High-performance async REST API built with Python FastAPI, PostgreSQL, and SQLAlchemy.

---

## Overview

The API backend provides:
- RESTful endpoints for all business logic
- JWT-based authentication
- Database operations (PostgreSQL)
- QR code generation
- PDF generation (Japanese meishi standard)
- File storage (Supabase)
- Automatic API documentation (Swagger/OpenAPI)

---

## Tech Stack

- **[Python 3.11](https://www.python.org/)** - Programming language
- **[FastAPI](https://fastapi.tiangolo.com/)** - Web framework
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation
- **[Alembic](https://alembic.sqlalchemy.org/)** - Database migrations
- **[PostgreSQL](https://www.postgresql.org/)** - Database
- **[python-jose](https://github.com/mpdavis/python-jose)** - JWT tokens
- **[passlib](https://passlib.readthedocs.io/)** - Password hashing
- **[ReportLab](https://www.reportlab.com/)** - PDF generation
- **[python-qrcode](https://github.com/lincolnloop/python-qrcode)** - QR codes
- **[Supabase Python](https://github.com/supabase-community/supabase-py)** - Storage client

---

## Project Structure (FastAPI Standard)

### **FastAPI uses "Routers" (not "Controllers")**

```
api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Settings (environment variables)
│   ├── database.py          # DB connection & session
│   │
│   ├── models/              # Database models (SQLAlchemy ORM)
│   │   ├── __init__.py
│   │   ├── user.py          # User table
│   │   ├── business_card.py # BusinessCard table
│   │   └── template.py      # Template table
│   │
│   ├── schemas/             # Request/Response schemas (Pydantic)
│   │   ├── __init__.py      # DTO (Data Transfer Objects)
│   │   ├── user.py          # UserCreate, UserResponse
│   │   ├── card.py          # CardCreate, CardResponse
│   │   ├── template.py      # TemplateResponse
│   │   └── auth.py          # LoginRequest, TokenResponse
│   │
│   ├── routers/             # API Routers (= Controllers in other frameworks)
│   │   ├── __init__.py
│   │   ├── auth.py          # POST /api/v1/auth/login, /register
│   │   ├── cards.py         # CRUD /api/v1/cards/*
│   │   ├── templates.py     # GET /api/v1/templates/*
│   │   └── users.py         # GET /api/v1/users/*
│   │
│   ├── services/            # Business logic (Service layer)
│   │   ├── __init__.py
│   │   ├── auth_service.py  # JWT, password hashing
│   │   ├── card_service.py  # Card CRUD logic
│   │   ├── pdf_generator.py # PDF generation
│   │   ├── qr_generator.py  # QR code generation
│   │   └── storage.py       # Supabase upload
│   │
│   ├── utils/               # Utility helpers
│   │   ├── __init__.py
│   │   ├── security.py      # Password hashing, JWT utils
│   │   └── helpers.py       # Common functions
│   │
│   └── dependencies.py      # FastAPI dependencies (auth, DB session)
│
├── alembic/                 # Database migrations (like Django migrations)
│   ├── versions/            # Migration files
│   └── env.py              # Alembic config
│
├── tests/                   # pytest tests
│   ├── __init__.py
│   ├── conftest.py         # Test fixtures
│   ├── test_auth.py        # Auth router tests
│   ├── test_cards.py       # Card router tests
│   ├── test_models.py      # Model tests
│   └── test_services.py    # Service layer tests
│
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker image
├── .env.example            # Environment template
└── README.md               # This file
```

### **FastAPI Architecture Explained:**

**1. Routers = Controllers** (Handle HTTP requests)
```python
# app/routers/cards.py
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/cards", tags=["cards"])

@router.post("/")  # POST /api/v1/cards/
async def create_card(card: CardCreate):
    return card_service.create(card)
```

**2. Services** (Business logic, separated from routers)
```python
# app/services/card_service.py
def create(card_data):
    # Business logic here
    # Generate QR, save to DB, etc.
    return created_card
```

**3. Models** (Database tables)
```python
# app/models/business_card.py
from sqlalchemy import Column, Integer, String

class BusinessCard(Base):
    __tablename__ = "business_cards"
    id = Column(Integer, primary_key=True)
    name_kanji = Column(String)
```

**4. Schemas** (Request/Response validation)
```python
# app/schemas/card.py
from pydantic import BaseModel

class CardCreate(BaseModel):  # Request DTO
    name_kanji: str
    company_kanji: str

class CardResponse(BaseModel):  # Response DTO
    id: int
    name_kanji: str
    created_at: datetime
```

### **Why This Structure is Standard:**

**Separation of Concerns** - Routers, Services, Models separate
**Testable** - Easy to test each layer independently
**Scalable** - Can add more routers/services easily
**FastAPI Best Practice** - Recommended by official docs

### **Comparison to Other Frameworks:**

| Layer | FastAPI | Spring Boot | Laravel |
|-------|---------|-------------|---------|
| **Routes** | `routers/` | `@Controller` | `routes/` |
| **Business Logic** | `services/` | `@Service` | `Services/` |
| **Database** | `models/` | `@Entity` | `Models/` |
| **Validation** | `schemas/` | `DTO` | `Requests/` |

---

## Getting Started

### **Prerequisites**
- Python 3.11 or higher
- PostgreSQL 15+ (or Docker)
- pip (Python package manager)

### **Installation**

```bash
# Navigate to api directory
cd api

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env

# Edit .env with your credentials
```

---

## Environment Configuration

The project supports **4 environments**:

| Environment | Purpose | Config File | Database |
|-------------|---------|-------------|----------|
| **local** | Local development | `.env.local` | `localhost:5432` |
| **dev** | Development deployment | `.env.dev` | Supabase Dev |
| **stg** | Staging/Testing | `.env.stg` | Supabase Staging |
| **prod** | Production (Client) | `.env.prod` | Supabase Production |

### **Setup Environment Files**

**`.env.local`** (Local development)
```env
# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/meishibridge

# Security
SECRET_KEY=dev-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# Supabase (for file storage)
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=your-dev-supabase-key

# CORS
FRONTEND_URL=http://localhost:3000
```

**`.env.dev`** (Development deployment)
```env
# Database
DATABASE_URL=postgresql://user:pass@db.supabase.co:5432/postgres

# Security
SECRET_KEY=dev-deployment-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# Supabase
SUPABASE_URL=https://xxx-dev.supabase.co
SUPABASE_KEY=your-dev-supabase-key

# CORS
FRONTEND_URL=https://meishibridge-dev.vercel.app
```

**`.env.stg`** (Staging deployment)
```env
# Database
DATABASE_URL=postgresql://user:pass@db-stg.supabase.co:5432/postgres

# Security
SECRET_KEY=staging-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# Supabase
SUPABASE_URL=https://xxx-stg.supabase.co
SUPABASE_KEY=your-stg-supabase-key

# CORS
FRONTEND_URL=https://meishibridge-stg.vercel.app
```

**`.env.prod`** (Production for clients)
```env
# Database
DATABASE_URL=postgresql://user:pass@db.supabase.co:5432/postgres

# Security
SECRET_KEY=<strong-production-secret-key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# Supabase
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=<prod-supabase-key>

# CORS
FRONTEND_URL=https://meishibridge.com
```

### **Run with Environment**

```bash
# Local development (uses .env.local automatically)
uvicorn app.main:app --reload

# Or specify environment file
export $(cat .env.dev | xargs) && uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### **Database Setup**

**Option 1: Docker PostgreSQL (Recommended)**
```bash
# Start PostgreSQL in Docker
docker run -d \
  --name meishibridge-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=meishibridge \
  -p 5432:5432 \
  postgres:15-alpine
```

**Option 2: Local PostgreSQL**
```bash
# Install PostgreSQL
# macOS: brew install postgresql@15
# Ubuntu: sudo apt install postgresql-15

# Create database
createdb meishibridge
```

### **Run Migrations**

```bash
# Run database migrations
alembic upgrade head
```

### **Start Development Server**

```bash
# Start FastAPI server with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# API running at: http://localhost:8000
# Swagger docs: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

---

## API Endpoints

### **Authentication**

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/v1/auth/register` | Register new user | No |
| POST | `/api/v1/auth/login` | Login user | No |
| GET | `/api/v1/auth/me` | Get current user | Yes |

### **Business Cards**

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/v1/cards/` | Get all user's cards | Yes |
| POST | `/api/v1/cards/` | Create new card | Yes |
| GET | `/api/v1/cards/{id}` | Get card by ID | Yes |
| PUT | `/api/v1/cards/{id}` | Update card | Yes |
| DELETE | `/api/v1/cards/{id}` | Delete card | Yes |
| GET | `/api/v1/cards/public/{card_url}` | Get public card | No |
| POST | `/api/v1/cards/{id}/generate-qr` | Generate QR code | Yes |
| POST | `/api/v1/cards/{id}/generate-pdf` | Generate PDF | Yes |

### **Templates**

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/v1/templates/` | Get all templates | No |
| GET | `/api/v1/templates/{id}` | Get template by ID | No |

---

## Testing & Code Coverage

### **Run Tests**

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_cards.py -v

# Run specific test function
pytest tests/test_auth.py::test_register_success -v

# Run tests in parallel (faster)
pytest -n auto
```

### **Code Coverage**

```bash
# Run tests with coverage report
pytest --cov=app --cov-report=html --cov-report=term

# Generate coverage report only
pytest --cov=app --cov-report=html

# View HTML coverage report
open htmlcov/index.html  # macOS
start htmlcov/index.html  # Windows

# Coverage with missing lines
pytest --cov=app --cov-report=term-missing
```

### **Coverage Goals**

| Module | Target Coverage | Priority |
|--------|----------------|----------|
| **Overall** | **90%+** | Critical |
| Models | 100% | High |
| API Endpoints | 95%+ | High |
| Services | 90%+ | Medium |
| Utils | 85%+ | Medium |

### **Test Case Examples**

**1. Authentication Tests** (`tests/test_auth.py`)
```python
def test_register_success():
    """Test successful user registration"""

def test_register_duplicate_email():
    """Test registration with existing email"""

def test_login_success():
    """Test successful login with correct credentials"""

def test_login_invalid_credentials():
    """Test login with wrong password"""

def test_get_current_user():
    """Test getting authenticated user profile"""
```

**2. Business Card Tests** (`tests/test_cards.py`)
```python
def test_create_card_success():
    """Test creating a new business card"""

def test_create_card_unauthorized():
    """Test creating card without authentication"""

def test_get_user_cards():
    """Test retrieving all cards for authenticated user"""

def test_update_card_success():
    """Test updating existing card"""

def test_delete_card_success():
    """Test deleting a card"""

def test_get_public_card():
    """Test accessing public card via URL"""
```

**3. QR & PDF Generation Tests** (`tests/test_services.py`)
```python
def test_generate_qr_code():
    """Test QR code generation for card"""

def test_generate_pdf_meishi():
    """Test PDF generation (91mm × 55mm)"""

def test_upload_to_storage():
    """Test file upload to Supabase storage"""
```

**4. Template Tests** (`tests/test_templates.py`)
```python
def test_get_all_templates():
    """Test retrieving all available templates"""

def test_get_template_by_id():
    """Test getting specific template"""
```

### **Test Structure**

```
tests/
├── conftest.py              # Fixtures and test configuration
├── test_auth.py             # Authentication endpoint tests
├── test_cards.py            # Business card CRUD tests
├── test_templates.py        # Template endpoint tests
├── test_models.py           # Database model tests
├── test_services.py         # Service layer tests
│   ├── test_qr_generator.py
│   ├── test_pdf_generator.py
│   └── test_storage.py
└── test_utils.py            # Utility function tests
```

### **Running Coverage Reports**

```bash
# Step 1: Run tests with coverage
pytest --cov=app --cov-report=html --cov-report=term-missing

# Step 2: View coverage summary in terminal
# Shows overall coverage percentage and missing lines

# Step 3: Open detailed HTML report
open htmlcov/index.html

# Step 4: Check coverage for specific module
pytest --cov=app.routers.cards --cov-report=term
```

### **CI/CD Coverage Check**

Add to `.github/workflows/api-ci.yml`:
```yaml
- name: Run tests with coverage
  run: |
    pytest --cov=app --cov-report=xml --cov-report=term

- name: Check coverage threshold
  run: |
    coverage report --fail-under=90
```

---

## Dependencies

### **Core**
```
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-dotenv==1.0.0
```

### **Database**
```
sqlalchemy==2.0.25
psycopg2-binary==2.9.9
alembic==1.13.1
```

### **Validation**
```
pydantic==2.5.3
pydantic-settings==2.1.0
```

### **Authentication**
```
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
```

### **Services**
```
pillow==10.2.0
reportlab==4.0.9
qrcode[pil]==7.4.2
supabase==2.3.1
```

### **Testing**
```
pytest==7.4.4
pytest-cov==4.1.0
httpx==0.26.0
```

---

## Database Models

### **User**
- id, email, username, hashed_password
- full_name, is_active, is_verified
- created_at, updated_at

### **BusinessCard**
- id, user_id (FK)
- name_kanji, furigana, name_english
- company_kanji, company_english
- title_japanese, title_english
- phone, email, website
- address_japanese, address_english
- linkedin, twitter, facebook
- template_id (FK), layout_type, is_public
- card_url (unique), qr_code_url, pdf_url
- view_count, created_at, updated_at

### **Template**
- id, name_ja, name_en
- description_ja, description_en
- category, thumbnail_url
- design_config (JSON), is_premium
- created_at

---

## Security

### **Authentication Flow**
1. User registers/logs in
2. Server generates JWT token
3. Client stores token
4. Client sends token in Authorization header
5. Server validates token on protected routes

### **Password Security**
- Passwords hashed with bcrypt
- Never stored in plain text
- Salt rounds: 12

### **CORS**
Configured to allow:
- Frontend URL from environment
- localhost:3000 (development)

---

## Deployment

### **Render (FREE)**

1. Connect GitHub repository
2. Create Web Service
3. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables
5. Deploy

**Keep-Alive (Prevent Cold Starts):**
Use [UptimeRobot](https://uptimerobot.com) to ping `/health` every 5 minutes

### **Other Options**
- Railway
- Fly.io
- AWS Lambda (serverless)
- DigitalOcean App Platform

---

## Development Tips

### **Database Migrations**

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback one version
alembic downgrade -1
```

### **Add New Endpoint**

1. Create route in `app/routers/`
2. Create schema in `app/schemas/`
3. Add business logic in `app/services/`
4. Write tests in `tests/`

### **Format Code**

```bash
# Install black (formatter)
pip install black

# Format code
black app/ tests/
```

---

## Performance

- Async/await for concurrent requests
- Database connection pooling
- Lazy loading relationships
- Response caching (future)

---

## Troubleshooting

### **Database Connection Error**
- Check PostgreSQL is running
- Verify DATABASE_URL in `.env`

### **Import Errors**
- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

### **Migration Errors**
- Check database connection
- Drop database and recreate if needed

---

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

---

## Contributing

See main [README](../README.md) for contribution guidelines.

---

**Built with FastAPI**
