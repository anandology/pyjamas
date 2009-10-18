# This is the gtk-dependent JSONService module.
# For the pyjamas/javascript version, see platform/JSONServicePyJS.py


""" JSONService is a module providing JSON RPC Client side proxying.
"""

import sys
from __pyjamas__ import JS
from HTTPRequest import HTTPRequest
import pygwt

# no stream support
class JSONService:
    def __init__(self, url, handler=None):
        """
        Create a JSON remote service object.  The url is the URL that will receive
        POST data with the JSON request.  See the JSON-RPC spec for more information.

        The handler object should implement onRemoteResponse(value, requestInfo) to
        accept the return value of the remote method, and
        onRemoteError(code, message, requestInfo) to handle errors.
        """
        self.url = url
        self.handler = handler

    def callMethod(self, method, params, handler = None):
        if handler is None:
            handler = self.handler

        if handler is None:
            return self.__sendNotify(method, params)
        else:
            return self.__sendRequest(method, params, handler)

    def onCompletion(self):
        pass

    def sendNotify(self, method, params):
        from jsonrpc.json import dumps
        msg = {"id": None, "method": method, "params": params}
        msg_data = dumps(msg)
        if not HTTPRequest().asyncPost(self.url, msg_data, self,
                                       content_type="text/x-json"):
            return -1
        return 1

    def sendRequest(self, method, params, handler):
        from jsonrpc.json import dumps
        id = pygwt.getNextHashId()
        msg = {"id":id, "method":method, "params":params}
        msg_data = dumps(msg)

        request_info = JSONRequestInfo(id, method, handler)
        if not HTTPRequest().asyncPost(self.url, msg_data,
                                       JSONResponseTextHandler(request_info),
                                       content_type="text/x-json"):
            return -1
        return id

    # dummy here - overridden in platform/JSONServicePyJS.py
    def __sendNotify(self, method, params): pass
    def __sendRequest(self, method, params, handler): pass


class JSONRequestInfo:
    def __init__(self, id, method, handler):
        self.id = id
        self.method = method
        self.handler = handler


class JSONResponseTextHandler:
    def __init__(self, request):
        self.request = request

    def onCompletion(self, json_str):
        from jsonrpc.json import loads, JSONDecodeException
        try:
            response = loads(json_str)
        except JSONDecodeException:
            # err.... help?!!
            self.request.handler.onRemoteError(0, "decode failure", None)
            return

        if not response:
            self.request.handler.onRemoteError(0, "Server Error or Invalid Response", self.request)
        elif response.get("error"):
            error = response["error"]
            self.request.handler.onRemoteError(error["code"], error["message"], self.request)
        else:
            self.request.handler.onRemoteResponse(response["result"], self.request)

    def onError(self, error_str, error_code):
        self.request.handler.onRemoteError(error_code, error_str, self.request)

class ServiceProxy(JSONService):
    def __init__(self, serviceURL, serviceName=None):
        JSONService.__init__(self, serviceURL)
        self.__serviceName = serviceName

    def __call__(self, *params):
        if hasattr(params[-1], "onRemoteResponse"):
            handler = params[-1]
            return JSONService.sendRequest(self, self.__serviceName,
                                            params[:-1], handler)
        else:
            return JSONService.sendNotify(self, self.__serviceName, params)

# reserved names: callMethod, onCompletion
class JSONProxy(JSONService):
    def __init__(self, url, methods=None):
        # don't call JSONService.__init__ here because we don't need it.
        # only in the override (JSONServicePyJS.py) is JSONService.__init__
        # needed.  in here, for pyjd, things are done slightly differently.
        # (using __getattr__).
        self._serviceURL = url 
        self.methods = methods

    def __createMethod(self, method):
        pass
    def __registerMethods(self, methods):
        pass

    def __getattr__(self, name):
        if not name in self.methods:
            raise AttributeError("no such method %s" % name) 
        return ServiceProxy(self._serviceURL, name)

