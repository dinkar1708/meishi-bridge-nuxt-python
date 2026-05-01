"""Vercel serverless function entry point.

Vercel auto-detects files inside the `api/` directory at the project root
as Python serverless functions. This file imports the existing FastAPI
`app` so the same application powers both local uvicorn dev and Vercel.
"""
import sys
from pathlib import Path

# Make the parent directory (project root) importable so `from app.main import app` works.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from app.main import app  # noqa: E402, F401  (re-exported for Vercel)
