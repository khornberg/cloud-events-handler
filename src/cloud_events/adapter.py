import io
import json
import os

from .utils import import_string


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
