# Database Setup (Neon)

This project uses Neon Postgres for production data.

## Assignment

- Database provider: Neon
- Connected to: backend Vercel project `meishi-api`
- Not connected to: frontend Vercel project `meishi-bridge`

## Connection Strings

Use these Neon values:

- `DATABASE_URL` -> pooled connection string (app runtime)
- `DATABASE_URL_UNPOOLED` -> direct connection string (migrations/tools)

Both should include TLS requirements from Neon.

## Where to Set Variables

Set in backend Vercel project only:

```env
DATABASE_URL=<pooled>
DATABASE_URL_UNPOOLED=<unpooled>
```

Do not set these in frontend Vercel project.

## Migration Note

Use `DATABASE_URL_UNPOOLED` for migration commands when possible.

## Validation

1. Backend deploy is healthy
2. Auth endpoints can read/write users
3. Frontend can log in through backend API URL
