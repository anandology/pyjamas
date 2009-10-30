# no stream support
class JSONService:
    def __init__(self, url, handler = None):
        """
        Create a JSON remote service object.  The url is the URL that will receive
        POST data with the JSON request.  See the JSON-RPC spec for more information.

        The handler object should implement onRemoteResponse(value, requestInfo) to
        accept the return value of the remote method, and
        onRemoteError(code, message, requestInfo) to handle errors.
        """
        from pyjamas.JSONParser import JSONParser
        self.parser = JSONParser()
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

    def __sendNotify(self, method, params):
        msg = {"id":None, "method":method, "params":params}
        msg_data = self.parser.encode(msg)
        if not HTTPRequest().asyncPost(self.url, msg_data, self):
            return -1
        return 1

    def __sendRequest(self, method, params, handler):
        id = pygwt.getNextHashId()
        msg = {"id":id, "method":method, "params":params}
        msg_data = self.parser.encode(msg)

        request_info = JSONRequestInfo(id, method, handler)
        if not HTTPRequest().asyncPost(self.url, msg_data, JSONResponseTextHandler(request_info)):
            return -1
        return id


class JSONRequestInfo:
    def __init__(self, id, method, handler):
        self.id = id
        self.method = method
        self.handler = handler


class JSONResponseTextHandler:
    def __init__(self, request):
        self.request = request

    def onCompletion(self, json_str):
        from pyjamas.JSONParser import JSONParser
        response = JSONParser().decodeAsObject(json_str)

        if not response:
            self.request.handler.onRemoteError(0, "Server Error or Invalid Response", self.request)
        elif response.has_key("error") and response['error']:
            error = response["error"]
            self.request.handler.onRemoteError(0, error, self.request)
        else:
            self.request.handler.onRemoteResponse(response["result"], self.request)

    def onError(self, error_str, error_code):
        self.request.handler.onRemoteError(error_code, error_str, self.request)

# reserved names: callMethod, onCompletion
class JSONProxy(JSONService):
    def __init__(self, url, methods=None):
        JSONService.__init__(self, url)
        if methods:
            self.__registerMethods(methods)

    def __createMethod(self, method):
        JS("""
        return function() {
            var params = [];
            for (var n=0; n<arguments.length; n++) { params.push(arguments[n]); }
            if (params[params.length-1].onRemoteResponse) {
                var handler=params.pop();
                return this.__sendRequest(method, params, handler);
            }
            else {
                return this.__sendNotify(method, params);
            }
        };
        """)

    def __registerMethods(self, methods):
        JS("""
        methods=methods.__array;
        for (var i in methods) {
            var method = methods[i];
            this[method]=this.__createMethod(method);
        }
        """)

