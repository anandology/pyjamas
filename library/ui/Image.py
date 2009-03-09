# Copyright 2006 James Tauber and contributors
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
from pyjamas import DOM

from pyjamas.ui.Widget import Widget
from pyjamas.ui.Event import Event
from pyjamas.ui.MouseListener import MouseListener

global prefetchImages
prefetchImages = {}

class Image(Widget):
    def __init__(self, url=""):
        Widget.__init__(self)
        self.clickListeners = []
        self.loadListeners = []
        self.mouseListeners = []

        self.setElement(DOM.createImg())
        self.sinkEvents(Event.ONCLICK | Event.MOUSEEVENTS | Event.ONLOAD | Event.ONERROR)
        self.setStyleName("gwt-Image")

        if url:
            self.setUrl(url)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addLoadListener(self, listener):
        self.loadListeners.append(listener)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def getUrl(self):
        return DOM.getAttribute(self.getElement(), "src")

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "click":
            for listener in self.clickListeners:
                if listener.onClick: listener.onClick(self, event)
                else: listener(self, event)
        elif type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener.fireMouseEvent(self, self.mouseListeners, self, event)
        elif type == "load":
            for listener in self.loadListeners:
                listener.onLoad(self)
        elif type == "error":
            for listener in self.loadListeners:
                listener.onError(self)

    def prefetch(self, url):
        global prefetchImages

        img = DOM.createImg()
        DOM.setAttribute(img, "src", url)
        prefetchImages[url] = img

    def setUrl(self, url):
        DOM.setAttribute(self.getElement(), "src", url)


