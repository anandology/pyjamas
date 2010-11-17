# Copyright (C) 2010 Jim Washington
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# transliterated/translated from jsio-3.2/net/csp/transports.js

from __pyjamas__ import wnd, doc
import urllib
import base64
from pyjamas import DOM
from pyjamas import Window
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas.Timer import Timer
from random import random
from pyjamas.webio import json, logger

_doc = None

def clearDoc():
    global _doc
    if _doc:
        _doc.body.innerHTML = ''
    _doc = None

def getDoc():
    global _doc
    if _doc:
        return _doc
    try:
        _doc = wnd().ActiveXObject('htmlfile')
        if _doc:
            _doc.open().write('<html></html')
            _doc.close()
            wnd().attachEvent('onunload', clearDoc)
        DOM.setInnerHTML(_doc.body, '')
    except:
        pass
    if _doc is None:
        _doc = doc()
    return _doc

def XHR():
    xhr = HTTPRequest().createXmlHTTPRequest()
    return xhr

def createXHR():
    return XHR()

def isLocalFile(url):
    return url.startswith('file:')

def isSameDomain(urla, urlb):
    if urla.startswith('/'):
        return True
    elif urlb.startswith('http'):
        end_a = urla.find('/', urla.find('//'+2))
        domain_a = urla[:end_a]
        end_b = urlb.find('/', urlb.find('//'+2))
        domain_b = urlb[:end_b]
        if domain_b.lower() == domain_a.lower():
            return True
    return False

def isWindowDomain(url):
    return isSameDomain(url, Window.getLocation().getHref())

def canUseXHR(url):
    if isLocalFile(url):
        return False
    xhr = XHR()
    if not xhr:
        return False
    if isWindowDomain(url):
        return True
    # TODO: cross-domain support?

class Transports(object):
    pass

transports = Transports()

def chooseTransport(url, options):
    preferred = options.get('preferredTransport',None)
    if preferred == 'jsonp':
        return transports.jsonp
    elif canUseXHR(url):
        return transports.xhr
    return transports.jsonp

#class PARAMS(object):
#    xhrstream = {'is':"1","bs":"\n"}
#    xhrpoll = {"du":"0"}
#    xhrlongpoll = {}
#    sselongpoll = {"bp":"data: ","bs":"\r\n", "se": "1"}
#    ssestream = {"bp": "data: ", "bs": "\r\n", "se": "1", "is": "1"}

class BaseTransport(object):
    def __init__(self):
        self._aborted = False
        self._handshakeArgs = {'d':{}, 'ct':'application/javascript'}

    def handshake(self, url, options):
        logger.debug("handshake: %s %s" % (url, options))
        self._makeRequest('send', url + '/handshake',
            self._handshakeArgs, self.handshakeSuccess,
            self.handshakeFailure)

    def comet(self, url, sessionKey, lastEventId, options):
        logger.debug("comet: %s %s %s %s" % (url, sessionKey, lastEventId,
                                             options))
        args = {'s':sessionKey, 'a':lastEventId}
        self._makeRequest('send', 'url' + '/comet', args, self.cometSuccess,
                          self.cometFailure)

    def send(self, url, sessionKey, lastEventId, data, options):
        logger.debug("send: %s %s %s %s" % (url, sessionKey, data,
                                            options))
        args = {'d':data, 's':sessionKey, 'a':lastEventId}
        self._makeRequest('send', 'url' + '/send', args, self.sendSuccess,
                          self.sendFailure)

    def encodePacket(self, packetId, data, options):
        raise NotImplementedError()

    def abort(self):
        raise NotImplementedError()

    def _makeRequest(self, rType, url, args, cb, eb):
        raise NotImplementedError()



