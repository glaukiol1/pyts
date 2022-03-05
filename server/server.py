import socket
import config
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((config.HOST, config.PORT))
while True:
    s.listen()
    conn, addr = s.accept()
    with conn:
        config.ON_CONNECTION(conn,addr)