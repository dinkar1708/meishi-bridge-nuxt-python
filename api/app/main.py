"""
FastAPI Application Entry Point
"""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import auth, cards

app = FastAPI(
    title="MeishiBridge API",
    description="REST API for Japanese Business Card Management",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Build CORS origins list: always allow local dev ports plus the configured
# production frontend URL (e.g. https://meishi-bridge.vercel.app).
_default_origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
]

_extra_origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "").split(",")
    if origin.strip()
]

allow_origins = list(dict.fromkeys(_default_origins + [settings.FRONTEND_URL] + _extra_origins))

# Allow Vercel preview deployments (e.g. meishi-bridge-git-*.vercel.app).
allow_origin_regex = r"^https://meishi-bridge(-[a-z0-9-]+)?\.vercel\.app$"

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_origin_regex=allow_origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(cards.router)


@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - API health check"""
    return {
        "status": "ok",
        "message": "MeishiBridge API is running",
        "version": "0.1.0"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "meishibridge-api"
    }
