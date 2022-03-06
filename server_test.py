from common.Response.Response import Response # only for a smother developing experience, remove this and the line below, while also removing them from the (index) function
from common.Request.Request import Request
from server.server import Server

app = Server("127.0.0.1", 3000)

def index(request:Request, resp:Response):
    print("From the handler!")
    resp.setStatus(200, "OK")
    resp.SendResponse()

app.routeHandler("/", index)

app.startServer()