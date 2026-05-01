# Deployment Guides

This folder is the source of truth for production deployment.

## Guides

- `frontend-vercel.md` - Frontend deploy (`meishi-bridge`, root `web`)
- `backend-vercel.md` - Backend deploy (`meishi-api`, root `api`)
- `database-neon.md` - Neon DB setup and environment variable assignment

## Ownership Rules (Must Follow)

1. Frontend Vercel project stores only public `NUXT_PUBLIC_*` variables.
2. Backend Vercel project stores all secrets (`DATABASE_URL`, `SECRET_KEY`, etc.).
3. Neon/Postgres credentials are backend-only and must never be added to frontend env vars.
