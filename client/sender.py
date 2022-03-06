import socket

def sendRequest(req, host:str, port:int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(bytes(req.getRequest(), "utf-8"))
        data = s.recv(1024)

    print(f"Received {data!r}")