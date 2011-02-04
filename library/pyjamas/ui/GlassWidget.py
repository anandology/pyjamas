# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
# Copyright (C) 2010 Serge Tarkovski <serge.tarkovski@gmail.com>
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
import pyjd
from pyjamas import DOM
from pyjamas import Window
from pyjamas import Factory
from __pyjamas__ import JS, doc
from SimplePanel import SimplePanel
from Widget import Widget
from MouseListener import MouseHandler
from RootPanel import RootPanel

mousecapturer = None


def getMouseCapturer(**kwargs):
    global mousecapturer
    if mousecapturer is None:
        mousecapturer = GlassWidget(**kwargs)
    # if mousecapturer has been overloaded with something
    # other than a GlassWidget (as in IE override)
    # just return None
    elif not isinstance(mousecapturer, GlassWidget):
        return None
    return mousecapturer


def show(mousetarget, **kwargs):
    global mousecapturer
    mc = getMouseCapturer(**kwargs)
    mc.mousetarget = mousetarget
    if isinstance(mousetarget, MouseHandler):
        mc.mousehandler = True
    mc.show()


def hide():
    global mousecapturer
    mousecapturer.hide()


class GlassWidget(Widget, MouseHandler):
    def __init__(self, **kwargs):

        self.glassListeners = []
        self.showing = False
        self.mousehandler = False

        if not 'StyleName' in kwargs:
            kwargs['StyleName'] = "gwt-GlassWidget"

        if 'Element' in kwargs:
            element = kwargs.pop('Element')
        else:
            element = DOM.createDiv()

        self.setElement(element)
        Widget.__init__(self, **kwargs)
        MouseHandler.__init__(self)
        self.setzIndex(1000000)
        self.addMouseListener(self)

    def addGlassListener(self, listener):
        self.glassListeners.append(listener)

    def hide(self, autoClosed=False):
        self.showing = False

        self.hideGlass()

        DOM.removeEventPreview(self)

        RootPanel().remove(self)
        self.onHideImpl(self.getElement())
        DOM.releaseCapture(self.getElement())
        for listener in self.glassListeners:
            if hasattr(listener, 'onGlassHide'):
                listener.onGlassHide(self, autoClosed)
            else:
                listener(self, autoClosed)

    def _event_targets_popup(self, event):
        target = DOM.eventGetTarget(event)
        return target and DOM.isOrHasChild(self.getElement(), target)

    def onEventPreview(self, event):
        etype = DOM.eventGetType(event)
        if etype == "mousedown" or etype == "blur":
            if DOM.getCaptureElement() is not None:
                return True
        elif etype == "mouseup" or etype == "click" or \
             etype == "mousemove" or etype == "dblclick":
            if DOM.getCaptureElement() is not None:
                return True
        return self._event_targets_popup(event)

    def onHideImpl(self, popup):
        pass

    def onShowImpl(self, popup):
        pass

    def removeGlassListener(self, listener):
        self.glassListeners.remove(listener)

    def setGlassPosition(self):
        top = Window.getScrollTop()
        left = Window.getScrollLeft()
        height = Window.getClientHeight()
        width = Window.getClientWidth()
        el = self.getElement()
        DOM.setStyleAttribute(el, "position", "absolute")
        DOM.setStyleAttribute(el, "left",
                                  "%s" % left if left == 0 else "%spx" % left)
        DOM.setStyleAttribute(el, "top",
                                  "%s" % top if top == 0 else "%spx" % top)
        DOM.setStyleAttribute(el, "height", "%spx" % (top + height))
        DOM.setStyleAttribute(el, "width", "%spx" % (left + width))
        # under pyjd glasswidget cannot be transparent,
        # otherwise it drops the mousecapture, so we have
        # to give it a 1% opaque background color
        if pyjd.is_desktop:
            # pyjd uses IE style opacity
            DOM.setStyleAttribute(el, "filter", "alpha(opacity=1)")
            # this is the Moz form of transparency
            DOM.setStyleAttribute(el, "background", "rgba(255,255,255,0.1)")

    def showGlass(self):
        Window.enableScrolling(False)
        self.setGlassPosition()
        doc().body.appendChild(self.getElement())
        Window.addWindowResizeListener(self)

    def hideGlass(self):
        Window.removeWindowResizeListener(self)
        doc().body.removeChild(self.getElement())
        Window.enableScrolling(True)

    def onWindowResized(self, width, height):
        self.setGlassPosition()

    def show(self):
        if self.showing:
            return

        self.showing = True

        self.showGlass()

        DOM.addEventPreview(self)

        RootPanel().add(self)
        self.onShowImpl(self.getElement())
        DOM.setCapture(self.getElement())

    def adjustMousePos(self, x, y):
        x += self.getAbsoluteLeft() - self.mousetarget.getAbsoluteLeft()
        y += self.getAbsoluteTop() - self.mousetarget.getAbsoluteTop()
        return x, y

    def onMouseDown(self, sender, x, y):
        x, y = self.adjustMousePos(x, y)
        if self.mousehandler:
            self.mousetarget.onBrowserEvent(DOM.eventGetCurrentEvent())
        else:
            self.mousetarget.onMouseDown(sender, x, y)

    def onMouseEnter(self, sender):
        self.mousetarget.onMouseGlassEnter(sender)

    def onMouseLeave(self, sender):
        self.mousetarget.onMouseGlassLeave(sender)

    def onMouseMove(self, sender, x, y):
        x, y = self.adjustMousePos(x, y)
        if self.mousehandler:
            self.mousetarget.onBrowserEvent(DOM.eventGetCurrentEvent())
        else:
            self.mousetarget.onMouseMove(sender, x, y)

    def onMouseUp(self, sender, x, y):
        x, y = self.adjustMousePos(x, y)
        if self.mousehandler:
            self.mousetarget.onBrowserEvent(DOM.eventGetCurrentEvent())
        else:
            self.mousetarget.onMouseUp(sender, x, y)


Factory.registerClass('pyjamas.ui.GlassWidget', 'GlassWidget', GlassWidget)
