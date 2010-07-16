# Date Time Example
# Copyright (C) 2009 Yit Choong (http://code.google.com/u/yitchoong/)
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>

from Hyperlink import Hyperlink
from pyjamas import Factory
from Image import Image
from pyjamas import DOM
from pyjamas.ui import Event
from pyjamas.ui.MouseListener import MouseHandler


class HyperlinkImage(Hyperlink, MouseHandler):
    def __init__(self, img, **kwargs):
        if not kwargs.has_key('StyleName'):
            kwargs['StyleName'] = 'gwt-HyperlinkImage'
        Hyperlink.__init__(self, **kwargs)
        DOM.appendChild(DOM.getFirstChild(self.getElement()), img.getElement())
        img.unsinkEvents(Event.ONCLICK | Event.MOUSEEVENTS)
        self.sinkEvents(Event.ONCLICK)
        MouseHandler.__init__(self, preventDefault=True)

    def onBrowserEvent(self, event):
        if not MouseHandler.onBrowserEvent(self, event):
            Hyperlink.onBrowserEvent(self, event)

Factory.registerClass('pyjamas.ui.HyperlinkImage', HyperlinkImage)

