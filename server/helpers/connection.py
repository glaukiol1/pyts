from common.Response.NotFoundResponse import GetNotFoundResponse
from common.Response.Response import Response
from server.helpers.pData import pData

def onConnection(conn, addr, RouteHandlers):
    print(f"Connected by {addr}")
    data = pData(conn)
    if data == None:
        # invalid request
        return
    try:
        handler = RouteHandlers[data.Headers.headers["ENDPOINT"]]
    except KeyError:
        resp = GetNotFoundResponse(conn,data)
        resp.SendResponse()
        return
    handler(data,Response(conn))