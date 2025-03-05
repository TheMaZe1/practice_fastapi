import asyncio
from datetime import datetime, time
from fastapi import Request, Response
import time as time_

from redis import Redis


CACHE_TIME_RESET = time(hour=14,minute=11)


def request_key_builder(
    func,
    namespace: str = "",
    *,
    request: Request = None,
    response: Response = None,
    **kwargs,
):
    return ":".join([
        namespace,
        request.method.lower(),
        request.url.path,
        repr(sorted(request.query_params.items()))
    ])


async def cache_time(redis_client: Redis):
    """Вычисляет время в сегундак до <CACHE_TIME_RESET>

    Returns:
        int: Кол-во секунд
    """
    while True:
        now = datetime.now()
        timedelta = now.replace(hour=CACHE_TIME_RESET.hour, minute=CACHE_TIME_RESET.minute) - now
        time_to_reset = timedelta.seconds + time_.time()
        while True:
            if time_.time() > time_to_reset:
                await redis_client.flushall()
                break
            else:
                await asyncio.sleep(20)
            