import asyncio

from aiohttp import web

from app.config import config
from app.store.database.models import database_accessor


def setup_accessors(application):
    database_accessor.setup(application)


async def setup_background_tasks(application):
    from app.cpu_load.cpu_load_func import save_cpu_load
    application['cpu_load_task'] = asyncio.create_task(save_cpu_load())


async def stop_background_tasks(application):
    if 'cpu_load_task' in application:
        application['cpu_load_task'].cancel()
        await app['cpu_load_task']


def setup_config(application):
    application['config'] = config


def setup_app(application):
    setup_config(application)
    setup_accessors(application)
    application.on_startup.append(setup_background_tasks)
    application.on_cleanup.append(stop_background_tasks)


app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    web.run_app(app, port=config['common']['port'])
