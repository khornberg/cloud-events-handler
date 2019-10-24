import io
import json
import os
from importlib import import_module

from werkzeug.wrappers import Response


def get_path_for_event(event):
    path = ""
    if event.get("Records") and event["Records"][0].get("eventSource"):
        path = event["Records"][0].get("eventSource").replace(":", ".")
    if event.get("source"):
        path = event.get("source")
    return "/{}".format(path.replace("/", "", 1))


def get_user_environ():
    app_path = os.environ.get("WSGI_ENVIRON")
    if app_path:
        return import_string(app_path)
    return {}


def get_wsgi_environ(event):
    default_environ = {
        "CONTENT_TYPE": "application/json",
        "REQUEST_METHOD": "post",
        "PATH_INFO": "/",
        "SCRIPT_NAME": "",
        "SERVER_NAME": "localhost",
        "SERVER_PORT": "80",
        "SERVER_PROTOCOL": str("HTTP/1.1"),
        "wsgi.input": None,
        "wsgi.version": (1, 0),
        "wsgi.run_once": False,
        "wsgi.multiprocess": False,
        "wsgi.multithread": False,
        "wsgi.url_scheme": "http",
    }
    environ = {**default_environ, **get_user_environ()}
    if environ["REQUEST_METHOD"].lower() == "post":
        event_bytes = str.encode(json.dumps(event))
        environ["CONTENT_LENGTH"] = len(event_bytes)
        environ["wsgi.input"] = io.BytesIO(event_bytes)
    if event:
        environ["PATH_INFO"] = get_path_for_event(event)
    return environ


def get_wsgi_response(app, environ):
    return Response.from_app(app, environ)


# https://github.com/django/django/blob/4b4e68a7a6847e8b449923bb882bed01f0d7b2a8/django/utils/module_loading.py
def import_string(dotted_path):
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err
    module = import_module(module_path)
    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError('Module "%s" does not define a "%s" attribute/class' % (module_path, class_name)) from err


def get_app():
    app_path = os.environ.get("WSGI_APPLICATION")
    return import_string(app_path)


def handler(event, context):
    app = get_app()
    environ = get_wsgi_environ(event)
    response = get_wsgi_response(app, environ)
    return {
        "status_code": response.status_code,
        "body": response.get_data(as_text=True),
        "headers": dict(response.headers),
    }
