import json

from common.Response.Response import Response


def parseResponse(response):
    try:
        data = json.loads(response)
    except:
        return "Invalid Request"
    resp = Response(None)
    resp.setHeaders(data["headers"])
    resp.setBody(data["body"])
    resp.setStatus(resp.Headers.getHeaders()["STATUS-CODE"],resp.Headers.getHeaders()["STATUS-TEXT"])
    return resp