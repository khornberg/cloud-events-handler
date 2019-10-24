import json
import os

import pytest
from cloud_events import handler


def assert_response(response, expected_body="", expected_status_code=200, **kwargs):
    headers = response["headers"]
    assert response["status_code"] == expected_status_code
    if headers.get("Content-Type") in ["application/json"]:
        assert json.loads(response["body"]) == expected_body
    if kwargs.get("expected_headers"):
        assert headers == kwargs.get("expected_headers")


event = {}
context = {}
environ = {"TEST": "Thing"}
environ_headers = {"HTTP_ACCEPT": "application/vnd.api+json", "PATH_INFO": "/books/", "REQUEST_METHOD": "get"}
django_environ = {"PATH_INFO": "/books/", "REQUEST_METHOD": "get"}
django_app = "tests.django-app.project.wsgi.application"


def test_handler():
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


def test_get_user_environ_as_attribute():
    os.environ["WSGI_ENVIRON"] = "tests.handler_test.environ"
    assert handler.get_user_environ() == {"TEST": "Thing"}


def test_get_wsgi_environ():
    event = {"my": "event"}
    os.environ["WSGI_ENVIRON"] = "tests.handler_test.environ"
    environ = handler.get_wsgi_environ(event)
    environ.pop("wsgi.input")  # this is a BytesIO object
    assert environ == {
        "CONTENT_LENGTH": 15,
        "CONTENT_TYPE": "application/json",
        "PATH_INFO": "/",
        "REQUEST_METHOD": "post",
        "SCRIPT_NAME": "",
        "SERVER_NAME": "localhost",
        "SERVER_PORT": "80",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "TEST": "Thing",
        "wsgi.multiprocess": False,
        "wsgi.multithread": False,
        "wsgi.run_once": False,
        "wsgi.url_scheme": "http",
        "wsgi.version": (1, 0),
    }


@pytest.mark.parametrize(
    "event,expected", [({"source": "a"}, "/a"), ({"source": "/a"}, "/a"), ({"source": "/a/b"}, "/a/b")]
)
def test_get_path_for_event(event, expected):
    os.environ["WSGI_ENVIRON"] = "tests.handler_test.environ"
    assert handler.get_path_for_event(event) == expected
