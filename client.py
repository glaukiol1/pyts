from client.sender import sendRequest
from common.common import *
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3000  # The port used by the server

req = Request()
req.setBody({"test": True})
sendRequest(req,HOST,PORT)