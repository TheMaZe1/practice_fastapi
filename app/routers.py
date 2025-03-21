from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache

from datetime import date

from app.cache import request_key_builder
from app.database import SessionLocal
from app.schemas import SpimexTradeResponse, SpimexTradeResponseList
from app.repositories.async_sql_repository import SQLAlchemyRepositoryAsync
from app.repositories.base_repository import BaseRepository
from app.schemas import SpimexTradeFiltres


async def get_db():
    async with SessionLocal() as db:
        yield db 


async def get_repo(db: AsyncSession = Depends(get_db)) -> BaseRepository:
    return SQLAlchemyRepositoryAsync(db)


router = APIRouter()


@router.get('/last_trading_dates', response_model=list[date], summary="Получение списка последних торговых дат")
@cache(expire=86400, key_builder=request_key_builder)
async def get_last_trading_dates(limit: int, repo: AsyncSession = Depends(get_repo)) -> list[date]:
    result = await repo.get_last_trading_dates(limit)
    return result


@router.get('/dynamics', response_model=SpimexTradeResponseList, summary="Получение динамики торгов за период")
@cache(expire=86400, key_builder=request_key_builder)
async def get_dynamics(
    start_date: date = Query(..., description="Начальная дата в формате YYYY-MM-DD"),
    end_date: date = Query(..., description="Конечная дата в формате YYYY-MM-DD"),
    filtres: SpimexTradeFiltres = Depends(),
    repo: BaseRepository = Depends(get_repo)) -> SpimexTradeResponseList:

    result = await repo.get_dynamics(start_date, end_date, filtres)
    return SpimexTradeResponseList(trades=result)


@router.get('/trading_results', response_model=SpimexTradeResponseList, summary="Получение результатов последних торгов с фильтрами")
@cache(expire=86400, key_builder=request_key_builder)
async def get_trading_results(filtres: SpimexTradeFiltres = Depends(), repo: BaseRepository = Depends(get_repo), limit: int = 100) -> SpimexTradeResponseList:
    result = await repo.get_trading_results(filtres, limit)
    return SpimexTradeResponseList(trades=result)