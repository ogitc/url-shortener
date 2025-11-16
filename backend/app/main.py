"""
Main FastAPI application.
"""
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from .deps import init_db
from .schemas import ShortenRequest, ShortenResponse
from .services import create_short_url, resolve_code


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="URL Shortener", version="1.0.0", lifespan=lifespan)

frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PUBLIC_BASE = os.getenv("PUBLIC_BASE", "http://localhost:8000")


@app.post("/api/shorten", response_model=ShortenResponse, status_code=201)
def shorten(payload: ShortenRequest):
    print(str(payload.url))
    row = create_short_url(str(payload.url))
    return ShortenResponse(short_url=f"{PUBLIC_BASE}/{row.short_code}", short_code=row.short_code)


@app.get("/{code}")
def redirect(code: str):
    long_url = resolve_code(code)
    if not long_url:
        raise HTTPException(status_code=404, detail="Not found")
    return RedirectResponse(long_url, status_code=302)
