#import win32traceutil

import win32con
import sys
import os
from ctypes import *
import time

import _mshtml

import win32con

from ctypes import *
from ctypes.wintypes import *
from comtypes import IUnknown
from comtypes.automation import IDispatch, VARIANT
from comtypes.client import wrap, GetModule
from comtypes.client.dynamic import Dispatch

#from win32com.client import *
#cast = gencache.GetModuleForProgID('htmlfile')

if not hasattr(sys, 'frozen'):
    GetModule('atl.dll')
    GetModule('shdocvw.dll')

kernel32 = windll.kernel32
user32 = windll.user32
atl = windll.atl                  # If this fails, you need atl.dll

import win32con
from ctypes import *
from comtypes import IUnknown
from comtypes.automation import VARIANT
from comtypes.client import GetEvents
from comtypes.gen import SHDocVw
from comtypes.gen import MSHTML

kernel32 = windll.kernel32
user32 = windll.user32

WNDPROC = WINFUNCTYPE(c_long, c_int, c_uint, c_int, c_int)

class WNDCLASS(Structure):
    _fields_ = [('style', c_uint),
                ('lpfnWndProc', WNDPROC),
                ('cbClsExtra', c_int),
                ('cbWndExtra', c_int),
                ('hInstance', c_int),
                ('hIcon', c_int),
                ('hCursor', c_int),
                ('hbrBackground', c_int),
                ('lpszMenuName', c_char_p),
                ('lpszClassName', c_char_p)]

class RECT(Structure):
    _fields_ = [('left', c_long),
                ('top', c_long),
                ('right', c_long),
                ('bottom', c_long)]

class PAINTSTRUCT(Structure):
    _fields_ = [('hdc', c_int),
                ('fErase', c_int),
                ('rcPaint', RECT),
                ('fRestore', c_int),
                ('fIncUpdate', c_int),
                ('rgbReserved', c_char * 32)]

class POINT(Structure):
    _fields_ = [('x', c_long),
                ('y', c_long)]
    
class MSG(Structure):
    _fields_ = [('hwnd', c_int),
                ('message', c_uint),
                ('wParam', c_int),
                ('lParam', c_int),
                ('time', c_int),
                ('pt', POINT)]

def ErrorIfZero(handle):
    if handle == 0:
        raise WinError
    else:
        return handle

def _createDiv(doc):
    div = doc.createElement('div')
    print div
    style = div.style
    print style
    #style2 = style.QueryInterface(MSHTML.IHTMLStyle2)
    #style3 = style.QueryInterface(MSHTML.IHTMLStyle3)
    style.position = 'absolute'
    print "pos", style.position
    style.top = 0
    print "top", style.top
    sys.stdout.flush()
    print "left before", style.left
    style.left = 0
    print "left", style.left
    style.overflow = 'scroll'
    print "overflow", style.overflow
    style.overflowX = 'hidden'
    print "overflowX", style.overflowX
    style.width = 300
    print "width", style.width
    style.height = 100
    print "height", style.height
    style.scrollbarBaseColor = '#3366CC'
    style.borderBottom = '2px solid black'
    style.scrollbarHighlightColor = '#99CCFF'
    style.scrollbarArrowColor = 'white'
    div.innerHTML = 'Hello'
    return div

#b = Dispatch('InternetExplorer.Application')
#b.Navigate('about:<h1 id=header>Hello</h1><iframe id=frm src="about:"></iframe>')
#b.Visible = 1
#doc1 = cast.IHTMLDocument2(b.Document)
#header = doc1.all.item('header')
#frm = doc1.all.item('frm')
#frm2 = doc1.frames('frm')
#doc2 = cast.IHTMLDocument2(frm2.document)
#div = doc2.createElement('div')
#cast.DispHTMLBody(doc2.body).appendChild(div)

#popup = cast.DispHTMLWindow2(doc1.parentWindow).createPopup()
#doc3 = cast.IHTMLDocument2(popup.document)
#body = cast.DispHTMLBody(doc3.body)
#div = _createDiv()

