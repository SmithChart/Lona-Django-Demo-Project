from lona.routing import Route, MATCH_ALL
from aiohttp_wsgi import WSGIHandler
from lona_project._django.wsgi import application
from lona_picocss.routes import IT_WORKS_ROUTE, SETTINGS_ROUTE, DEMO_ROUTES

wsgi_handler = WSGIHandler(application)


routes = [
    Route("/", view="views/home.py::HomeView", name="home"),
    SETTINGS_ROUTE,
    *DEMO_ROUTES,
    Route(MATCH_ALL, wsgi_handler, http_pass_through=True),
]
