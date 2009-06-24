
class HTTPRequest:
    # also callable as: asyncPost(self, url, postData, handler)
    def asyncPost(self, user, pwd, url, postData=None, handler=None,
                                        returnxml=0):
        if postData == None:
            return self.asyncPostImpl(None, None, user, pwd, url, returnxml)
        return self.asyncPostImpl(user, pwd, url, postData, handler, returnxml)

    # also callable as: asyncGet(self, url, handler)
    def asyncGet(self, user, pwd, url, handler, returnxml=0):
        if url == None:
            return self.asyncGetImpl(None, None, user, pwd, returnxml)
        return self.asyncGetImpl(user, pwd, url, handler, returnxml)

    def createXmlHTTPRequest(self):
        return self.doCreateXmlHTTPRequest()

    def doCreateXmlHTTPRequest(self):
        JS("""
        return new XMLHttpRequest();
        """)

    def asyncPostImpl(self, user, pwd, url, postData, handler, returnxml=0):
        JS("""
        var xmlHttp = this.doCreateXmlHTTPRequest();
        try {
            xmlHttp.open("POST", url, true);
            xmlHttp.setRequestHeader("Content-Type",
                                           "application/x-www-form-urlencoded");
            xmlHttp.setRequestHeader("Content-Length", postData.length);
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4) {
                    delete xmlHttp.onreadystatechange;
                    var localHandler = handler;
                    var response;
                    var status = xmlHttp.status;
                    if (returnxml)
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

    def asyncGetImpl(self, user, pwd, url, handler, returnxml=0):
        JS("""
        var xmlHttp = this.doCreateXmlHTTPRequest();
        try {
            xmlHttp.open("GET", url, true);
            xmlHttp.setRequestHeader("Content-Type", "text/plain; charset=utf-8");
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4) {
                    delete xmlHttp.onreadystatechange;
                    var localHandler = handler;
                    var response;
                    var status = xmlHttp.status;
                    if (returnxml)
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
