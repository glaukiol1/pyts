import json
from common.headers.headers import Headers
class Request:
    def __init__(self):
        # default values
        self.Headers = Headers("REQUEST")
        self.Body = {}
    
    def setHeaders(self,headers):
        self.Headers = headers

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
    