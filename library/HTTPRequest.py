from __pyjamas__ import JS

class HTTPRequest:
    # also callable as: asyncPost(self, url, postData, handler)
    def asyncPost(self, user, pwd, url, postData=None, handler=None):
        if postData == None:
            return self.asyncPostImpl(None, None, user, pwd, url)
        return self.asyncPostImpl(user, pwd, url, postData, handler)

    # also callable as: asyncGet(self, url, handler)
    def asyncGet(self, user, pwd, url, handler):
        if url == None:
            return self.asyncGetImpl(None, None, user, pwd)
        return self.asyncGetImpl(user, pwd, url, handler)

    def createXmlHTTPRequest(self):
        return self.doCreateXmlHTTPRequest()

    def doCreateXmlHTTPRequest(self):
        JS("""
        return new XMLHttpRequest();
        """)

    def asyncPostImpl(self, user, pwd, url, postData, handler):
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
                    var responseText = xmlHttp.responseText;
                    var status = xmlHttp.status;
                    handler = null;
                    xmlHttp = null;
                    if(status == 200) {
                        localHandler.onCompletion(responseText);
                    } else {
                        localHandler.onError(responseText, status);
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
            localHandler.onError(String(e));
            return false;
        }
        """)

    def asyncGetImpl(self, user, pwd, url, handler):
        JS("""
        var xmlHttp = this.doCreateXmlHTTPRequest();
        try {
            xmlHttp.open("GET", url, true);
            xmlHttp.setRequestHeader("Content-Type", "text/plain; charset=utf-8");
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4) {
                    delete xmlHttp.onreadystatechange;
                    var localHandler = handler;
                    var responseText = xmlHttp.responseText;
                    var status = xmlHttp.status;
                    handler = null;
                    xmlHttp = null;
                    if(status == 200) {
                        localHandler.onCompletion(responseText);
                    } else {
                        localHandler.onError(responseText, status);
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
            localHandler.onError(String(e));
            return false;
        }
        """)
