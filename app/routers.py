from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from datetime import date

from app.database import SessionLocal
from app.schemas import SpimexTradeResponse
from app.repositories.async_sql_repository import SQLAlchemyRepositoryAsync
from app.repositories.base_repository import BaseRepository
from app.schemas import SpimexTradeFiltres


async def get_db():
    db = SessionLocal()  # Создаем сессию
    try:
        yield db  # Отдаем сессию в обработчик запроса
    finally:
        db.close()  # Закрываем после использования


async def get_repo(db: AsyncSession = Depends(get_db)) -> BaseRepository:
    return SQLAlchemyRepositoryAsync(db)

router = APIRouter()


@router.get('/last_trading_dates', response_model=list[date], summary="Получение списка последних торговых дат")
async def get_last_trading_dates(limit: int, repo: AsyncSession = Depends(get_repo)) -> list[date]:
    result = await repo.get_last_trading_dates(limit)
    return result


@router.get('/dynamics', response_model=list[SpimexTradeResponse], summary="Получение динамики торгов за период")
async def get_dynamics(
    start_date: date = Query(..., description="Начальная дата в формате YYYY-MM-DD"),
    end_date: date = Query(..., description="Конечная дата в формате YYYY-MM-DD"),
    filtres: SpimexTradeFiltres = Depends(),
    repo: BaseRepository = Depends(get_repo)) -> list[SpimexTradeResponse]:

    result = await repo.get_dynamics(start_date, end_date, filtres)
    return result


@router.get('/trading_results', response_model=list[SpimexTradeResponse], summary="Получение результатов последних торгов с фильтрами")
async def get_trading_results(limit: int, filtres: SpimexTradeFiltres = Depends(), repo: BaseRepository = Depends(get_repo)) -> list[SpimexTradeResponse]:
    result = await repo.get_trading_results(limit, filtres)
    return result