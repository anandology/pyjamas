
class HTTPRequest:
    # also callable as: asyncPut(self, url, postData, handler)
    def asyncPut(self, user, pwd, url, postData=None, handler=None,
                                        returnxml=0,
                                        content_type='text/plain charset=utf8'):
        if postData is None:
            return self.asyncPutImpl(None, None, user, pwd, url, returnxml,
                                      content_type)
        return self.asyncPutImpl(user, pwd, url, postData, handler,
                                    returnxml,
                                  content_type)

    # also callable as: asyncDelete(self, url, handler)
    def asyncDelete(self, user, pwd, url=None, handler=None, returnxml=0):
        if url is None:
            return self.asyncDeleteImpl(None, None, user, pwd, returnxml)
        return self.asyncDeleteImpl(user, pwd, url, handler, returnxml)

    # also callable as: asyncPost(self, url, postData, handler)
    def asyncPost(self, user, pwd, url, postData=None, handler=None,
                                        returnxml=0,
                                        content_type='text/plain charset=utf8'):
        if postData is None:
            return self.asyncPostImpl(None, None, user, pwd, url, returnxml,
                                      content_type)
        return self.asyncPostImpl(user, pwd, url, postData, handler,
                                    returnxml,
                                  content_type)

    # also callable as: asyncGet(self, url, handler)
    def asyncGet(self, user, pwd, url=None, handler=None, 
                                        returnxml=0,
                                        content_type='text/plain charset=utf8'):
        if url is None:
            return self.asyncGetImpl(None, None, user, pwd, returnxml, content_type)
        return self.asyncGetImpl(user, pwd, url, handler, returnxml, content_type)

    def createXmlHTTPRequest(self):
        return self.doCreateXmlHTTPRequest()

    def doCreateXmlHTTPRequest(self):
        JS("""
        return new XMLHttpRequest();
        """)

    def asyncPutImpl(self, user, pwd, url, postData, handler,
                            returnxml, content_type):
        pdlen = str(len(postData))
        JS("""
        var xmlHttp = this.doCreateXmlHTTPRequest();
        try {
            xmlHttp.open("PUT", url, true);
            xmlHttp.setRequestHeader("Content-Type", content_type);
            xmlHttp.setRequestHeader("Content-Length", pdlen);
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4) {
                    delete xmlHttp.onreadystatechange;
                    var localHandler = handler;
                    var response;
                    var status = xmlHttp.status;
                    if (returnxml.valueOf())
                        response = xmlHttp.responseXML;
                    else
                        response = xmlHttp.responseText;
                    handler = null;
                    xmlHttp = null;
                    if(status == 200) {
                        localHandler.onCompletion(response);
                    } else {
                        localHandler.onError(response, status);
                    }
                }
            };
            xmlHttp.send(postData);
            return true;
        }
        catch (e) {
            delete xmlHttp.onreadystatechange;
            var localHandler = handler;
            handler = null;
            xmlHttp = null;
            localHandler.onError(String(e), "");
            return false;
        }
        """)

    def asyncDeleteImpl(self, user, pwd, url, handler, returnxml=0):
        JS("""
        var xmlHttp = this.doCreateXmlHTTPRequest();
        try {
            xmlHttp.open("DELETE", url, true);
            if (returnxml.valueOf())
                xmlHttp.setRequestHeader("Content-Type", "application/xml; charset=utf-8");
            else
                xmlHttp.setRequestHeader("Content-Type", "text/plain; charset=utf-8");
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4) {
                    delete xmlHttp.onreadystatechange;
                    var localHandler = handler;
                    var response;
                    var status = xmlHttp.status;
                    if (returnxml.valueOf())
                        response = xmlHttp.responseXML;
                    else
                        response = xmlHttp.responseText;
                    handler = null;
                    xmlHttp = null;
                    if(status == 200) {
                        localHandler.onCompletion(response);
                    } else {
                        localHandler.onError(response, status);
                    }
                }
            };
            xmlHttp.send('');
            return true;
        }
        catch (e) {
            delete xmlHttp.onreadystatechange;
            var localHandler = handler;
            handler = null;
            xmlHttp = null;
            localHandler.onError(String(e), "");
            return false;
        }
        """)

    def asyncPostImpl(self, user, pwd, url, postData, handler,
                            returnxml, content_type):
        pdlen = str(len(postData))
        JS("""
        var xmlHttp = this.doCreateXmlHTTPRequest();
        try {
            xmlHttp.open("POST", url, true);
            xmlHttp.setRequestHeader("Content-Type", content_type);
            xmlHttp.setRequestHeader("Content-Length", pdlen);
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4) {
                    delete xmlHttp.onreadystatechange;
                    var localHandler = handler;
                    var response;
                    var status = xmlHttp.status;
                    if (returnxml.valueOf())
                        response = xmlHttp.responseXML;
                    else
                        response = xmlHttp.responseText;
                    handler = null;
                    xmlHttp = null;
                    if(status == 200) {
                        localHandler.onCompletion(response);
                    } else {
                        localHandler.onError(response, status);
                    }
                }
            };
            xmlHttp.send(postData);
            return true;
        }
        catch (e) {
            delete xmlHttp.onreadystatechange;
            var localHandler = handler;
            handler = null;
            xmlHttp = null;
            localHandler.onError(String(e), "");
            return false;
        }
        """)

    def asyncGetImpl(self, user, pwd, url, handler, 
                            returnxml, content_type):
        JS("""
        var xmlHttp = this.doCreateXmlHTTPRequest();
        try {
            xmlHttp.open("GET", url, true);
            if (returnxml.valueOf())
                xmlHttp.setRequestHeader("Content-Type", "application/xml; charset=utf-8");
            else
                xmlHttp.setRequestHeader("Content-Type", content_type);
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4) {
                    delete xmlHttp.onreadystatechange;
                    var localHandler = handler;
                    var response;
                    var status = xmlHttp.status;
                    if (returnxml.valueOf())
                        response = xmlHttp.responseXML;
                    else
                        response = xmlHttp.responseText;
                    handler = null;
                    xmlHttp = null;
                    if(status == 200) {
                        localHandler.onCompletion(response);
                    } else {
                        localHandler.onError(response, status);
                    }
                }
            };
            xmlHttp.send('');
            return true;
        }
        catch (e) {
            delete xmlHttp.onreadystatechange;
            var localHandler = handler;
            handler = null;
            xmlHttp = null;
            localHandler.onError(String(e), "");
            return false;
        }
        """)
