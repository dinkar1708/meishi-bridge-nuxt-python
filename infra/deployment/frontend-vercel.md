# Frontend Deployment (Vercel)

Deploys the Nuxt app to Vercel project `meishi-bridge`.

## Project Assignment

- Platform: Vercel
- Project: `meishi-bridge`
- Root Directory: `web`
- Framework: `Nuxt.js` (or `Other` with manual commands)

## Required Build Settings

- Install Command: `npm install`
- Build Command: `npm run build`

## Required Environment Variables

```env
NUXT_PUBLIC_API_URL=https://meishi-api.vercel.app/api/v1
NUXT_PUBLIC_APP_URL=https://meishi-bridge.vercel.app
```

## Deploy Steps

1. Open Vercel project `meishi-bridge`
2. Confirm Root Directory is `web`
3. Confirm framework/build settings above
4. Add/update required env vars
5. Redeploy

## Verification

- Frontend loads at `https://meishi-bridge.vercel.app`
- Login/register requests go to `https://meishi-api.vercel.app/api/v1/*`
- No frontend request points to `localhost` in production

## Security Note

Do not store `DATABASE_URL` or any private secret in this frontend project.
