import asyncio
from datetime import datetime, timedelta
from sqlalchemy import func
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


async def get_cpu_loads_last_hour():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)

    cpu_loads = await CPULoad.query.where(
        (CPULoad.timestamp >= start_time) & (CPULoad.timestamp <= end_time)
    ).gino.all()

    return cpu_loads


async def compute_average_load_per_minute():
    cpu_loads = await get_cpu_loads_last_hour()

    average_loads_per_minute = {}

    for load in cpu_loads:
        minute = load.timestamp.replace(second=0, microsecond=0)
        minute_str = minute.strftime('%Y-%m-%d %H:%M:%S')
        if minute_str not in average_loads_per_minute:
            average_loads_per_minute[minute_str] = [load.value]
        else:
            average_loads_per_minute[minute_str].append(load.value)

    for minute, loads in average_loads_per_minute.items():
        average_loads_per_minute[minute] = sum(loads) / len(loads)

    return average_loads_per_minute


