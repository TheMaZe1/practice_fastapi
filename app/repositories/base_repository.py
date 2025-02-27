import abc
from typing import TypeVar

from models import Base, SpimexTrade

T = TypeVar("T", bound=Base)


class Repository(abc.ABC):
    """Интерфейс для репозитория"""

    @abc.abstractmethod
    def add(self, entity: list[SpimexTrade]):
        raise NotImplementedError
    

    @abc.abstractmethod
    def update(self, id_: id):
        raise NotImplementedError
    

    @abc.abstractmethod
    def remove(self, id_: id):
        raise NotImplementedError
    

    @abc.abstractmethod
    def get_by_id(self, id_: id):
        raise NotImplementedError
