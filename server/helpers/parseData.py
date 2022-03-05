def parseData(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        return data