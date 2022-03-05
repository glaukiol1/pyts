from argparse import ArgumentError


class Headers:
    def __init__(self,TYPE):
        self.headers = {
            "VERSION": "PYTS/1.0.0",
        }
        if TYPE == "REQUEST": self.headers["type"] = "REQUEST"
        elif TYPE == "RESPONSE": self.headers["type"] = "RESPONSE"
        else: raise ArgumentError(None, "TYPE != REQUEST || RESPONSE!")
    
    def setHeader(self, header, value):
        self.headers[header] = value

    def getHeaders(self):
        return self.headers

    def getRequestType(self):
        return self.TYPE