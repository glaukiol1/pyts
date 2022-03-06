import json
from time import sleep
from client.sender import sendRequest
from common.Response.Response import Response
from common.headers.headers import Headers
from common.parseResponse import parseResponse
class Request:
    def __init__(self,HOST,PORT,ENDPOINT):
        self.HOST = HOST
        self.PORT = PORT
        # default values
        self.Headers = Headers("REQUEST")
        self.Headers.setHeader("REQUEST-URL", f"pytf://{HOST}:{PORT}{ENDPOINT}")
        self.Headers.setHeader("HOST", HOST)
        self.Headers.setHeader("PORT", PORT)
        self.Headers.setHeader("ENDPOINT", ENDPOINT)
        self.Body = {}
    
    def setHeaders(self,headers):
        self.Headers.headers = headers

    def setHeader(self,header,value):
        self.Headers.setHeader(header,value)
    
    def setBody(self,body):
        self.Body = body

    def getRequest(self):
        request = {
            "headers": self.Headers.getHeaders(),
            "body": self.Body
        }
        return json.dumps(request)
    
    def SendRequest(self) -> Response:
        req = sendRequest(self,self.HOST,self.PORT)
        sleep(1)
        return parseResponse(req)