class Xhr(BaseTransport):
    _mustEncode = None
    def __init__(self):
        super(Xhr, self).__init__()
        self._xhr = {'send': XHR(), 'comet':XHR()}

    def abort(self):
        for i in self._xhr:
            self._abortXHR(i)

    def _abortXHR(self, key):
        xhr = self._xhr[key]
        try:
            if hasattr(xhr, 'onload'):
                xhr.onload = None
                xhr.onerror = None
                xhr.ontimeout = None
            elif hasattr(xhr, 'onreadystatechange'):
                xhr.onreadystatechange = None
            if hasattr(xhr, 'abort'):
                xhr.abort()
        except Exception(e):
            logger.debug("error aborting xhr %s" % e)
        self._xhr[key] = XHR()

    @property
    def mustEncode(self):
        if Xhr._mustEncode is not None:
            return Xhr._mustEncode
        if hasattr(createXHR(), 'sendAsBinary'):
            Xhr._mustEncode = False
        else:
            Xhr._mustEncode = True
        return Xhr._mustEncode

    def encodePacket(self, packetId, data, options):
        if self.mustEncode:
            return [packetId, 1, base64.urlsafe_b64encode(data)]
        else:
            return [packetId, 0, data]

    def _onReadyStateChange(self, rType, cb, eb):
        xhr = self._xhr[rType]
        try:
            data = {'status': xhr.status}
        except:
            eb({'response': 'Could not access status.'})
        try:
            if xhr.readyState != 4:
                return
            data.response = json.decode(xhr.responseText)
            if data['status'] != 200:
                logger.debug('XHR failed with status %s' % xhr.status)
                eb(data)
                return
            logger.debug('XHR data received')
        except Exception(e):
            logger.debug('Error in XHR::onReadyStateChange %s' % e)
            eb(data)
            self._abortXHR(rType)
            logger.debug('done handling XHR error')
        cb(data)

    def _makeRequest(self, rType, url, args, cb, eb):
        if self._aborted:
            return
        xhr = self._xhr[rType]
        data = None
        if 'd' in args:
            data = args['d']
            del args['d']
        # must open XHR first
        xhr.open('POST', url+ '?' + urllib.urlencode(args))
        # avoid preflighting
        xhr.setRequestHeader('Content-Type', 'text/plain')
        if hasattr(xhr, 'onload'):
            xhr.onload = self._onReadyStateChange(rType,cb,eb)
            xhr.onerror = eb
            xhr.ontimeout = eb
        elif hasattr(xhr, 'onreadystatechange'):
            xhr.onreadystatechange = self._onReadyStateChange(rType, cb, eb)
        if getattr(xhr, 'supportsBinary', None):
            def send():
                xhr.sendAsBinary(data)
        else:
            def send():
                xhr.send(data)
        Timer(notify=send, delayMillis=0)

transports.xhr = Xhr

def EMPTY_FUNCTION():
    pass

def createIframe():
    body = Window.getDocumentRoot()
    i = DOM.createElement('iframe')
    attrs = [('display','block'), ('width', '0'), ('height','0'),
             ('border','0'), ('margin','0'), ('padding', '0'),
             ('overflow', 'hidden'), ('visibility', 'hidden'),
             ('position','absolute'),('top','-999px'),('left', '-999px')]
    for name, value in attrs:
        DOM.setStyleAttribute(i, name, value)
    DOM.setAttribute(i,'cbId', '0')
    DOM.appendChild(body, i)
#    js = '''javascript:var d=document;
#    d.open();d.write("<html><body></body></html>");d.close();
#    '''
    js = 'about:blank'
    DOM.setAttribute(i, 'src', js)
    return i

def cleanupIframe(ifr):
    win = ifr.contentWindow
    doc = win.document

    scripts = doc.getElementsByTagName('script')
    while scripts.length:
        doc.body.removeChild(scripts[0])
        scripts = doc.getElementsByTagName('script')
    logger.debug('deleting iframe callbacks')
    win['cb' + DOM.getAttribute(ifr, 'cbId')] = EMPTY_FUNCTION
    win['eb' + DOM.getAttribute(ifr, 'cbId')] = EMPTY_FUNCTION

def removeIframe(ifr):
    def remove():
        if ifr is not None:
            if ifr.parentNode is not None:
                ifr.parentNode.removeChild(ifr)
    Timer(delayMillis=60000, notify=remove)


