import socket
import server.config as config
def startServer(HOST,PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    print(f"INFO:: Server started; {HOST}:{PORT}")
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            config.ON_CONNECTION(conn,addr)