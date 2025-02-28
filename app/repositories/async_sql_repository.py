from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import SpimexTrade
from app.repositories.base_repository import BaseRepository
from app.schemas import SpimexTradeFiltres


class SQLAlchemyRepositoryAsync(BaseRepository):
    """Репозиторий для асинхронного подключения к БД"""

    async def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_last_trading_dates(self, limit: int) -> list[date]:
        ...
    
    async def get_dynamics(self, start_date: date, end_date: date, filtres: SpimexTradeFiltres) -> list[SpimexTrade]:
        ...
    
    async def get_trading_results(self, filtres: SpimexTradeFiltres) -> list[SpimexTrade]:
        ...