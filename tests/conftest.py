from datetime import date
from unittest.mock import patch

import pytest

patch('app.config.DB_NAME', "oil_reports_test").start()

from app.database import SessionLocal, async_engine
from app.models import Base, SpimexTrade


@pytest.fixture(scope="session")
async def session():
    async with SessionLocal() as session:
        yield session

@pytest.fixture(autouse=True, scope="session")
async def fill_test_db(session):
    """Заполняет тестовую БД данными перед тестами"""
    async with async_engine.begin() as conn:
        # Очистка таблиц
        await conn.run_sync(Base.metadata.drop_all)
        # Создание всех таблиц
        await conn.run_sync(Base.metadata.create_all)
    
    test_data = [
        SpimexTrade(
            id_=1, exchange_product_id="P1", exchange_product_name="Product 1",
            oil_id="OIL1", delivery_basis_id="B1", delivery_basis_name="Basis 1",
            delivery_type_id="D1", volume=100, total=1000.5, count=10,
            date=date(2024, 1, 1), created_on=date(2024, 1, 2), updated_on=date(2024, 1, 3)
        ),
        SpimexTrade(
            id_=2, exchange_product_id="P2", exchange_product_name="Product 2",
            oil_id="OIL2", delivery_basis_id="B2", delivery_basis_name="Basis 2",
            delivery_type_id="D2", volume=200, total=2000.5, count=20,
            date=date(2024, 1, 5), created_on=date(2024, 1, 6), updated_on=date(2024, 1, 7)
        ),
    ]
    
    session.add_all(test_data)
    await session.commit()
    