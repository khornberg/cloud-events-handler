import json
import os

import pytest
from cloud_events.handler import handler


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

s3_example_event = {
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-2",
            "eventTime": "2019-09-03T19:37:27.192Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {"principalId": "AWS:AIDAINPONIXQXHT3IKHL2"},
            "requestParameters": {"sourceIPAddress": "205.255.255.255"},
            "responseElements": {
                "x-amz-request-id": "D82B88E5F771F645",
                "x-amz-id-2": "vlR7PnpV2Ce81l0PRw6jlUpck7Jo5ZsQjryTjKlc5aLWGVHPZLj5NeC6qMa0emYBDXOo6QBU0Wo=",
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "828aa6fc-f7b5-4305-8584-487c791949c1",
                "bucket": {
                    "name": "lambda-artifacts-deafc19498e3f2df",
                    "ownerIdentity": {"principalId": "A3I5XTEXAMAI3E"},
                    "arn": "arn:aws:s3:::lambda-artifacts-deafc19498e3f2df",
                },
                "object": {
                    "key": "b21b84d653bb07b05b1e6b33684dc11b",
                    "size": 1305107,
                    "eTag": "b21b84d653bb07b05b1e6b33684dc11b",
                    "sequencer": "0C0F6F405D6ED209E1",
                },
            },
        }
    ]
}

eventbridge_scheduled_example_event = {
    "id": "53dc4d37-cffa-4f76-80c9-8b7d4a4d2eaa",
    "detail-type": "Scheduled Event",
    "source": "aws.events",
    "account": "123456789012",
    "time": "2015-10-08T16:53:06Z",
    "region": "us-east-1",
    "resources": ["arn:aws:events:us-east-1:123456789012:rule/MyScheduledRule"],
    "detail": {},
}

cloudevents = {
    "specversion": "1.0-rc1",
    "type": "com.example.someevent",
    "source": "/my/context",
    "id": "A234-1234-1234",
    "time": "2018-04-05T17:31:00Z",
    "comexampleextension1": "value",
    "comexampleothervalue": 5,
    "datacontenttype": "text/xml",
    "data": '<much wow="xml"/>',
}


@pytest.mark.django_db
def test_aws_s3_file_added_event():
    os.environ["WSGI_APPLICATION"] = django_app
    event = expected = s3_example_event
    expected_headers = {
        "Content-Type": "application/json",
        "Vary": "Accept, Cookie",
        "Allow": "POST, OPTIONS",
        "X-Frame-Options": "SAMEORIGIN",
        "Content-Length": "810",
    }
    assert_response(handler(event, {}), expected, 201, expected_headers=expected_headers)


@pytest.mark.django_db
@pytest.mark.parametrize("event_payload", [s3_example_event, eventbridge_scheduled_example_event, cloudevents])
def test_events(event_payload):
    os.environ["WSGI_APPLICATION"] = django_app
    event = expected = event_payload
    assert_response(handler(event, {}), expected, 201)
