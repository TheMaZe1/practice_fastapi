from contextlib import asynccontextmanager
import redis.asyncio as redis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.database import init_models
from app.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_client = await redis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis_client), prefix='fastapi-cache')
    # await init_models()
    yield  # Здесь работает приложение
    print("Приложение завершает работу")


app = FastAPI(lifespan=lifespan)

app.include_router(router)
