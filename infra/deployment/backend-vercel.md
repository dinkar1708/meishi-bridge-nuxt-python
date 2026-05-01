# Backend Deployment (Vercel)

Deploys FastAPI to Vercel project `meishi-api`.

## Project Assignment

- Platform: Vercel
- Project: `meishi-api`
- Root Directory: `api`
- Runtime: Python (via `runtime.txt`)

## Required Files in `api/`

- `api/api/index.py` - FastAPI entrypoint for Vercel runtime
- `api/vercel.json` - rewrite all routes to `/api/index.py`
- `api/runtime.txt` - Python runtime pin (`python-3.12`)
- `api/.vercelignore` - trims deployment bundle

## Required Environment Variables (Backend Only)

```env
DATABASE_URL=<Neon pooled URL>
DATABASE_URL_UNPOOLED=<Neon unpooled URL>
SECRET_KEY=<strong-random-value>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080
FRONTEND_URL=https://meishi-bridge.vercel.app
```

Optional (if storage is enabled):

```env
SUPABASE_URL=<value>
SUPABASE_KEY=<value>
```

## Deploy Steps

1. Open Vercel project `meishi-api`
2. Confirm Root Directory is `api`
3. Add backend env vars
4. Deploy and verify health endpoints

## Verification

- `https://meishi-api.vercel.app/` returns status JSON
- `https://meishi-api.vercel.app/health` returns healthy JSON
- `https://meishi-api.vercel.app/docs` loads Swagger UI

## Security Note

All DB credentials live here. Never duplicate them into frontend project env vars.
