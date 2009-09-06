# This is the gtk-dependent HTTPRequest module.
# For the pyjamas/javascript version, see platform/HTTPRequestPyJS.py

import sys
import pygwt
from __pyjamas__ import JS
if sys.platform not in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from __pyjamas__ import get_main_frame

handlers = {}

class HTTPRequest:
    # also callable as: asyncPost(self, url, postData, handler)
    def asyncPost(self, user, pwd, url, postData=None, handler=None,
                        return_xml=0, content_type='text/plain charset=utf8'):
        if postData is None:
            return self.asyncPostImpl(None, None, user, pwd, url,
                                      return_xml, content_type)
        return self.asyncPostImpl(user, pwd, url, postData, handler,
                                 return_xml, content_type)

    # also callable as: asyncGet(self, url, handler)
    def asyncGet(self, user, pwd, url=None, handler=None):
        if url is None:
            return self.asyncGetImpl(None, None, user, pwd)
        return self.asyncGetImpl(user, pwd, url, handler)

    def createXmlHTTPRequest(self):
        return self.doCreateXmlHTTPRequest()

    def doCreateXmlHTTPRequest(self):
        return get_main_frame().getXmlHttpRequest()

    def onLoad(self, sender, event, ignorearg):
        xmlHttp = event.target
        localHandler = handlers.get(xmlHttp)
        del handlers[xmlHttp]
        responseText = xmlHttp.responseText
        status = xmlHttp.status
        handler = None
        xmlHttp = None
        # XXX HACK! webkit wrapper returns 0 not 200!
        if status == 0:
            print "HACK ALERT! webkit wrapper returns 0 not 200!"
        if status == 200 or status == 0:
            localHandler.onCompletion(responseText)
        else :
            localHandler.onError(responseText, status)
        
    def onReadyStateChange(self, xmlHttp, event, ignorearg):
        try:
            xmlHttp = get_main_frame().gobject_wrap(xmlHttp) # HACK!
        except:
            pass # hula / XUL
        print xmlHttp.readyState
        if xmlHttp.readyState != 4:
            return
        # TODO - delete xmlHttp.onreadystatechange
        localHandler = handlers.get(xmlHttp)
        del handlers[xmlHttp]
        responseText = xmlHttp.responseText
        print "headers", xmlHttp.getAllResponseHeaders()
        status = xmlHttp.status
        handler = None
        xmlHttp = None
        print "status", status
        print "local handler", localHandler
        # XXX HACK! webkit wrapper returns 0 not 200!
        if status == 0:
            print "HACK ALERT! webkit wrapper returns 0 not 200!"
        if status == 200 or status == 0:
            localHandler.onCompletion(responseText)
        else :
            localHandler.onError(responseText, status)
        
    def _convertUrlToAbsolute(self, url):

        uri = pygwt.getModuleBaseURL()
        if url[0] == '/':
            # url is /somewhere.
            sep = uri.find('://')
            if not uri.startswith('file://'):
                
                slash = uri.find('/', sep+3)
                if slash > 0:
                    uri = uri[:slash]

            return "%s%s" % (uri, url)

        else:
            if url[:7] != 'file://' and url[:7] != 'http://' and \
               url[:8] != 'https://':
                slash = uri.rfind('/')
                return uri[:slash+1] + url

        return url

    def asyncPostImpl(self, user, pwd, url, postData, handler, 
                            return_xml, content_type):
        mf = get_main_frame()
        xmlHttp = self.doCreateXmlHTTPRequest()
        url = self._convertUrlToAbsolute(url)
        print "xmlHttp", user, pwd, url, postData, handler, dir(xmlHttp)
        #try :
        if mf.platform == 'webkit' or mf.platform == 'mshtml':
            xmlHttp.open("POST", url, True, '', '')
        else:
            # EEK!  xmlhttprequest.open in xpcom is a miserable bastard.
            #xmlHttp.open("POST", url, True, '', '')
            print url, xmlHttp.open("POST", url)
        xmlHttp.setRequestHeader("Content-Type", content_type)
        xmlHttp.setRequestHeader("Content-Length", str(len(postData)))
        #for c in Cookies.get_crumbs():
        #    xmlHttp.setRequestHeader("Set-Cookie", c)
        #    print "setting cookie", c

        if mf.platform == 'webkit' or mf.platform == 'mshtml':
            mf._addXMLHttpRequestEventListener(xmlHttp, "onreadystatechange",
                                         self.onReadyStateChange)
        else:
            mf._addXMLHttpRequestEventListener(xmlHttp, "load",
                                         self.onLoad)
        handlers[xmlHttp] = handler
        xmlHttp.send(postData)
            
        return True
    
        #except:
            #del xmlHttp.onreadystatechange
        handler = None
        xmlHttp = None
        localHandler.onError(str(e))
        return False
        

    def asyncGetImpl(self, user, pwd, url, handler):
        mf = get_main_frame()
        url = self._convertUrlToAbsolute(url)
        xmlHttp = self.doCreateXmlHTTPRequest()
        print dir(xmlHttp)
        print user, pwd, url, handler
        #try :

        if mf.platform == 'webkit':
            xmlHttp.open("GET", url, True, user, pwd)
        else:
            xmlHttp.open("GET", url)
        xmlHttp.setRequestHeader("Content-Type", "text/plain charset=utf-8")
        # TODO: xmlHttp.onreadystatechange = self.onReadyStateChange
        xmlHttp.send('')
        return True
    
        #except:
        #    #TODO: del xmlHttp.onreadystatechange
        #    handler = None
        #    xmlHttp = None
        #    handler.onError(err)
        #    return False
        
