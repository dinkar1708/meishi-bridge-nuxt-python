# Test Accounts

This document lists test accounts available for development and testing.

## Quick Start

### Create Test Accounts

Run the seed script to create test accounts:

```bash
# Using Docker
docker exec meishibridge-api python seeds/seed_users.py

# Or locally with venv
source venv/bin/activate
python seeds/seed_users.py
```

## Available Test Accounts

The following test accounts are created by the seed script:

### 1. Test User
- **Email**: `test@example.com`
- **Password**: `test123`
- **Username**: `testuser`
- **Full Name**: Test User
- **Use case**: General testing

### 2. Admin User
- **Email**: `admin@example.com`
- **Password**: `admin123`
- **Username**: `admin`
- **Full Name**: Admin User
- **Use case**: Admin functionality testing

### 3. Demo User
- **Email**: `demo@example.com`
- **Password**: `demo123`
- **Username**: `demouser`
- **Full Name**: Demo User
- **Use case**: Demo/presentation purposes

## Using Test Accounts

### Login via UI

1. Navigate to http://localhost:3000/login
2. Enter one of the test account emails and passwords
3. Click login

### Login via API

```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

## Notes

- Test accounts are created with `is_active=True` and `is_verified=False`
- Passwords are hashed using bcrypt
- The seed script is idempotent - running it multiple times won't create duplicates
- These accounts should only be used in development/staging environments
- Never use these credentials in production

## Resetting Test Accounts

To reset all test accounts:

```bash
# Drop and recreate database (Docker)
docker compose down -v
docker compose up -d

# Run seed script again
docker exec meishibridge-api python seeds/seed_users.py
```
