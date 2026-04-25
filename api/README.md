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
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM (Object-Relational Mapping)
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation
- **[Alembic](https://alembic.sqlalchemy.org/)** - Database migrations (version control for database schema)
- **[PostgreSQL](https://www.postgresql.org/)** - Database
- **[python-jose](https://github.com/mpdavis/python-jose)** - JWT tokens
- **[passlib](https://passlib.readthedocs.io/)** - Password hashing
- **[ReportLab](https://www.reportlab.com/)** - PDF generation
- **[python-qrcode](https://github.com/lincolnloop/python-qrcode)** - QR codes
- **[Supabase Python](https://github.com/supabase-community/supabase-py)** - Storage client

---

## VS Code Setup (Recommended)

### **Install Required Extensions**

For the best FastAPI development experience in VS Code, install these official extensions:

#### **1. Python Extension (Official - Required)**

```bash
# Install via command line
code --install-extension ms-python.python

# Or in VS Code:
# Press Cmd+Shift+X (Mac) or Ctrl+Shift+X (Windows/Linux)
# Search for "Python"
# Install "Python" by Microsoft
```

**Features:**
- IntelliSense (autocomplete)
- Linting (code quality checks)
- Debugging
- Code formatting
- Virtual environment support

#### **2. FastAPI Extension (Official - Highly Recommended)**

```bash
# Install via command line
code --install-extension FastAPILabs.fastapi-vscode

# Or in VS Code:
# Press Cmd+Shift+X (Mac) or Ctrl+Shift+X (Windows/Linux)
# Search for "FastAPI"
# Install "FastAPI" by FastAPILabs
```

**Features:**
- Route explorer (tree view of all endpoints)
- Quick navigation to route definitions
- Search FastAPI routes
- FastAPI Cloud integration
- Better autocomplete for FastAPI code

#### **3. Additional Helpful Extensions (Optional)**

```bash
# Pylance - Enhanced Python language support
code --install-extension ms-python.vscode-pylance

# Python Debugger
code --install-extension ms-python.debugpy

# Better TOML support (for pyproject.toml)
code --install-extension tamasfe.even-better-toml
```

### **VS Code Settings for This Project**

Create `.vscode/settings.json` in your project root:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/api/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [
    "tests"
  ],
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

### **Verify Installation**

1. Open VS Code in the `api` directory: `code .`
2. Check bottom-left corner for Python version
3. Open Command Palette (Cmd/Ctrl+Shift+P)
4. Type "FastAPI" - you should see FastAPI-related commands
5. Look for "FastAPI Routes" panel in the sidebar

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

## How This Project Was Created

### **Method 1: Manual Creation (What We Did)**

FastAPI doesn't have an official CLI like Django's `startproject`, so we created the structure manually:

```bash
# Navigate to api directory
cd api

# Create app directory and files
mkdir -p app
touch app/__init__.py
touch app/main.py
touch app/config.py

# Create requirements.txt
touch requirements.txt

# Create environment template
touch .env.example
```

Then we populated each file with the basic FastAPI setup code.

### **Method 2: Using Cookiecutter (Alternative)**

You can also use a project template generator:

```bash
# Install cookiecutter
pip install cookiecutter

# Generate FastAPI project from template
cookiecutter https://github.com/tiangolo/full-stack-fastapi-postgresql
```

### **Method 3: Using FastAPI CLI (Unofficial)**

```bash
# Install fastapi-cli
pip install fastapi-cli

# Create new project (basic structure)
fastapi new my-project
```

### **What We Created**

**Current Project Structure:**
```
api/
├── app/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # FastAPI app with health endpoints
│   └── config.py            # Pydantic settings configuration
├── docs/
│   ├── README.md           # Documentation index
│   └── SETUP.md            # Complete setup guide
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This documentation
```

**Files Created:**

1. **`app/__init__.py`** - Package marker with version
2. **`app/main.py`** - FastAPI application with:
   - Health check endpoints (`/` and `/health`)
   - CORS middleware configured
   - Auto-generated API docs at `/docs`
3. **`app/config.py`** - Configuration using Pydantic Settings
4. **`requirements.txt`** - All project dependencies
5. **`.env.example`** - Environment variable template
6. **`docs/`** - Documentation folder
   - `README.md` - Documentation index
   - `SETUP.md` - Complete setup guide

---

## Getting Started

### **Quick Start (Docker - Recommended)**

```bash
cd api
cp .env.example .env.local
docker compose up -d
```

**Important:** Use `db` as DATABASE_URL hostname in `.env.local`

### **Quick Start (Virtual Environment)**

```bash
cd api
python -m venv venv
source venv/bin/activate              # macOS/Linux (Windows: venv\Scripts\activate)
pip install -r requirements.txt
cp .env.example .env.local

# Start PostgreSQL container
docker run -d --name meishibridge-db \
  -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=meishibridge -p 5432:5432 postgres:15-alpine

# Start server
uvicorn app.main:app --reload
```

**Important:** Use `localhost` as DATABASE_URL hostname in `.env.local`

### **Verify Installation**

Visit:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

### **Detailed Setup Guide**

For complete setup instructions including:
- Prerequisites and installation
- Environment configuration (local/dev/stg/prod)
- Database setup (Docker/Local PostgreSQL)
- Database migrations
- Troubleshooting

See: **[docs/setup/installation.md](docs/setup/installation.md)**

### **Full Documentation**

Complete documentation organized by topic:
- **[docs/](docs/)** - Documentation index
- **[docs/setup/](docs/setup/)** - Installation and configuration
- **[docs/testing/](docs/testing/)** - Testing guide (Docker method)
- **[docs/database/](docs/database/)** - Database migrations
- **[docs/development/](docs/development/)** - Development guides
- **[docs/api-reference/](docs/api-reference/)** - API endpoints
- **[docs/architecture/](docs/architecture/)** - System architecture
- **[docs/guides/](docs/guides/)** - How-to tutorials
- **[/infra/](../infra/)** - Deployment & infrastructure (separate folder)

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

### **Run Tests (Docker Method - Recommended)**

```bash
# Run all tests
docker compose exec api pytest

# Run with verbose output
docker compose exec api pytest -v

# Run with coverage report
docker compose exec api pytest --cov=app --cov-report=term-missing

# Run specific test file
docker compose exec api pytest tests/test_auth.py -v

# Run specific test function
docker compose exec api pytest tests/test_auth.py::TestUserLogin::test_login_success
```

### **Quick Test Commands**

```bash
# Run all tests
docker compose exec api pytest

# Run with detailed coverage
docker compose exec api pytest --cov=app --cov-report=html

# View HTML coverage report
open htmlcov/index.html  # macOS
```

### **Detailed Testing Guide**

For complete testing documentation including:
- All test commands (filtering, coverage, debugging)
- Test structure and organization
- Writing tests and best practices
- Using fixtures and test data
- CI/CD integration

See: **[docs/testing/README.md](docs/testing/README.md)**

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

**Alembic** is a database migration tool for SQLAlchemy. It tracks and manages changes to your database schema over time (like Git for databases).

**Why use Alembic?**
- Version control for database schema
- Auto-generate migrations from model changes
- Easy rollback to previous versions
- Team collaboration on database changes

```bash
# Create new migration (auto-detects model changes)
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback one version
alembic downgrade -1

# Check current version
alembic current
```

**See detailed guide:** [docs/database/migrations.md](docs/database/migrations.md)

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
