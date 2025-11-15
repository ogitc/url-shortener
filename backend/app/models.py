"""
Using SQLModel to define the database models.
"""
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class UrlMap(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    short_code: str = Field(index=True, unique=True, max_length=16)
    long_url: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
