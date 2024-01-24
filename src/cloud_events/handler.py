from .adapter import get_wsgi_environ
from .interface import get_app, get_asgi_response, get_wsgi_response


def handler(event, context):
    app_type, app = get_app()
    if app_type == "WSGI":
        environ = get_wsgi_environ(event)
        response = get_wsgi_response(app, environ)
        return {
            "status_code": response.status_code,
            "body": response.get_data(as_text=True),
            "headers": dict(response.headers),
        }
    if app_type == "ASGI":
        response = get_asgi_response(app, event, context)
        headers = {header[0].decode("utf-8"): header[1].decode("utf-8") for header in response["headers"]}
        return {
            "status_code": response["status"],
            "body": response["body"].decode("utf-8"),
            "headers": headers,
        }
