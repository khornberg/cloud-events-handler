from .adapter import get_wsgi_environ
from .interface import get_app
from .interface import get_wsgi_response


def handler(event, context):
    app = get_app()
    environ = get_wsgi_environ(event)
    response = get_wsgi_response(app, environ)
    return {
        "status_code": response.status_code,
        "body": response.get_data(as_text=True),
        "headers": dict(response.headers),
    }
