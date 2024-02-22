import asyncio
from datetime import datetime

import psutil
from app.cpu_load.models import CPULoad
from app.store.database.models import database_accessor


async def get_cpu_load():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, psutil.cpu_percent)


async def save_cpu_load():
    while True:
        cpu_load = await get_cpu_load()
        async with database_accessor.db.transaction():
            await CPULoad.create(value=cpu_load, timestamp=datetime.now())
        print(cpu_load)
        await asyncio.sleep(5)

