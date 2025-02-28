from datetime import date
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from app.repositories.base_repository import T, Repository
from app.schemas import SpimexTradeFiltres
from models import Base


class SQLAlchemyRepositoryAsync(Repository):
    """Репозиторий для асинхронного подключения к БД"""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_last_trading_dates(self, limit: int):
        ...
    
    def get_dynamics(self, start_date: date, end_date: date, filtres: SpimexTradeFiltres):
        ...
    
    def get_trading_results(self, filtres: SpimexTradeFiltres):
        ...