class EventSink(object):
    # some DWebBrowserEvents
    def OnVisible(self, this, *args):
        print "OnVisible", args

    def BeforeNavigate(self, this, *args):
        print "BeforeNavigate", args

    def NavigateComplete(self, this, *args):
        print "NavigateComplete", this, args
        return

    # some DWebBrowserEvents2
    def BeforeNavigate2(self, this, *args):
        print "BeforeNavigate2", args

    def NavigateComplete2(self, this, *args):
        print "NavigateComplete2", args

    def DocumentComplete(self, this, *args):
        print "DocumentComplete", args
        if self.workaround_ignore_first_doc_complete == False:
            # ignore first about:blank.  *sigh*...
            # TODO: work out how to parse *args byref VARIANT
            # in order to get at the URI.
            self.workaround_ignore_first_doc_complete = True
            return
            
        self._loaded()

    def NewWindow2(self, this, *args):
        print "NewWindow2", args
        return
        v = cast(args[1]._.c_void_p, POINTER(VARIANT))[0]
        v.value = True

    def NewWindow3(self, this, *args):
        print "NewWindow3", args
        return
        v = cast(args[1]._.c_void_p, POINTER(VARIANT))[0]
        v.value = True

def addWindowEventListener(self, event_name, cb):
    #print self, event_name, cb
    if cb not in self._callbacks:
        self.connect("browser-event", cb)
        self._callbacks.append(cb)
    return self.addWindowEventListener(event_name, True)

def addXMLHttpRequestEventListener(element, event_name, cb):
    if not hasattr(element, "_callbacks"):
        element._callbacks = []
    if cb not in element._callbacks:
        element.connect("browser-event", cb)
        element._callbacks.append(cb)
    return element.addEventListener(event_name)

def addEventListener(element, event_name, cb):
    if not hasattr(element, "_callbacks"):
        element._callbacks = []
    if cb not in element._callbacks:
        element.connect("browser-event", cb)
        element._callbacks.append(cb)
    return element.addEventListener(event_name, True)

class EventCaller:
    def __init__(self, handler, name):
        self.handler = handler
        self.name = name
    def __call__(self, *args):
        callbacks = self.handler._listeners.get(self.name, [])
        for fn in callbacks:
            fn(*args)

class EventHandler:
    def __init__(self, pBrowser):
        self._pBrowser = pBrowser
        self._listeners = {}
    def __getattr__(self, name):
        print "EventHandler requested ", name
        if name.startswith('_') or name == 'addEventListener':
            return self.__dict__[name]
        if name.startswith('On'):
            return EventCaller(self, name[2:])
        raise NameError, '%s requested in EventHandler'
    def addEventListener(self, name, fn):
        if not self._listeners.has_key(name):
            self._listeners[name] = []
        self._listeners[name].append(fn)

