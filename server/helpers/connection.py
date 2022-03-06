from server.helpers.pData import pData

def onConnection(conn, addr, RouteHandlers):
    print(f"Connected by {addr}")
    data = pData(conn)
    if data == None:
        # invalid request
        return
    if RouteHandlers[data.Headers.headers["ENDPOINT"]] != None:
        conn.sendall(b"Found handler")
        RouteHandlers[data.Headers.headers["ENDPOINT"]](data)
    else:
        conn.sendall(b"No handler")
