from common.Response.Response import Response
from server.helpers.pData import pData

def onConnection(conn, addr, RouteHandlers):
    print(f"Connected by {addr}")
    data = pData(conn)
    if data == None:
        # invalid request
        return
    if RouteHandlers[data.Headers.headers["ENDPOINT"]] != None:
        RouteHandlers[data.Headers.headers["ENDPOINT"]](data,Response(conn))
    else:
        conn.sendall(b"No handler")
