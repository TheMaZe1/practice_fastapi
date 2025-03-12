from datetime import date
import pytest

from app.repositories.async_sql_repository import SQLAlchemyRepositoryAsync
from app.schemas import SpimexTradeFiltres


@pytest.mark.asyncio(loop_scope="session")
async def test_get_last_trading_dates(session):
    repo = SQLAlchemyRepositoryAsync(session)
    
    dates = await repo.get_last_trading_dates(2)

    assert len(dates) == 2
    assert dates == [date(2024, 1, 5), date(2024, 1, 1)]


@pytest.mark.asyncio(loop_scope="session")
async def test_get_dynamics(session):
    repo = SQLAlchemyRepositoryAsync(session)
    
    start_date = date(2024, 1, 1)
    end_date = date(2024, 1, 5)
    filtres = SpimexTradeFiltres()

    trades = await repo.get_dynamics(start_date, end_date, filtres)

    assert len(trades) == 2
    assert trades[0].date == date(2024, 1, 1)
    assert trades[1].date == date(2024, 1, 5)


@pytest.mark.asyncio(loop_scope="session")
async def test_get_trading_results(session):
    repo = SQLAlchemyRepositoryAsync(session)

    filtres = SpimexTradeFiltres(oil_id="OIL1")
    trades = await repo.get_trading_results(filtres, limit=10)

    assert len(trades) == 1
    assert trades[0].oil_id == "OIL1"
    assert trades[0].date == date(2024, 1, 1)