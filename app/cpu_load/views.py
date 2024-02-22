from aiohttp import web

from app.cpu_load.models import CPULoad


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