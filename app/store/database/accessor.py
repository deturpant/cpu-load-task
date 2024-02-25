from datetime import datetime

from aiohttp import web



class PostgresAccessor:
    def __init__(self) -> None:
        self.db = None

    def setup(self, application: web.Application) -> None:
        application.on_startup.append(self._on_connect)
        application.on_cleanup.append(self._on_disconnect)

    async def _on_connect(self, application: web.Application) -> None:
        from app.store.database.models import db
        self.config = application['config']['postgres']
        await db.set_bind(self.config['database_url'])
        self.db = db
        application['db'] = self
        async with self.db.transaction():
            from app.cpu_load.models import Log, CPULoad
            curr_timestamp = datetime.now()
            await CPULoad.create(value=0, timestamp=curr_timestamp)
            await Log.create(status="UP", timestamp=curr_timestamp)

    async def _on_disconnect(self, _) -> None:
        if self.db is not None:
            async with self.db.transaction():
                from app.cpu_load.models import Log, CPULoad
                curr_timestamp = datetime.now()
                await CPULoad.create(value=0, timestamp=curr_timestamp)
                await Log.create(status="DOWN", timestamp=curr_timestamp)
            await self.db.pop_bind().close()
