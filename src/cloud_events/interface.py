import json
import os

from mangum.protocols.http import HTTPCycle
from werkzeug.wrappers import Response

from .adapter import get_asgi_scope
from .utils import import_string


def get_wsgi_response(app, environ):
    return Response.from_app(app, environ)


def _get_app_type():
    if os.environ.get("ASGI_APPLICATION"):
        return "ASGI"
    if os.environ.get("WSGI_APPLICATION"):
        return "WSGI"


def get_app():
    app_path = os.environ.get("WSGI_APPLICATION", os.environ.get("ASGI_APPLICATION"))
    return _get_app_type(), import_string(app_path)


def get_asgi_response(app, event, context):
    scope = get_asgi_scope(event, context)
    body = json.dumps(event).encode()
    asgi_cycle = HTTPCycle(scope, body=body)
    response = asgi_cycle(app)
    return response
