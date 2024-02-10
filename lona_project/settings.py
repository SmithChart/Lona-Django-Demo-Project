from lona_picocss.middlewares import LonaPicocssMiddleware
from lona_picocss import settings, get_debug_navigation

from lona_picocss import (
    Error403View,
    Error404View,
    Error500View,
    NavItem,
    get_django_auth_navigation,
)

MIDDLEWARES = [
    "lona_picocss.middlewares.LonaPicocssMiddleware",
    "lona_django.middlewares.DjangoSessionMiddleware",
]

FRONTEND_TEMPLATE = settings.FRONTEND_TEMPLATE
ERROR_403_VIEW = Error403View
ERROR_404_VIEW = Error404View
ERROR_500_VIEW = Error500View

MAX_WORKER_THREADS = 4
MAX_STATIC_THREADS = 4
MAX_RUNTIME_THREADS = 6

ROUTING_TABLE = "routes.py::routes"

STATIC_DIRS = [
    settings.STATIC_DIR,
    "static",
    "img",
]

TEMPLATE_DIRS = [
    "templates",
    settings.TEMPLATE_DIR,
]

UPLOAD_DIR = "lona_project/static/upload/"
DELAY = 10
MULTI = 2

AIOHTTP_CLIENT_MAX_SIZE = 10 * 1024**2


# navigation
def get_navigation(server, request):
    nav_items = [
        NavItem(
            title="Home",
            url="/",
        ),
    ]

    # django auth navigation
    nav_items.extend(get_django_auth_navigation(server, request))

    return nav_items


PICOCSS_NAVIGATION = get_navigation
