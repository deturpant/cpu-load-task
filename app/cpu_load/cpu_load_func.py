import asyncio
from datetime import datetime

import psutil
from app.cpu_load.models import CPULoad
from app.store.database.models import database_accessor


async def get_cpu_load() -> float:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, psutil.cpu_percent)
