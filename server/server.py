import socket
import server.config as config
class Server:
    def __init__(self,HOST,PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.RouteHandlers = {}

    def routeHandler(self, route:str, cb):
        self.RouteHandlers[route] = cb

    def startServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.HOST,self.PORT))
        print(f"INFO:: Server started; {self.HOST}:{self.PORT}")
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                config.ON_CONNECTION(conn,addr,self.RouteHandlers)