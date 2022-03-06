from common.Response.Response import Response

def GetNotFoundResponse(conn,request):
    resp = Response(conn)
    endpoint = request.Headers.getHeaders()["ENDPOINT"]
    resp.setStatus(404, "Not Found")
    resp.setBody(f"{endpoint} was not found on this server. (404 Not Found)")
    return resp