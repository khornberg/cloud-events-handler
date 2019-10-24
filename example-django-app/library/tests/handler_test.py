import json
import os

import library
import pytest
from library.handler import handler


def assert_response(response, expected_body="", expected_status_code=200, **kwargs):
    headers = response["headers"]
    assert response["status_code"] == expected_status_code
    if headers.get("Content-Type") in ["application/json"]:
        assert json.loads(response["body"]) == expected_body
    else:
        assert response["body"] == expected_body
    if kwargs.get("expected_headers"):
        assert headers == kwargs.get("expected_headers")


event = {}
context = {}
default_wsgi_environ = {
    "REQUEST_METHOD": "get",
    "PATH_INFO": "/books/",
    "wsgi.input": None,
    "SERVER_NAME": "localhost",
    "SERVER_PORT": "80",
    "SERVER_PROTOCOL": str("HTTP/1.1"),
    "wsgi.version": (1, 0),
    "wsgi.run_once": False,
    "wsgi.multiprocess": False,
    "wsgi.multithread": False,
    "wsgi.url_scheme": "http",
}


def test_handler(mocker):
    mocker.patch("library.handler.get_wsgi_environ")
    environ = default_wsgi_environ.copy()
    library.handler.get_wsgi_environ.return_value = environ
    os.environ["WSGI_APPLICATION"] = "wsgiref.simple_server.demo_app"
    expected = """Hello world!

PATH_INFO = '/books/'
REQUEST_METHOD = 'get'
SERVER_NAME = 'localhost'
SERVER_PORT = '80'
SERVER_PROTOCOL = 'HTTP/1.1'
wsgi.input = None
wsgi.multiprocess = False
wsgi.multithread = False
wsgi.run_once = False
wsgi.url_scheme = 'http'
wsgi.version = (1, 0)
"""
    assert_response(handler(event, context), expected)


@pytest.mark.django_db
def test_handler_with_django(mocker):
    mocker.patch("library.handler.get_wsgi_environ")
    environ = default_wsgi_environ.copy()
    library.handler.get_wsgi_environ.return_value = environ
    os.environ["WSGI_APPLICATION"] = "project.wsgi.application"
    expected = []
    assert_response(handler(event, context), expected)


@pytest.mark.django_db
def test_wsgi_with_headers(mocker):
    mocker.patch("library.handler.get_wsgi_environ")
    environ = default_wsgi_environ.copy()
    environ.update({"HTTP_ACCEPT": "application/vnd.api+json"})
    library.handler.get_wsgi_environ.return_value = environ
    os.environ["WSGI_APPLICATION"] = "project.wsgi.application"
    expected = json.dumps({"data": []}).replace(" ", "")
    expected_headers = {
        "Content-Type": "application/vnd.api+json",
        "Vary": "Accept, Cookie",
        "Allow": "GET, POST, HEAD, OPTIONS",
        "X-Frame-Options": "SAMEORIGIN",
        "Content-Length": "11",
    }
    assert_response(handler(event, context), expected, expected_headers=expected_headers)


@pytest.mark.django_db
def test_handler_response_is_json_compatible(mocker):
    mocker.patch("library.handler.get_wsgi_environ")
    environ = default_wsgi_environ.copy()
    library.handler.get_wsgi_environ.return_value = environ
    os.environ["WSGI_APPLICATION"] = "project.wsgi.application"
    assert json.dumps(handler(event, context))
