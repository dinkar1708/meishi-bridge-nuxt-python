# Setup Guide - MeishiBridge API

Complete guide for setting up the FastAPI backend locally.

---

## Prerequisites

- **Docker & Docker Compose** (Recommended)
- **OR Python 3.11+** (Alternative)

---

## Method 1: Docker Setup (Recommended)

### Quick Start

```bash
# Navigate to API directory
cd api

# Copy environment template
cp .env.example .env.local

# Start all services (API + PostgreSQL)
docker compose up -d

# View logs
docker compose logs -f api
```

### Environment Variables

Create `.env.local` (gitignored) and follow `.env.example` for configuration.

**Important:** For Docker, use `db` as DATABASE_URL hostname (not `localhost`).

### Verify Installation

- **API Root:** http://localhost:8000
- **Swagger Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

### Common Commands

```bash
# Stop services
docker compose down

# Rebuild containers
docker compose up -d --build

# View running containers
docker compose ps

# Access container shell
docker compose exec api bash

# Run tests
docker compose exec api pytest
```

---

## Method 2: Virtual Environment Setup

### Quick Start

```bash
# Navigate to API directory
cd api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env.local

# Start PostgreSQL (Docker)
docker run -d \
  --name meishibridge-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=meishibridge \
  -p 5432:5432 \
  postgres:15-alpine

# Start development server
uvicorn app.main:app --reload
```

### Environment Variables

Create `.env.local` and follow `.env.example` for configuration.

**Important:** For venv, use `localhost` as DATABASE_URL hostname.

---

## Environment Configuration

| Environment | Config File | Database | Committed? |
|-------------|-------------|----------|------------|
| **local** | `.env.local` | localhost/Docker | No |
| **dev** | `.env.dev` | Supabase Dev | Yes |
| **stg** | `.env.stg` | Supabase Staging | Yes |
| **prod** | `.env.prod` | Supabase Production | Yes |

---

## Troubleshooting

### Port Already in Use

```bash
# Find and kill process using port 8000
lsof -i :8000
kill -9 <PID>
```

### Database Connection Error (Docker)

```bash
# Make sure DATABASE_URL uses 'db' as hostname (not 'localhost')
DATABASE_URL=postgresql://postgres:postgres@db:5432/meishibridge

# Restart services
docker compose down && docker compose up -d
```

### Check Logs

```bash
# Docker
docker compose logs api
docker compose logs db

# Virtual environment
# Check terminal output
```

---

## Next Steps

1. **Explore API Documentation:** http://localhost:8000/docs
2. **Read Architecture Guide:** [../architecture/](../architecture/)
3. **Start Development:** [../development/](../development/)
