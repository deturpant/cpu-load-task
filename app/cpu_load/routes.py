from app.cpu_load import views


def setup_routes(app):
    app.router.add_get('/cpu_loads', views.ListViewCPULoad)