class Jsonp(BaseTransport):
    def __init__(self):
        super(Jsonp, self).__init__()
        self._onReady = []
        self._isReady = False
        self._createIframes()

    def _createIframes(self):
        self._ifr = {'send':False, 'comet':False}
        for item in ['send', 'comet']:
            self._ifr[item] = createIframe()
        while not self._ifr['send']:
            Timer(delayMillis=100,notify=self._createIframes)
        self._isReady = True
        readyArgs = tuple(self._onReady)
        self._onReady = []
        self._makeRequest(*readyArgs)

    def encodePacket(self, packetId, data, options):
        return [packetId, 1, base64.urlsafe_b64encode(data)]

    def abort(self):
        self._aborted = True
        for iframekey in self._ifr.keys():
            ifr = self._ifr[iframekey]
            if ifr:
                cleanupIframe(ifr)
                removeIframe(ifr)

    def _makeRequest(self, rType, url, args, cb, eb):
        if not self._isReady:
            for item in [rType, url, args, cb, eb]:
                self._onReady.append(item)
            return self._onReady
        ifr = self._ifr[rType]
        id = DOM.getIntAttribute(ifr, 'cbId') + 1
        req = {'type':rType,
               'id': id,
               'cb': cb,
               'eb': eb,
               'cbName': 'cb' + id,
               'ebName': 'eb' + id,
               'completed': False
                }
        args['n'] = str(random())[2:]
        if rType == 'send':
            args['rs'] = ';'
            args['rp'] = req['cbName']
        elif rType == 'comet':
            args['bs'] = ';'
            args['bp'] = req['cbName']
        req['url'] = url + '?' + urllib.urlencode(args)
        def send():
            self._request(req)
        Timer(delayMillis=0,notify=send)

    def _request(self, req):
        ifr = self._ifr[req['type']]
        win = ifr.contentWindow
        doc = win.document
        body = doc.body
        def cfe(resp):
            self.checkForError(req, resp)
        def ons(resp):
            self.onSuccess(req, resp)

        win[req['ebName']] = cfe
        win[req['cbName']] = ons

        # webkit
#        doc.open()
#        doc.write('<scr' + 'ipt src="' + req['url'] + '"></scr'+'ipt>'+
#                  '<scr' + 'ipt>'+req['ebName']+'(false)</scr'+'ipt>')
#        doc.close()
#
        # browser
        s = doc.createElement('script')
        s.src = req['url']

        # browser == ie
        if hasattr(s, 'onreadystatechange'):
            def orsc(event):
                self.onReadyStateChange(s)
            s.onreadystatechange = orsc
        else:
            s = DOM.createElement('script')
            DOM.setInnerHTML(s, req['ebName']+ '(false)')
        body.appendChild(s)

        self.killLoadingBar()

    def onSuccess(self, req, response):
        logger.debug('successful: %s %s' % (req['url'], response) )
        req['completed'] = True
        logger.debug('calling the cb')
        req['cb'](GLOBAL, {'status': 200, 'response': response})
        logger.debug('cb called')

    def onReadyStateChange(self, scriptTag):
        if scriptTag and scriptTag.readyState !='loaded':
            return
        scriptTag.onreadystatechange = EMPTY_FUNCTION()

    def checkForError(self, req, response):
        cleanupIframe(self._ifr[req['type']])
        if not req['completed']:
            data = {}
            if response:
                data['status'] = 200
                data['response'] = response
            else:
                data['status'] = 404
                data['response'] = 'Unable to load resource'
            logger.debug('error making request: %s %s' % (req['url'], data))
            logger.debug('calling eb')
            req['eb'](GLOBAL, data)

    def killLoadingBar(self):
        # only needed in firefox and opera...
        b = Window.getDocumentRoot()
        if b is None:
            return
        iframe = DOM.createElement('iframe')
        b.insertBefore(iframe, b.firstChild)
        b.removeChild(iframe)

transports.jsonp = Jsonp
