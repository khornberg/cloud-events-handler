import os
import json
from library.handler import handler


def assert_response(response, expected_body='', expected_status_code=200):
    assert response['status_code'] == expected_status_code
    assert json.loads(response['body']) == expected_body


def test_handler():
    os.environ.setdefault('WSGI_APPLICATION', 'wsgiref.simple_server.demo_app')
    event = {}
    context = {}
    expected = "Hello world!\n\nPATH = '/books/'\nREQUEST_METHOD = 'get'\nSERVER_NAME = 'localhost'\nSERVER_PORT = '80'\nwsgi.input = None\n"
    assert_response(handler(event, context), expected)


def test_handler_with_django():
    os.environ.setdefault('WSGI_APPLICATION', 'project.wsgi.application')
    event = {}
    context = {}
    expected = '{"authors":"None://localhost/authors/","books":"None://localhost/books/","paper-sources":"None://localhost/paper-sources/"}'
    assert_response(handler(event, context), expected)
