from pydantic import BaseModel

from datetime import date


class SpimexTrade(BaseModel):

    exchange_product_id: str
    exchange_product_name: str
    oil_id: str
    delivery_basis_id: str
    delivery_basis_name: str
    delivery_type_id: str
    volume: int
    total: float
    count: int
    date: date


class SpimexTradeFiltres(BaseModel):
    oil_id: str | None = None
    delivery_type_id: str | None = None
    delivery_basis_id: str | None = None