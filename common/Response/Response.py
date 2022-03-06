import json
from common.headers.headers import Headers
class Response:
    def __init__(self,conn):
        self.conn = conn
        # default values
        self.Headers = Headers("RESPONSE")
        self.Body = {}
    def setHeaders(self,headers):
        self.Headers.headers = headers

    def setHeader(self,header,value):
        self.Headers.setHeader(header,value)
    
    def setStatus(self,code,text):
        self.Headers.setHeader("STATUS-TEXT", text)
        self.Headers.setHeader("STATUS-CODE", code)
        self.Headers.setHeader("STATUS", f"{code} {text}")

    def setBody(self,body):
        self.Body = body

    def getResponse(self):
        response = {
            "headers": self.Headers.getHeaders(),
            "body": self.Body
        }
        return json.dumps(response)
    
    def SendResponse(self):
        self.conn.sendall(bytes(self.getResponse(), "utf-8"))