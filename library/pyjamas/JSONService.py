# Check http://json-rpc.org/wiki for the sepcification of JSON-RPC
# Currently:
#     http://groups.google.com/group/json-rpc/web/json-rpc-1-1-wd
#     http://groups.google.com/group/json-rpc/web/json-rpc-1-2-proposal


""" JSONService is a module providing JSON RPC Client side proxying.
"""

import sys
from HTTPRequest import HTTPRequest

try:
    from jsonrpc.json import dumps, loads, JSONDecodeException
except ImportError:
    from pyjamas.JSONParser import JSONParser
    parser = JSONParser()
    dumps = getattr(parser, 'encode')
    loads = getattr(parser, 'decodeAsObject')
    JSONDecodeException = None


__requestID = 0
__requestIDPrefix = 'ID'
__lastRequestID = None
def nextRequestID():
    """
    Return Next Request identifier.
    MUST be a JSON scalar (String, Number, True, False), but SHOULD normally 
    not be Null, and Numbers SHOULD NOT contain fractional parts.
    """
    global __requestID, __requestIDPrefix, __lastRequestID
    __requestID += 1
    id = "%s%s" % (__requestIDPrefix, __requestID)
    if __lastRequestID == id:
        # javascript integer resolution problem
        __requestIDPrefix += '_'
        __requestID = 0
        id = "%s%s" % (__requestIDPrefix, __requestID)
    __lastRequestID = id
    return id

# no stream support
class JSONService(object):
    def __init__(self, url, handler=None, headers=None):
        """
        Create a JSON remote service object. The url is the URL that will 
        receive POST data with the JSON request. See the JSON-RPC spec for 
        more information.

        The handler object should implement 
            onRemoteResponse(value, requestInfo)
        to accept the return value of the remote method, and
            onRemoteError(code, message, requestInfo)
        to handle errors.
        """
        self.url = url
        self.handler = handler
        self.headers = headers if headers is not None else {}
        if not self.headers.get("Accept"):
            self.headers["Accept"] = "application/json"

    def callMethod(self, method, params, handler = None):
        if handler is None:
            handler = self.handler

        if handler is None:
            return self.sendNotify(method, params)
        else:
            return self.sendRequest(method, params, handler)

    def onCompletion(self):
        pass

    def sendNotify(self, method, params):
        # jsonrpc: A String specifying the version of the JSON-RPC protocol. 
        #          MUST be exactly "2.0"
        #          If jsonrpc is missing, the server MAY handle the Request as 
        #          JSON-RPC V1.0-Request.
        # version: String specifying the version of the JSON-RPC protocol.
        #          MUST be exactly "1.1"
        # NOTE: We send both, to indicate that we can handle both.
        #
        # id:      If omitted, the Request is a Notification
        #          NOTE: JSON-RPC 1.0 uses an id of Null for Notifications.
        # method:  A String containing the name of the procedure to be invoked.
        # params:  An Array or Object, that holds the actual parameter values 
        #          for the invocation of the procedure. Can be omitted if 
        #          empty.
        #          NOTE: JSON-RPC 1.0 only a non-empty Array is used
        # From the spec of 1.1:
        #     The Content-Type MUST be specified and # SHOULD read 
        #     application/json.
        #     The Accept MUST be specified and SHOULD read application/json.
        #
        msg = {"jsonrpc": "2.0",
               "version": "1.1",
               "method": method, 
               "params": params
              }
        msg_data = dumps(msg)
        if not HTTPRequest().asyncPost(self.url, msg_data, self,
                                       False, "text/json",
                                       self.headers):
            return -1
        return 1

    def sendRequest(self, method, params, handler):
        id = nextRequestID()
        msg = {"jsonrpc": "2.0", 
               "id": id, 
               "method": method, 
               "params": params
              }
        msg_data = dumps(msg)

        request_info = JSONRequestInfo(id, method, handler)
        if not HTTPRequest().asyncPost(self.url, msg_data,
                                       JSONResponseTextHandler(request_info),
                                       False, "text/json",
                                       self.headers):
            return -1
        return id


class JSONRequestInfo(object):
    def __init__(self, id, method, handler):
        self.id = id
        self.method = method
        self.handler = handler


class JSONResponseTextHandler(object):
    def __init__(self, request):
        self.request = request

    def onCompletion(self, json_str):
        try:
            response = loads(json_str)
        except JSONDecodeException:
            # err.... help?!!
            error = dict(jsonrpc="2.0",
                         code=-32700,
                         message="Parse error while decoding response",
                         data=None,
                        )
            self.request.handler.onRemoteError(0, error, self.request)
            return

        if not response:
            error = dict(jsonrpc="2.0",
                         code=-32603,
                         message="Empty Resonse",
                         data=None,
                        )
            self.request.handler.onRemoteError(0, error, self.request)
        elif response.get("error"):
            error = response["error"]
            jsonrpc = error.get("jsonrpc")
            code = error.get("code", 0)
            message = error.get("message", errors)
            data = error.get("data")
            if not jsonrpc:
                jsonrpc = error.get("version", "1.0")
                if jsonrpc == "1.0":
                    message = error
                else:
                    data = error.get("error")
            error = dict(jsonrpc=jsonrpc,
                         code=code,
                         message=message,
                         data=data,
                        )
            self.request.handler.onRemoteError(0, error, self.request)
        elif response.get("result"):
            self.request.handler.onRemoteResponse(response["result"], 
                                                  self.request)
        else:
            self.request.handler.onRemoteError(error.get("code", 0), 
                                               self.request)

    def onError(self, error_str, error_code):
        error = dict(jsonrpc="2.0",
                     code=error_code,
                     message=error_str,
                     data=None,
                    )
        self.request.handler.onRemoteError(error_code, error, self.request)

class ServiceProxy(JSONService):
    def __init__(self, serviceURL, serviceName=None, headers=None):
        JSONService.__init__(self, serviceURL, headers=headers)
        self.__serviceName = serviceName

    def __call__(self, *params):
        if isinstance(params, tuple):
            params = list(params)
        if hasattr(params[-1], "onRemoteResponse"):
            handler = params[-1]
            return JSONService.sendRequest(self, self.__serviceName,
                                            params[:-1], handler)
        else:
            return JSONService.sendNotify(self, self.__serviceName, params)

# reserved names: callMethod, onCompletion
class JSONProxy(JSONService):
    def __init__(self, url, methods=None, headers=None):
        self._serviceURL = url 
        self.methods = methods
        self.headers = {} if headers is None else headers
        # Init with JSONService, for the use of callMethod
        JSONService.__init__(self, url, headers=self.headers)
        self.__registerMethods(methods)

    def __registerMethods(self, methods):
        if methods:
            for method in methods:
                setattr(self, 
                        method,
                        getattr(ServiceProxy(self._serviceURL, method, 
                                             headers=self.headers),
                                '__call__')
                       )

    # It would be nice to use __getattr__ (in stead of __registerMethods)
    # However, that doesn't work with pyjs and the use of __registerMethods
    # saves some repeated instance creations (now only once per method and 
    # not once per call)
    #def __getattr__(self, name):
    #    if not name in self.methods:
    #        raise AttributeError("no such method %s" % name) 
    #    return ServiceProxy(self._serviceURL, name, headers=self.headers)

