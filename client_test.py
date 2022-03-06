from common.common import *
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3000  # The port used by the server

req = Request(HOST,PORT,"/")
req.setBody({"test": True})
req.SendRequest()