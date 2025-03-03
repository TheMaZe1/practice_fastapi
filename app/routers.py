from fastapi import APIRouter, Depends, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache

from datetime import date

from app.database import SessionLocal
from app.schemas import SpimexTradeResponse
from app.repositories.async_sql_repository import SQLAlchemyRepositoryAsync
from app.repositories.base_repository import BaseRepository
from app.schemas import SpimexTradeFiltres


async def get_db():
    async with SessionLocal() as db:  # Используем async with для асинхронной сессии
        yield db  # Возвращаем сессию в обработчик запроса


async def get_repo(db: AsyncSession = Depends(get_db)) -> BaseRepository:
    return SQLAlchemyRepositoryAsync(db)

router = APIRouter()


def request_key_builder(
    func,
    namespace: str = "",
    *,
    request: Request = None,
    response: Response = None,
    **kwargs,
):
    return ":".join([
        namespace,
        request.method.lower(),
        request.url.path,
        repr(sorted(request.query_params.items()))
    ])

@router.get('/last_trading_dates', response_model=list[date], summary="Получение списка последних торговых дат")
@cache(expire=600, key_builder=request_key_builder)
async def get_last_trading_dates(limit: int, repo: AsyncSession = Depends(get_repo)) -> list[date]:
    result = await repo.get_last_trading_dates(limit)
    return result


@router.get('/dynamics', response_model=list[SpimexTradeResponse], summary="Получение динамики торгов за период")
@cache(expire=600, key_builder=request_key_builder)
async def get_dynamics(
    start_date: date = Query(..., description="Начальная дата в формате YYYY-MM-DD"),
    end_date: date = Query(..., description="Конечная дата в формате YYYY-MM-DD"),
    filtres: SpimexTradeFiltres = Depends(),
    repo: BaseRepository = Depends(get_repo)) -> list[SpimexTradeResponse]:

    result = await repo.get_dynamics(start_date, end_date, filtres)
    return result


@router.get('/trading_results', response_model=list[SpimexTradeResponse], summary="Получение результатов последних торгов с фильтрами")
@cache(expire=600, key_builder=request_key_builder)
async def get_trading_results(filtres: SpimexTradeFiltres = Depends(), repo: BaseRepository = Depends(get_repo), limit: int = 100) -> list[SpimexTradeResponse]:
    result = await repo.get_trading_results(filtres, limit)
    return result