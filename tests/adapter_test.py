import os

import pytest

from src.cloud_events import adapter

environ = {"TEST": "Thing"}


def test_get_user_environ_as_attribute():
    os.environ["WSGI_ENVIRON"] = "tests.adapter_test.environ"
    assert adapter.get_user_environ() == {"TEST": "Thing"}


def test_get_wsgi_environ():
    event = {"my": "event"}
    os.environ["WSGI_ENVIRON"] = "tests.adapter_test.environ"
    environ = adapter.get_wsgi_environ(event)
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
    os.environ["WSGI_ENVIRON"] = "tests.adapter_test.environ"
    assert adapter.get_path_for_event(event) == expected
