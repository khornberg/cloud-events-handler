import os

from werkzeug.wrappers import Response

from .utils import import_string


def get_wsgi_response(app, environ):
    return Response.from_app(app, environ)


def get_app():
    app_path = os.environ.get("WSGI_APPLICATION")
    return import_string(app_path)