class Browser(EventSink):
    def __init__(self, application, appdir):
        EventSink.__init__(self)
        self.platform = 'mshtml'
        self.application = application
        self.appdir = appdir
        self.already_initialised = False
        self.workaround_ignore_first_doc_complete = False
        self.window_listeners = []
        self.window_handler = None

        CreateWindowEx = windll.user32.CreateWindowExA
        CreateWindowEx.argtypes = [c_int, c_char_p, c_char_p, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int]
        CreateWindowEx.restype = ErrorIfZero

        # Create an instance of IE via AtlAxWin.
        atl.AtlAxWinInit()
        hInstance = kernel32.GetModuleHandleA(None)

        self.hwnd = CreateWindowEx(0,
                              "AtlAxWin",
                              "about:blank",
                              win32con.WS_OVERLAPPEDWINDOW |
                              win32con.WS_VISIBLE | 
                              win32con.WS_HSCROLL | win32con.WS_VSCROLL,
                              win32con.CW_USEDEFAULT,
                              win32con.CW_USEDEFAULT,
                              win32con.CW_USEDEFAULT,
                              win32con.CW_USEDEFAULT,
                              win32con.NULL,
                              win32con.NULL,
                              hInstance,
                              win32con.NULL)

        # Get the IWebBrowser2 interface for the IE control.
        self.pBrowserUnk = POINTER(IUnknown)()
        atl.AtlAxGetControl(self.hwnd, byref(self.pBrowserUnk))
        # the wrap call querys for the default interface
        self.pBrowser = wrap(self.pBrowserUnk)
        self.pBrowser.RegisterAsBrowser = True
        self.pBrowser.AddRef()

        self.conn = GetEvents(self.pBrowser, sink=self,
                        interface=SHDocVw.DWebBrowserEvents2)

    def _alert(self, txt):
        self.get_prompt_svc().alert(None, "Alert", txt)

    def load_app(self):

        uri = self.application
        if uri.find(":") == -1:
            # assume file
            uri = 'file://'+os.path.abspath(uri)

        print "load_app", uri

        self.application = uri
        v = byref(VARIANT())
        self.pBrowser.Navigate(uri, v, v, v, v)

        # Show Window
        cw = c_int(self.hwnd)
        windll.user32.ShowWindow(cw, c_int(win32con.SW_SHOWNORMAL))
        windll.user32.UpdateWindow(cw)

    def getGdomDocument(self):
        return Dispatch(self.pBrowser.Document)

    def getGdomWindow(self):
        return Dispatch(self.pBrowser.Document.window)

    def _addXMLHttpRequestEventListener(self, node, event_name, event_fn):
        
        return None
        listener = xpcom.server.WrapObject(ContentInvoker(node, event_fn),
                                            interfaces.nsIDOMEventListener)
        print event_name, listener
        node.addEventListener(event_name, listener, False)
        return listener

    def addEventListener(self, node, event_name, event_fn):
        
        return None
        listener = xpcom.server.WrapObject(ContentInvoker(node, event_fn),
                                            interfaces.nsIDOMEventListener)
        node.addEventListener(event_name, listener, True)
        return listener

    def mash_attrib(self, attrib_name):
        return attrib_name

    def _addWindowEventListener(self, event_name, event_fn):
        
        if self.window_handler is None:
            self.window_handler = EventHandler(self)
            self.window_conn = GetEvents(self.pBrowser.Document.window,
                                        sink=self.window_handler,
                                    interface=MSHTML.HTMLWindowEvents2)
        self.window_handler.addEventListener(event_name, event_fn)
        self.window_root.addEventListener(event_name, listener, True)
        return event_name # hmmm...

    def getXmlHttpRequest(self):
        xml_svc_cls = components.classes[ \
            "@mozilla.org/xmlextras/xmlhttprequest;1"]
        return xml_svc_cls.createInstance(interfaces.nsIXMLHttpRequest)
        
    def getUri(self):
        return self.application

    def _loaded(self):

        print "loaded"

        if self.already_initialised:
            return
        self.already_initialised = True

        from __pyjamas__ import pygwt_processMetas, set_main_frame
        #from __pyjamas__ import set_gtk_module
        set_main_frame(self)
        #set_gtk_module(gtk)

        (pth, app) = os.path.split(self.application)
        if self.appdir:
            pth = os.path.abspath(self.appdir)
        sys.path.append(pth)

def MainWin(one_event):

    # Pump Messages
    msg = MSG()
    pMsg = pointer(msg)
    NULL = c_int(win32con.NULL)
    
    while windll.user32.GetMessageA( pMsg, NULL, 0, 0) != 0:

        windll.user32.TranslateMessage(pMsg)
        windll.user32.DispatchMessageA(pMsg)

        #print msg.message, msg.wParam, msg.lParam
        #if msg.message == 161: # win32con.WM_DESTROY:
        #    windll.user32.PostQuitMessage(0)

        if one_event:
            break

    return msg.wParam
    
class ContentInvoker:

    def __init__(self, node, event_fn):
        self._node = node
        self._event_fn = event_fn

    def handleEvent(self, event):
        self._event_fn(self._node, event, False)

global wv
wv = None

def is_loaded():
    return wv.already_initialised

def run(one_event=False, block=True):
    MainWin(one_event) # TODO: ignore block arg for now

def setup(application, appdir=None, width=800, height=600):

    global wv
    wv = Browser(application, appdir)

    wv.load_app()

    while 1:
        if is_loaded():
            return
        run(one_event=True)

