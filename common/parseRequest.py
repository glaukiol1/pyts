import json

from common.Request.Request import Request


def parseRequest(request):
    try:
        data = json.loads(request)
    except:
        return "Invalid Request"
    req = Request(data["headers"]["HOST"],data["headers"]["PORT"],data["headers"]["ENDPOINT"])
    req.setHeaders(data["headers"])
    req.setBody(data["body"])
    return req