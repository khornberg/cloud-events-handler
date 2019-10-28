import json
import os

import pytest
from cloud_events.handler import handler

from tests import events

test_events = [getattr(events, e) for e in events.__dict__.keys() if not e.startswith('__')]


def assert_response(response, expected_body="", expected_status_code=200, **kwargs):
    headers = response["headers"]
    assert response["status_code"] == expected_status_code
    if headers.get("Content-Type") in ["application/json"]:
        assert json.loads(response["body"]) == expected_body
    else:
        assert response["body"] == expected_body
    if kwargs.get("expected_headers"):
        assert headers == kwargs.get("expected_headers")


django_app = "tests.django-app.project.wsgi.application"


@pytest.mark.django_db
def test_aws_s3_file_added_event():
    os.environ["WSGI_APPLICATION"] = django_app
    event = expected = events.s3_example_event
    expected_headers = {
        "Content-Type": "application/json",
        "Vary": "Accept, Cookie",
        "Allow": "POST, OPTIONS",
        "X-Frame-Options": "SAMEORIGIN",
        "Content-Length": "810",
    }
    assert_response(handler(event, {}), expected, 201, expected_headers=expected_headers)


@pytest.mark.django_db
@pytest.mark.parametrize("event_payload", test_events)
def test_events(event_payload):
    print(event_payload)
    os.environ["WSGI_APPLICATION"] = django_app
    event = expected = event_payload
    assert_response(handler(event, {}), expected, 201)
