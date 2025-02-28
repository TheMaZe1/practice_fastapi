from fastapi import FastAPI

from app.database import init_models
from app.routers import router

async def lifespan(app: FastAPI):
    # await init_models()
    yield  # Здесь работает приложение
    print("Приложение завершает работу")

app = FastAPI()

app.include_router(router)