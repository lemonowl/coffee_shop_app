import json


def format_request(request) -> dict:
    return json.loads(request.data.decode('utf-8'))
