from unittest.mock import patch
from httpx import ASGITransport, AsyncClient
import pytest_asyncio

patch('fastapi_cache.decorator.cache', lambda *args, **kwargs: lambda f: f).start()

from app.main import app

@pytest_asyncio.fixture(scope="session")
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

