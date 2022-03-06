# **pyts** | Python Transfer System

Data transfering system written in Python. HTTP-like, with headers and body for request/response. It uses sockets for communicating between server and client. Easy programming for endpoints; you can set route handlers with a function, which will give you access to two parameters, [*request*](https://github.com/glaukiol1/pyts/blob/main/common/Response/Response.py) and [*response*](https://github.com/glaukiol1/pyts/blob/main/common/Response/Response.py). You can use the response arguemnt to set headers and data, and you could call [*response.SendResponse()*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/Response/Response.py#L34) to send it back to the client.

## **pyts** | Client

A pyts client is the client in the server-client relationship. It sends requests, that will be responded to by the server. To send a request, you would first need to make the actual [*request*](https://github.com/glaukiol1/pyts/blob/main/common/Response/Response.py) class, and call the [*request.SendRequest*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/Request/Request.py#L35).

### Sending a Request

To build the Request, the syntax is as follows; `req = Request(HOST,PORT,ENDPOINT)`

- HOST = IP address of the server; a local server would be `127.0.0.1`
- PORT = Port of the **pyts** service
- ENDPOINT = the endpoint you are requesting; something like `/` or `/endpoint`.

Now that you have built the base request class, and have it in a variable, recomended namely `req`, it is time to set [*headers*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/headers/headers.py) and the [*body*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/Request/Request.py#L25).

- To set a single header, use [*request.setHeader*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/Request/Request.py#L22). To set all the headers at once (**NOT** recommended), pass a dict to [*request.setHeaders*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/Request/Request.py#L19).
- To set the body, use [*request.setBody*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/Request/Request.py#L25)

An example of setting a header and the body would be;

```py
req.setHeader("TEST-HEADER", True)
req.setBody({"test": True})
```

Now that our request is all set up, we can now send it. Call the [*request.SendRequest*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/Request/Request.py#L35) function. Note that this function returns the response back, so you would use something like;

```py
response = req.SendRequest()
```

Thats it! Now you have access to the [*Response*](https://github.com/glaukiol1/pyts/blob/91a5b74e20154b968d91cc59b1b0b908c98072e8/common/Response/Response.py) class. You have access to all the headers and data sent back. To get the status code, you can use;

```py
response.StatusCode
```
