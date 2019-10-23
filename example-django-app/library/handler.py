import json
import os
from importlib import import_module
from werkzeug.wrappers import Response


def get_wsgi_response(app, environ):
    return Response.from_app(app, environ)


# https://github.com/django/django/blob/4b4e68a7a6847e8b449923bb882bed01f0d7b2a8/django/utils/module_loading.py
def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError('Module "%s" does not define a "%s" attribute/class' % (
            module_path, class_name)
        ) from err


def handler(event, context):
    app_path = os.environ.get('WSGI_APPLICATION')
    app = import_string(app_path)
    environ = {
        "REQUEST_METHOD": "get",
        "PATH": "/books/",
        "wsgi.input": None,
        "SERVER_NAME": "localhost",
        "SERVER_PORT": "80",
    }
    response = get_wsgi_response(app, environ)
    return {"status_code": response.status_code, "body": json.dumps(response.get_data(as_text=True))}
