import io
import json
import os

from .utils import import_string


def get_path_for_event(event):  # noqa C901
    path = ""
    if event.get("source"):
        path = event.get("source")
    if event.get("event") and event["event"].get("eventName"):
        path = event["event"].get("eventName")
    if event.get("Records") and event["Records"][0].get("eventSource"):
        path = event["Records"][0].get("eventSource").replace(":", ".")
    if event.get("Records") and event["Records"][0].get("EventSource"):
        path = event["Records"][0].get("EventSource").replace(":", ".")
    if event.get("bot") and event.get("outputDialogMode") and event.get("currentIntent"):
        path = "aws.lex"
    if event.get("records") and event["records"][0].get("kinesisRecordMetadata"):
        path = "aws.kinesis.firehose"
    if event.get("identityId") and event.get("identityPoolId"):
        path = "aws.cognito"
    if event.get("configRuleId"):
        path = "aws.config"
    if event.get("Records") and event["Records"][0].get("cf"):
        path = "aws.cloudfront"
    if event.get("LogicalResourceId"):
        path = "aws.cloudformation"
    if event.get("header") and event.get("payload"):
        path = "aws.alexa"

    return "/{}".format(path.replace("/", "", 1))


def get_user_environ():
    app_path = os.environ.get("WSGI_ENVIRON")
    if app_path:
        return import_string(app_path)
    return {}


def get_wsgi_environ(event):
    default_environ = {
        "CONTENT_TYPE": "application/json",
        "REQUEST_METHOD": "post",
        "PATH_INFO": "/",
        "SCRIPT_NAME": "",
        "SERVER_NAME": "localhost",
        "SERVER_PORT": "80",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "wsgi.version": (1, 0),
        "wsgi.run_once": False,
        "wsgi.multiprocess": False,
        "wsgi.multithread": False,
        "wsgi.url_scheme": "http",
        "wsgi.input": io.BytesIO(b""),
    }
    environ = {**default_environ, **get_user_environ()}
    if environ["REQUEST_METHOD"].lower() == "post":
        event_bytes = str.encode(json.dumps(event))
        environ["CONTENT_LENGTH"] = len(event_bytes)
        environ["wsgi.input"] = io.BytesIO(event_bytes)
    if event:
        environ["PATH_INFO"] = get_path_for_event(event)
    return environ


def get_asgi_scope(event, context):
    headers = {k.lower(): v for k, v in event.get("headers").items()} if event.get("headers") else {}
    return {
        "type": "http",
        "http_version": "1.1",
        "method": "POST",
        "headers": [[k.encode(), v.encode()] for k, v in headers.items()],
        "path": get_path_for_event(event),
        "raw_path": None,
        "root_path": "",
        "scheme": "https",
        "query_string": "",
        "server": "localhost",
        "client": "",
        "asgi": {"version": "3.0"},
        "aws.event": event,
        "aws.context": context,
    }
