#! -*- coding: utf-8 -*-
# Copyright (C) 2010 Henning Schroeder <henning.schroeder@gmail.com>
# Copyright (C) 2010 Luke Leighton <lkcl@lkcl.net>

import sys
import os
from cgi import escape as html_quote

from PyQt4.QtCore import QUrl, SIGNAL, pyqtSignature, QObject, QVariant, QString
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtWebKit import QWebView, QWebElement, QWebElementCollection





class _ElementBase(object):

    
    @property
    def nodeType(self):
        return self._js("nodeType")

    @property
    def innerHTML(self):
        return self.getAttribute("html")
    
    @property
    def length(self):
        return self.getAttribute("length")
    
    @property
    def type(self):
        return self.getAttribute("type")
    
    @property
    def offsetParent(self):
        return int(self.getAttribute("offsetParent") or "0")

    
    @property
    def offsetTop(self):
        return int(self.getAttribute("offsetTop") or "0")

    
    @property
    def offsetLeft(self):
        return int(self.getAttribute("offsetLeft") or "0")
    

    @property
    def scrollTop(self):
        return int(self.getAttribute("scrollTop") or "0")

    
    @property
    def scrollLeft(self):
        return int(self.getAttribute("scrollLeft") or "0")


    @property
    def rows(self):
        rows = self._js("rows")
        print "rows", repr(rows)
        return _ElementProxy(rows)
    

    def setInnerText(self, text):
        self.setInnerHTML(html_quote(text))


    def insertChild(self, child, before_index):
        element = self._element
        i = 0
        while i < before_index or element is None:
            element = element.nextSibling()
            i += 1
        if element is None:
            return
        element.appendInside(child._element)


        
    def getParent(self):
        return _ElementProxy(self._element.parent())
    
    
    def _js(self, cmd):
        self._element.evaluateJavaScript("this.%s" % cmd)
        
    
    def cloneNode(self, arg):
        return _ElementProxy(self._element.clone())

    def blur(self):
        self._js("blur()");
    

    def focus(self):
        self._js("focus()");


class _NewElement(_ElementBase):
    
    
    def __init__(self, tag_name, **attrs):
        self._tag_name = tag_name.lower()
        self._inner_html = ""
        self._attrs = attrs
        self._styles = {}


    def getAttribute(self, name, default=""):
        return self._attrs.get(name.lower(), default)


    def setAttribute(self, name, value):
        if name.lower() == "style":
            print "Warning: style should be set with setStyleAttribute and not with setAttribute"
        self._attrs[name.lower()] = value
        

    def setStyleAttribute(self, name, value):
        self._styles[name.lower()] = value
        
    
    def setInnerHTML(self, html):
        self._inner_html = html

        
    def setInnerText(self, text):
        self._inner_html = html_quote(text)


    def __str__(self):
        html = "<%s" % self._tag_name
        for k, v in self._attrs.items():
            html += ' %s="%s"' % (k, v)
        if self._styles:
            html += ' style="'
            for ks, vs in self._styles.items():
                html += "%s:%s;" % (ks, vs)
            html += '"'
        html += ">"
        html += self._inner_html
        html += "</%s>" % self._tag_name
        return html



class _ElementProxy(_ElementBase):


    def __init__(self, element):
        self._element = element

        
    def __hash__(self):
        return hash(self._element)

        
    def __repr__(self):
        return "<%s>" % unicode(self._element.tagName())


    def getAttribute(self, name, default=""):
        value = self._element.attribute(name, default)
        if isinstance(value, QWebElement):
            return _ElementProxy(value)
        return unicode(value)

        
    def setAttribute(self, name, value):
        if name == "className":
            name = "class"
        self._element.setAttribute(name, value)


    def getInnerHTML(self):
        return self._element.toInnerXml()

    def setInnerHTML(self, html):
        self._element.setInnerXml(html)


    def setStyleAttribute(self, name, value):
        self._element.setStyleProperty(name, value + "!important")


    def appendChild(self, child):
        if isinstance(child, _ElementProxy):
            self._element.appendInside(child._element)
        else:
            self._element.appendInside(str(child))
            for name, value in child._styles.items():
                self.setStyleAttribute(name, value)



