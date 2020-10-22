from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def test_route(request):
    return JSONResponse({"data": []}, headers={"Content-Type": "application/vnd.api+json"})


async def event_route(request):
    b = await request.body()
    import json

    return JSONResponse(json.loads(b), status_code=201)


application = Starlette(
    debug=True, routes=[Route("/", test_route, methods=["POST"]), Route("/aws.s3", event_route, methods=["POST"])]
)
