"""
Services for the URL shortener:
- create_short_url: Create a new short URL
- resolve_code: Resolve a short code to a long URL
"""
from sqlmodel import select
from .models import UrlMap
from .short_code import generate_short_code
from .deps import get_session
from sqlalchemy.exc import IntegrityError


def create_short_url(long_url: str) -> UrlMap:
    # retry in the ultra-rare event of a collision
    for _ in range(5):
        code = generate_short_code(7)
        with get_session() as session:
            row = UrlMap(short_code=code, long_url=long_url)
            session.add(row)
            try:
                session.commit()
                session.refresh(row)
                return row
            except IntegrityError:
                session.rollback()
                continue
    raise RuntimeError("Failed to generate unique short code")


def resolve_code(short_code: str) -> str | None:
    with get_session() as session:
        stmt = select(UrlMap).where(UrlMap.short_code == short_code)
        row = session.exec(stmt).first()
        return row.long_url if row else None
