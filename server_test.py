from common.common import Request
from server.server import Server

app = Server("127.0.0.1", 3000)

def index(request:Request):
    print("From the handler!")

app.routeHandler("/", index)

app.startServer()