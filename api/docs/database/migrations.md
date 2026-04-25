# Database Migrations Guide

Guide for managing database schema changes using Alembic.

## Prerequisites

- Alembic installed (`pip install alembic`)
- Database connection configured in `.env.local`

## Initial Setup

Alembic has been initialized in this project. If you need to initialize it in a new project:

```bash
cd api
alembic init alembic
```

## Configuration

The `alembic/env.py` file is configured to:
- Read `DATABASE_URL` from `app.config.settings`
- Import all models from `app.models`
- Use `Base.metadata` for autogenerate support

## Common Commands

### Create a New Migration

```bash
# Auto-generate migration from model changes
alembic revision --autogenerate -m "Description of changes"

# Create empty migration file (manual)
alembic revision -m "Description of changes"
```

### Apply Migrations

```bash
# Apply all pending migrations
alembic upgrade head

# Apply specific number of migrations
alembic upgrade +1

# Apply to specific revision
alembic upgrade <revision_id>
```

### Rollback Migrations

```bash
# Rollback one migration
alembic downgrade -1

# Rollback to specific revision
alembic downgrade <revision_id>

# Rollback all migrations
alembic downgrade base
```

### View Migration History

```bash
# Show current revision
alembic current

# Show migration history
alembic history

# Show pending migrations
alembic history --verbose
```

## Docker Commands

### Run Migrations in Docker Container

```bash
# Apply migrations
docker compose exec api alembic upgrade head

# Create new migration
docker compose exec api alembic revision --autogenerate -m "Description"

# View current migration status
docker compose exec api alembic current
```

## Best Practices

1. **Always review auto-generated migrations** before applying
2. **Test migrations** on development database first
3. **Create migrations atomically** - one logical change per migration
4. **Never edit applied migrations** - create a new migration instead
5. **Commit migrations** to version control

## Migration File Structure

```python
"""Create users table

Revision ID: a1211d1e7e30
Revises:
Create Date: 2026-04-25
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = 'a1211d1e7e30'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Schema changes to apply
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        # ... more columns
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    # Schema changes to rollback
    op.drop_table('users')
```

## Troubleshooting

### Database Does Not Exist

Create the database first:
```bash
# Using psql
createdb -U postgres meishibridge

# Or using SQL
psql -U postgres -c "CREATE DATABASE meishibridge;"

# In Docker
docker exec meishibridge-db psql -U postgres -c "CREATE DATABASE meishibridge;"
```

### Connection Issues (Docker)

Ensure `.env.local` uses correct hostname:
- **Docker**: `DATABASE_URL=postgresql://postgres:postgres@db:5432/meishibridge`
- **Virtual Env**: `DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:5432/meishibridge`

### Migration Conflicts

If multiple developers create migrations simultaneously:
```bash
# Merge migrations
alembic merge <rev1> <rev2> -m "Merge migrations"
alembic upgrade head
```

## Current Migrations

### a1211d1e7e30 - Create users table
- Creates `users` table with authentication fields
- Indexes on `email`, `username`, `id`
- Timestamps for `created_at` and `updated_at`
