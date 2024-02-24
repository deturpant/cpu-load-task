from app.cpu_load import views


def setup_routes(app):
    app.router.add_get('/cpu_loads', views.ListViewCPULoad)
    app.router.add_get('/avg_loads', views.ListViewCPUPerMin)
    app.router.add_get('/last_hours_loads', views.ListViewCPULoadLastHour)
    app.router.add_get("/shutdowns", views.ListViewShutdowns)