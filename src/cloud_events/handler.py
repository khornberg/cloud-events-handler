from .adapter import get_wsgi_environ
from .interface import get_app
from .interface import get_asgi_response
from .interface import get_wsgi_response


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
        return {
            "status_code": response["statusCode"],
            "body": response["body"],
            "headers": response["headers"],
        }
