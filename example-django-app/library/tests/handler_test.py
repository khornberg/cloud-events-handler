import json
from library.handler import handler


def assert_response(response, expected_body='', expected_status_code=200):
    assert response['status_code'] == expected_status_code
    assert json.loads(response['body']) == expected_body


def test_handler():
    event = {}
    context = {}
    expected = "Hello world!\n\nPATH = '/books/'\nREQUEST_METHOD = 'get'\nSERVER_NAME = 'localhost'\nSERVER_PORT = '80'\nwsgi.input = None\n"
    assert_response(handler(event, context), expected)
