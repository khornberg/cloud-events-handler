import json
import os

import pytest

from src.cloud_events import handler


def assert_response(response, expected_body="", expected_status_code=200, **kwargs):
    headers = response["headers"]
    assert response["status_code"] == expected_status_code
    if headers.get("Content-Type") in ["application/json"]:
        assert json.loads(response["body"]) == expected_body
    if kwargs.get("expected_headers"):
        assert headers == kwargs.get("expected_headers")


event = {}
context = {}
environ_headers = {"HTTP_ACCEPT": "application/vnd.api+json", "PATH_INFO": "/books/", "REQUEST_METHOD": "get"}
django_environ = {"PATH_INFO": "/books/", "REQUEST_METHOD": "get"}
django_app = "tests.django-app.project.wsgi.application"


@pytest.fixture
def delete_config():
    try:
        del os.environ["WSGI_APPLICATION"]
        del os.environ["WSGI_ENVIRON"]
    except KeyError:
        pass
    try:
        del os.environ["ASGI_APPLICATION"]
    except KeyError:
        pass


def test_handler(delete_config):
    os.environ["WSGI_APPLICATION"] = "wsgiref.simple_server.demo_app"
    expected = "Hello world!"
    response = handler.handler(event, context)
    assert_response(response)
    assert response["body"].startswith(expected)


@pytest.mark.django_db
def test_handler_with_django():
    os.environ["WSGI_ENVIRON"] = "tests.handler_test.django_environ"
    os.environ["WSGI_APPLICATION"] = django_app
    expected = []
    assert_response(handler.handler(event, context), expected)


@pytest.mark.django_db
def test_wsgi_with_headers():
    os.environ["WSGI_ENVIRON"] = "tests.handler_test.environ_headers"
    os.environ["WSGI_APPLICATION"] = django_app
    expected = json.dumps({"data": []}).replace(" ", "")
    expected_headers = {
        "Content-Type": "application/vnd.api+json",
        "Vary": "Accept, Cookie",
        "Allow": "GET, POST, HEAD, OPTIONS",
        "X-Frame-Options": "SAMEORIGIN",
        "Content-Length": "11",
    }
    assert_response(handler.handler(event, context), expected, expected_headers=expected_headers)


@pytest.mark.django_db
def test_handler_response_is_json_compatible():
    os.environ["WSGI_APPLICATION"] = django_app
    assert json.dumps(handler.handler(event, context))


def test_handler_for_asgi(delete_config):
    os.environ["ASGI_APPLICATION"] = "tests.asgi-app.app"
    expected = "Hello, world! I'm from an ASGI world"
    response = handler.handler(event, context)
    assert_response(response)
    assert response["body"] == expected


def test_handler_with_starlette(delete_config):
    os.environ["ASGI_APPLICATION"] = "tests.starlette-app.application"
    expected = json.dumps({"data": []})
    expected_headers = {
        "content-length": "11",
        "content-type": "application/vnd.api+json",
    }
    assert_response(handler.handler(event, context), expected, expected_headers=expected_headers)
