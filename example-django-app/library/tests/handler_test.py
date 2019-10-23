import os
import json
from library.handler import handler


def assert_response(response, expected_body="", expected_status_code=200):
    headers = dict(response["headers"])
    assert response["status_code"] == expected_status_code
    if headers.get("Content-Type") in ["application/json"]:
        assert json.loads(response["body"]) == expected_body
    else:
        assert response["body"] == expected_body


def test_handler():
    os.environ["WSGI_APPLICATION"] = "wsgiref.simple_server.demo_app"
    event = {}
    context = {}
    expected = """Hello world!

PATH = '/books/'
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


def test_handler_with_django():
    os.environ["WSGI_APPLICATION"] = "project.wsgi.application"
    event = {}
    context = {}
    expected = {
        "authors": "http://localhost/authors/",
        "books": "http://localhost/books/",
        "paper-sources": "http://localhost/paper-sources/",
    }
    assert_response(handler(event, context), expected)
