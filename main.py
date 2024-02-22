from aiohttp import web


def setup_app(application):
    pass


app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    web.run_app(app)