class _Document(_ElementProxy):

    @property
    def body(self):
        return _ElementProxy(self._element.findFirst("body"))


    def createElement(self, tag):
        global app
        # XXX: which solution is better?
        #return _NewElement(tag)
        tag_id = "__create_new_element_id__"
        js = """
        var _new_tag = document.createElement("%s");
        _new_tag.setAttribute("id", "%s");
        document.body.appendChild(_new_tag);
        """ % (tag, tag_id)
        doc = app.getDomDocument()
        doc._element.evaluateJavaScript(js)
        element = doc._element.findFirst("%s#%s" % (tag, tag_id))
        element.removeAttribute("id")
        element = element.takeFromDocument()
        return _ElementProxy(element)




def console(*args):
    print "console:", args


def JS(code):
    print "js: %r" % code
    global app
    print app.getDomDocument().evaluateJavaScript(code)
    



_app = None
_win = None
_browser = None

class QBrowserApp:

    def __init__(self, filename, width, height):
        self._listeners = []
        self.app = QApplication(sys.argv)
        self.win = QMainWindow()
        self.win.resize(width, height)
        self.browser = QWebView(_win)
        filename = os.path.abspath(filename)
        self.browser.setUrl(QUrl(filename))
        filename = filename.split("?")[0]
        path, path = os.path.split(filename)
        self.browser.setHtml(open(filename).read(),
                             QUrl.fromLocalFile(filename))
        self.win.setCentralWidget(self.browser)
        self.win.show()

        from __pyjamas__ import pygwt_processMetas, set_main_frame
        from __pyjamas__ import set_gtk_module
        set_main_frame(self)

    def current_web_frame(self):
        return self.browser.page().currentFrame()

    def getDomDocument(self):
        element = self.current_web_frame().documentElement()
        return _Document(element)


    def addEventListener(self, element, event, callback):
        listener = Listener(element, event, callback)
        l_id = "__pyjamas_listener_%s__" % abs(id(listener))
        self.current_web_frame().addToJavaScriptWindowObject(l_id, listener)
        js = "this.%s=function(e) { window.%s.execute(e); }" % (event, l_id)
        element._element.evaluateJavaScript(js)
        self._listeners.append(listener)

    def _alert(self, txt):
        js = "window.alert('%s');" % (txt)
        doc = self.getDomDocument()
        doc._element.evaluateJavaScript(js)

    def _addWindowEventListener(self, event, callback):
        listener = Listener(self.current_web_frame(), event, callback)
        l_id = "__pyjamas_listener_%s__" % abs(id(listener))
        self.current_web_frame().addToJavaScriptWindowObject(l_id, listener)
        js = "this.%s=function(e) { window.%s.execute(e); }" % (event, l_id)
        doc = self.getDomDocument()
        doc._element.evaluateJavaScript(js)
        self._listeners.append(listener)

    def getUri(self):
        return unicode(self.current_web_frame().baseUrl().toString())

def setup(filename, width=800, height=600):
    global app
    app = QBrowserApp(filename, width, height)

def run():
    global app
    app.app.exec_()
    print "-"*60
    print _current_web_frame().toHtml()

    
    
    
class Listener(QObject):
    
    def __init__(self, element, event, callback):
        QObject.__init__(self)
        self._element = element
        self._event = event
        self._callback = callback

    
    @pyqtSignature("QVariant", result="bool")
    def execute(self, event_data):
        class _Event(unicode):
            pass
        ev = _Event(self._event)
        for k, v in event_data.toPyObject().items():
            if isinstance(v, QString):
                v = unicode(v)
            setattr(ev, unicode(k), v)
        result = self._callback(self._element, ev)
        if result is None:
            return True
        return result

        

