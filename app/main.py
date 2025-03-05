import asyncio
from contextlib import asynccontextmanager
import redis.asyncio as redis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.cache import cache_time
from app.config import REDIS
from app.database import init_models
from app.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_client = await redis.from_url(f"redis://{REDIS}")
    FastAPICache.init(RedisBackend(redis_client), prefix='fastapi-cache')
    cache_task = asyncio.create_task(cache_time(redis_client))
    yield  # Здесь работает приложение
    cache_task.cancel()
    await redis_client.close()


app = FastAPI(lifespan=lifespan)

app.include_router(router)
