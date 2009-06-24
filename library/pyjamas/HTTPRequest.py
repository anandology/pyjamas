# This is the gtk-dependent HTTPRequest module.
# For the pyjamas/javascript version, see platform/HTTPRequestPyJS.py

import sys
if sys.platform not in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from pyjamas.__pyjamas__ import get_main_frame
    from pyjamas import Cookies
else:
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
        return get_main_frame().get_xml_http_request()

    def onReadyStateChange(self, xmlHttp, event, ignorearg):
        if (xmlHttp.props.ready_state != 4) :
            return
        # TODO - delete xmlHttp.onreadystatechange
        localHandler = xmlHttp.handler
        responseText = xmlHttp.props.response_text
        print "headers", xmlHttp.get_all_response_headers()
        status = xmlHttp.props.status
        handler = None
        xmlHttp = None
        print "response text", responseText, dir(responseText)
        if status == 200 :
            localHandler.onCompletion(responseText)
        else :
            localHandler.onError(responseText, status)
        
                
    def asyncPostImpl(self, user, pwd, url, postData, handler):
        xmlHttp = self.doCreateXmlHTTPRequest()
        if url[0] != '/':
            uri = get_main_frame().get_uri()
            if url[:7] != 'file://' and url[:7] != 'http://' and \
               url[:8] != 'https://':
                slash = uri.rfind('/')
                url = uri[:slash+1] + url
        print "xmlHttp", user, pwd, url, postData, handler, dir(xmlHttp)
        #try :
        xmlHttp.open("POST", url, True, '', '')
        xmlHttp.set_request_header("Content-Type", "text/plain charset=utf-8")
        for c in Cookies.get_crumbs():
            xmlHttp.set_request_header("Set-Cookie", c)
            print "setting cookie", c
        xmlHttp.connect("browser-event", self.onReadyStateChange)
        xmlHttp.add_event_listener("onreadystatechange")
        xmlHttp.handler = handler # hmm...
        #post_doc = get_main_frame().create_text_gdom_document()
        #body = post_doc.create_element("body")
        #tn = post_doc.create_text_node(postData)
        #post_doc.append_child(tn)
        #post_doc.props.body = body
        #print post_doc, dir(post_doc), list(post_doc.props)
        #print "inner html", post_doc.props.body.props.inner_html
        #sys.exit(0)
        #xmlHttp.send(post_doc)
        xmlHttp.send(postData)
        return True
    
        #except:
            #del xmlHttp.onreadystatechange
        handler = None
        xmlHttp = None
        localHandler.onError(str(e))
        return False
        

    def asyncGetImpl(self, user, pwd, url, handler):
        xmlHttp = self.doCreateXmlHTTPRequest()
        print dir(xmlHttp)
        try :
            xmlHttp.open("GET", url, true, None, None)
            xmlHttp.setRequestHeader("Content-Type", "text/plain charset=utf-8")
            # TODO: xmlHttp.onreadystatechange = self.onReadyStateChange
            xmlHttp.send('')
            return True
        
        except:
            #TODO: del xmlHttp.onreadystatechange
            handler = None
            xmlHttp = None
            localHandler.onError(String(e))
            return False
        
