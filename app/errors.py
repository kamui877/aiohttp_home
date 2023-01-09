import json
from aiohttp import web


class HTTPError(web.HTTPException):
    def __init__(self, message):
        json_response = json.dumps({"error": message})
        super().__init__(text=json_response, content_type="application/json")


class BadRequest(HTTPError):
    status_code = 400


class NotFound(HTTPError):
    status_code = 404
