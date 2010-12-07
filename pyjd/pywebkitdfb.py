#!/usr/bin/env python
# Copyright (C) 2006, Red Hat, Inc.
# Copyright (C) 2007, One Laptop Per Child
# Copyright (C) 2007 Jan Alonzo <jmalonzo@unpluggable.com>
# Copyright (C) 2008, 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
    pyjd.py is the loader for Pyjamas-Desktop applications.

    It takes as the first argument either the python module containing a class
    named after the module, with an onModuleLoad() function, or an HTML page
    containing one or more <meta name="pygwt:module" content="modulename" />
    tags.

    This is an example Hello.py module (which you would load with
    pyjd.py Hello.py):

        from pyjamas.ui import RootPanel, Button
        class Hello:
            def onModuleLoad(self):
                RootPanel().add(Button("Hello world"))

    This is an example HTML file which will load the above example
    (which you would load with pyjd.py Hello.html, and the application
     Hello.py will be automatically located, through the <meta /> tag):

        <html>
            <head> <meta name="pygwt:module" content="Hello" /> </head>
            <body />
        </html>

    pyjd.py will create a basic template HTML, based on the name of your
    application if you do not provide one, in order to load the application.
    The basic template does not contain any HTML, or any links to CSS
    stylesheets, and so your application will have to add everything,
    manually, by manipulating the DOM model.  The basic template does,
    however, include a "History" frame, which is essential for the Pyjamas
    History module to function correctly.

    You may find using an HTML page, even to just add a CSS stylesheet
    (in the usual way - <link rel='stylesheet' href='./Hello.css' /> or
    other location, even href="http://foo.org/style.css") to be more
    convenient.

    pyjd.py also takes a second argument (which the author has found
    to be convenient) which can be used to specify an alternative
    "root" location for loading of content from any "relative" URLs
    in your DOM document.  for example, equivalent to images with
    <img src="./images/test.png" />.  the author has found this to
    be convenient when running pyjamas applications
    http://code.google.com/p/pyjamas), which store the static content
    in a directory called "public".  Specifying this directory as the
    second argument to pyjd.py allows the same application being
    developed with Pyjamas to also be tested under Pyjamas-Desktop.

    However, you may find that you need to write a separate short
    http page for your Pyjamas-Desktop app, which is an identical
    copy of your Pyjamas HTML page in every respect but making
    absolutely sure that you remove the javascript "pygwt.js" script.
    You will still need to place the page on your Web Server,
    and then load it with pyjs.py as follows:

        pyjs.py http://127.0.0.1/jsonrpc/output/test.html

    This will ensure that pyjs.py - more specifically Webkit - knows
    the correct location for all relative URLS (of the form
    href="./images", stylesheet links, img src= references etc.)

    If you do not remove the "pygwt.js" script from the copy of
    the http loader page, pyjs.py, being effectively a web browser
    in its own right thanks to Webkit, will successfully run your
    Pyjamas-compiled application!  Unfortunately, however, the
    loader will also be activated, and you will end up running
    two conflicting versions of your application - one javascript
    based and one python based - simultaneously.  It's probably
    best to avoid this scenario.

    pyjd.py is based on the PyWebkitGTK "demobrowser.py".
"""

import os
import new
import sys
import time
from traceback import print_stack, print_exc

import webkitdfb as pywebkit

def module_load(m):
    minst = None
    exec """\
from %(mod)s import %(mod)s
minst = %(mod)s()
""" % ({'mod': m})
    return minst


class Callback:
    def __init__(self, sender, cb, boolparam):
        self.sender = sender
        self.cb = cb
        self.boolparam = boolparam
    def _callback(self, event):
        #print "callback", self.sender, self.cb
        try:
            return self.cb(self.sender, event, self.boolparam)
        except:
            print_exc()
            return None

class Browser:
    def __init__(self, application, appdir=None, width=800, height=600):

        self.already_initialised = False

        self._loading = False

        self.width = width
        self.height = height
        self.application = application
        self.appdir = appdir

    def load_app(self):

        uri = self.application
        if uri.find("://") == -1:
            # assume file
            uri = 'file://'+os.path.abspath(uri)

        self._browser = pywebkit.WebView(self.width, self.height, uri)
        self._browser.SetDocumentLoadedCallback(self._loading_stop_cb)

    def getUri(self):
        return self.application

    def init_app(self):
        # TODO: ideally, this should be done by hooking body with an "onLoad".

        from __pyjamas__ import pygwt_processMetas, set_main_frame
        from __pyjamas__ import set_gtk_module
        set_gtk_module(None)

        #main_frame = self._browser.get_main_frame()
        main_frame = self
        main_frame._callbacks = []
        #main_frame.gobject_wrap = pywebkit.gobject_wrap
        main_frame.platform = 'webkit'
        set_main_frame(main_frame)

        #for m in pygwt_processMetas():
        #    minst = module_load(m)
        #    minst.onModuleLoad()

    def _loading_stop_cb(self):
        # FIXME: another frame may still be loading?

        if self.already_initialised:
            return
        self.already_initialised = True
        self.init_app()

    def mash_attrib(self, name, joiner='-'):
        return name

    def _alert(self, msg):
        print "alert:", msg

    def getDomWindow(self):
        return self._browser.GetDomWindow()

    def getDomDocument(self):
        return self._browser.GetDomDocument()

    def getXmlHttpRequest(self):
        return self._browser.GetXMLHttpRequest()

    def _addWindowEventListener(self, event_name, cb):
        cb = Callback(self, cb, True)
        setattr(self._browser.GetDomWindow(), "on%s" % event_name, cb._callback)

    def _addXMLHttpRequestEventListener(self, element, event_name, cb):
        #print "add XMLHttpRequest", element, event_name, cb
        cb = Callback(element, cb, True)
        setattr(element, "on%s" % event_name, cb._callback)
        #return element.addEventListener(event_name, cb._callback, True)

    def _addEventListener(self, element, event_name, cb):
        #    element._callbacks.append(cb)
        cb = Callback(element, cb, True)
        #print "addEventListener", element, event_name, cb
        setattr(element, "on%s" % event_name, cb._callback)


def setup(application, appdir=None, width=800, height=600):

    global wv

    wv = Browser(application, appdir, width, height)
    wv.load_app()

    while 1:
        if is_loaded():
            return
        run(one_event=True)

def is_loaded():
    return wv.already_initialised

def run(one_event=False, block=True):
    if one_event:
        if block: #or gtk.events_pending():
            pywebkit.loop()
            sys.stdout.flush()
        return True #gtk.events_pending()
    else:
        while 1:
            pywebkit.loop()
            sys.stdout.flush()


