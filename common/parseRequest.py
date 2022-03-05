import json

from common.Request.Request import Request


def parseRequest(request):
    try:
        data = json.loads(request)
    except:
        return "Invalid Request"
    req = Request()
    req.setHeaders(data.headers)
    req.setBody(data.body)
    return req