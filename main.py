from aiohttp import web

from app.config import config


def setup_app(application):
    setup_config(application)


def setup_config(application):
    application['config'] = config


app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    web.run_app(app)