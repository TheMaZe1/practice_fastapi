from datetime import date
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import SpimexTrade
from app.repositories.base_repository import BaseRepository
from app.schemas import SpimexTradeFiltres, SpimexTradeResponse


class SQLAlchemyRepositoryAsync(BaseRepository):
    """Репозиторий для асинхронного подключения к БД"""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_last_trading_dates(self, limit: int) -> list[date]:
        """Получает список дат последниих торговых дней.

        Args:
            limit (int): Ограничение на кол-во последних торговых дней.

        Returns:
            list[date]: Список дат последних торговых дней.
        """
        query = select(SpimexTrade.date).group_by(SpimexTrade.date)\
                    .order_by(desc(SpimexTrade.date))\
                    .limit(limit)
                                 
        dates = await self.db.execute(query)
        return dates.scalars().all()
    
    async def get_dynamics(self, start_date: date, end_date: date, filtres: SpimexTradeFiltres) -> list[SpimexTradeResponse]:
        """получает список торгов за заданный период.

        Args:
            start_date (date): Начальная дата периода, включительно.
            end_date (date): Конечная дата периода, включительно.
            filtres (SpimexTradeFiltres): Список фильтров.

        Returns:
            list[SpimexTradeResponse]: Список торгов за заданный период и соответствующий фильтрам.
        """
        query = select(SpimexTrade).filter(
            SpimexTrade.date >= start_date,
            SpimexTrade.date <= end_date
            )
        if filtres.oil_id:
            query = query.filter(SpimexTrade.oil_id == filtres.oil_id)
        if filtres.delivery_basis_id:
            query = query.filter(SpimexTrade.delivery_basis_id == filtres.delivery_basis_id)
        if filtres.delivery_type_id:
            query = query.filter(SpimexTrade.delivery_type_id == filtres.delivery_type_id)
        

        trades = await self.db.execute(query)
        return [SpimexTradeResponse.model_validate(trade) for trade in trades.scalars().all()]
    
    async def get_trading_results(self, filtres: SpimexTradeFiltres, limit: int = 100) -> list[SpimexTradeResponse]:
        """Получает список последних торгов.

        Args:
            filtres (SpimexTradeFiltres): Список фильтров
            limit (int, optional): Ограничение на кол-во последних торгов. По умолчанию 100.

        Returns:
            list[SpimexTradeResponse]: Список последних торгов, в соответствии с фильтрами.
        """
        query = select(SpimexTrade)

        if filtres.oil_id:
            query = query.filter(SpimexTrade.oil_id == filtres.oil_id)
        if filtres.delivery_basis_id:
            query = query.filter(SpimexTrade.delivery_basis_id == filtres.delivery_basis_id)
        if filtres.delivery_type_id:
            query = query.filter(SpimexTrade.delivery_type_id == filtres.delivery_type_id)
        

        trades = await self.db.execute(query.limit(limit))
        return [SpimexTradeResponse.model_validate(trade) for trade in trades.scalars().all()]