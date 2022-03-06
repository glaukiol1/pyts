from common.Response.Response import Response # only for a smother developing experience, remove this and the line below, while also removing them from the route handler functions
from common.Request.Request import Request
from server.server import Server

app = Server("127.0.0.1", 3000)

def index(request:Request, resp:Response):
    resp.setStatus(200, "OK")
    resp.setBody("<1>Index page</1>")
    resp.SendResponse()

def test(request:Request, resp:Response):
    resp.setStatus(200, "OK")
    resp.setBody("<1>Test page</1>")
    resp.SendResponse()

app.routeHandler("/", index)
app.routeHandler("/test", test)

app.startServer()