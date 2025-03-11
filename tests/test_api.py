import pytest

from app.schemas import SpimexTradeResponseList


@pytest.mark.asyncio(loop_scope="session")
async def test_get_last_trading_dates(async_client):
    response = await async_client.get("/last_trading_dates",params={"limit": 10})
    assert response.status_code == 200
    assert len(response.json()) == 10


@pytest.mark.asyncio(loop_scope="session")
async def test_get_dynamics(async_client):
    params = {
            "start_date": "2023-12-01",
            "end_date": "2023-12-05",
        }

    response = await async_client.get("/dynamics", params=params)
    assert response.status_code == 200
    SpimexTradeResponseList.model_validate_json(response.text)


@pytest.mark.asyncio(loop_scope="session")
async def test_get_trading_results(async_client):
    params = {
        "limit": 10,
    }
    
    response = await async_client.get("/trading_results", params=params)
    assert response.status_code == 200
    assert len(response.json()["trades"]) == 10
    SpimexTradeResponseList.model_validate_json(response.text)