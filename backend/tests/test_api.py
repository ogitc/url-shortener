import os
import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
import sys
from pathlib import Path

from app.main import app
from app.deps import init_db

backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))
os.environ["DATABASE_URL"] = "sqlite:///./test.db"


@pytest.fixture(scope="session", autouse=True)
def _setup_db():
    init_db()
    yield


@pytest.mark.asyncio
async def test_shorten_and_redirect():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # should fail with invalid URL
        r = await ac.post("/api/shorten", json={"url":"not-a-url"})
        assert r.status_code in (400, 422)

        # should succeed with valid URL
        r = await ac.post("/api/shorten", json={"url":"https://example.com/a"})
        assert r.status_code == status.HTTP_201_CREATED
        data = r.json()
        code = data["short_code"]

        # should redirect to the long URL
        r2 = await ac.get(f"/{code}", follow_redirects=False)
        assert r2.status_code == status.HTTP_302_FOUND
        assert r2.headers["location"] == "https://example.com/a"

        # should fail with not found
        r3 = await ac.get("/______", follow_redirects=False)
        assert r3.status_code == status.HTTP_404_NOT_FOUND
