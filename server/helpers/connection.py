from server.helpers.pData import pData

def onConnection(conn, addr):
    print(f"Connected by {addr}")
    data = pData(conn)
    if data.Body.test == True:
        conn.sendall("GOOD!")
