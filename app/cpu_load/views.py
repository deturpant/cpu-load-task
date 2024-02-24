from aiohttp import web

from app.cpu_load.cpu_load_func import compute_average_load_per_minute, get_cpu_loads_last_hour, \
    get_program_status_changes_last_hour
from app.cpu_load.models import CPULoad


class ListViewShutdowns(web.View):
    async def get(self):
        intervals = await get_program_status_changes_last_hour()
        return web.json_response(data={"shutdowns" : intervals})


class ListViewCPUPerMin(web.View):
    async def get(self):
        averages = await compute_average_load_per_minute()
        return web.json_response(data={"cpu_loads": averages})


class ListViewCPULoadLastHour(web.View):
    async def get(self):
        avgs = await get_cpu_loads_last_hour()
        data = []
        for item in avgs:
            data.append({
                "timestamp": str(item.timestamp),
                "value": item.value,
                "id": item.id
            })
        return web.json_response(data={"cpu_loads": data})


class ListViewCPULoad(web.View):
    async def get(self):
        cpu_loads = await CPULoad.query.order_by(CPULoad.timestamp.desc()).gino.all()
        data = []
        for item in cpu_loads:
            data.append({
                "timestamp": str(item.timestamp),
                "value": item.value,
                "id": item.id
            })
        return web.json_response(data={"cpu_loads": data}, status=200)
