import json

from cloud_events.handler import handler


def custom_handler(event, context):
    print(event)
    return handler(event, context)
