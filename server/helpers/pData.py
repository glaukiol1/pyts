from common.common import *

def pData(conn) -> Request:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        return parseRequest(data)