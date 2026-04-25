# Database Seeds

This folder contains database seeding scripts for development and testing.

## Available Seeds

### User Seeds (`seed_users.py`)

Creates test user accounts for development/testing.

**Run:**
```bash
# Using Docker
docker exec meishibridge-api python seeds/seed_users.py

# Or locally
source venv/bin/activate
python seeds/seed_users.py
```

**Creates:**
- test@example.com / test123 (testuser)
- admin@example.com / admin123 (admin)
- demo@example.com / demo123 (demouser)

## Adding New Seeds

1. Create a new file: `seed_[entity].py`
2. Follow the pattern in `seed_users.py`
3. Make it idempotent (safe to run multiple times)
4. Update this README

## Notes

- Seeds are for development/testing only
- Never run seeds in production
- All seed scripts should be idempotent
- Check for existing data before creating
