from fastapi import APIRouter, Depends

from datetime import date

from app.database import SessionLocal
from app.models import SpimexTrade
from app.repositories.async_sql_repository import SQLAlchemyRepositoryAsync
from app.repositories.base_repository import BaseRepository
from app.schemas import SpimexTradeFiltres


def get_db():
    db = SessionLocal()  # Создаем сессию
    try:
        yield db  # Отдаем сессию в обработчик запроса
    finally:
        db.close()  # Закрываем после использования

router = APIRouter()


@router.get('/last_trading_dates')
async def get_last_trading_dates(limit: int, db: BaseRepository = Depends(get_db())) -> list[date]:
    repo = SQLAlchemyRepositoryAsync(db)
    return repo.get_last_trading_dates(limit)


@router.get('/dynamics')
async def get_dynamics(start_date: date, end_date: date, filtres: SpimexTradeFiltres = Depends(), db: BaseRepository = Depends(get_db())) -> list[SpimexTrade]:
    repo = SQLAlchemyRepositoryAsync(db)
    return repo.get_dynamics(start_date, end_date, filtres)


@router.get('/trading_results')
async def get_trading_results(limit: int, filtres: SpimexTradeFiltres = Depends(), db: BaseRepository = Depends(get_db())) -> list[SpimexTrade]:
    repo = SQLAlchemyRepositoryAsync(db)
    return repo.get_trading_results(limit, filtres)