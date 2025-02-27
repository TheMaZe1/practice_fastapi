from fastapi import APIRouter

from datetime import date

from app.models import SpimexTrade


router = APIRouter()


@router.get('/last_trading_dates')
async def get_last_trading_dates(limit: int) -> list[date]:
    ...


@router.get('/dynamics')
async def get_dynamics(start_date: date, end_date: date, oil_id: str = None, delivery_type_id: str = None, delivery_basis_id: str = None) -> list[SpimexTrade]:
    ...


@router.get('/trading_results')
async def get_trading_results(limit: int, oil_id: str = None, delivery_type_id: str = None, delivery_basis_id: str = None):
    ...