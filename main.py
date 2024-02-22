from aiohttp import web

from app.config import config
from app.store.database.models import database_accessor


def setup_accessors(application):
    database_accessor.setup(application)


def setup_config(application):
    application['config'] = config


def setup_app(application):
    setup_config(application)
    setup_accessors(application)


app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    web.run_app(app, port=config['common']['port'])
