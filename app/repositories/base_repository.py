import abc
from datetime import date
from typing import TypeVar

from app.schemas import SpimexTradeFiltres
from app.models import Base, SpimexTrade

T = TypeVar("T", bound=Base)


class BaseRepository(abc.ABC):
    """Интерфейс для репозитория"""
    
    @abc.abstractmethod
    def get_last_trading_dates(self, limit: int) -> list[date]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_dynamics(self, start_date: date, end_date: date, filtres: SpimexTradeFiltres) -> list[SpimexTrade]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_trading_results(self, filtres: SpimexTradeFiltres) -> list[SpimexTrade]:
        raise NotImplementedError
