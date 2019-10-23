import json
from werkzeug.wrappers import Response

from wsgiref.simple_server import demo_app as app

environ = {
    "REQUEST_METHOD": "get",
    "PATH": "/books/",
    "wsgi.input": None,
    "SERVER_NAME": "localhost",
    "SERVER_PORT": "80",
}


def get_wsgi_response():
    return Response.from_app(app, environ)


def handler(event, context):
    response = get_wsgi_response()
    return {"status_code": response.status_code, "body": json.dumps(response.get_data(as_text=True))}
