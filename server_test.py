from common.Response.Response import Response
from common.Request.Request import Request
from server.server import Server

app = Server("127.0.0.1", 3000)

def index(request:Request, resp:Response):
    print("From the handler!")
    resp.setStatus(200, "OK")
    resp.SendResponse()

app.routeHandler("/", index)

app.startServer()