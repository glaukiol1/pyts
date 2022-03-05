from helpers.parseData import parseData

def onConnection(conn, addr):
    print(f"Connected by {addr}")
    data = parseData(conn)
    conn.sendall(data)