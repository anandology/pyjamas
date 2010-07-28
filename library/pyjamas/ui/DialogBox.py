# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
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
from pyjamas import Factory

from PopupPanel import PopupPanel
from HTML import HTML
from FlexTable import FlexTable
from pyjamas.ui import HasHorizontalAlignment
from pyjamas.ui import HasVerticalAlignment
from pyjamas.ui.Image import Image
from pyjamas.ui.GlassWidget import GlassWidget

from pyjamas import Window

class DialogBox(PopupPanel):
    def __init__(self, autoHide=None, modal=True, centered=False,
                       **kwargs):

        self.caption = HTML()
        self.child = None
        self.dragging = False
        self.gw = GlassWidget(self)
        self.dragStartX = 0
        self.dragStartY = 0
        self.panel = FlexTable(Height="100%", BorderWidth="0",
                                CellPadding="0", CellSpacing="0")
        self.panel.setWidget(0, 0, self.caption)
        cf = self.panel.getCellFormatter()
        cf.setHeight(1, 0, "100%")
        cf.setWidth(1, 0, "100%")
        cf.setAlignment(1, 0,
                        HasHorizontalAlignment.ALIGN_CENTER,
                        HasVerticalAlignment.ALIGN_MIDDLE)

        self.caption.setStyleName("Caption")
        self.caption.addMouseListener(self)

        self.centered = centered

        self.closeable = False

        kwargs['StyleName'] = kwargs.get('StyleName', "gwt-DialogBox")
        PopupPanel.__init__(self, autoHide, modal, **kwargs)
        PopupPanel.setWidget(self, self.panel)

    def _closeClicked(self, sender):
        self.hide()

    def setCloseable(self, closeable):
        """ Note: only use this to set closeable to True,
            and do not attempt to set closeable to False:
            it won't work.
        """
        if self.closeable or not closeable:
            return

        closeButton = Image("window_close.gif")
        closeButton.setStyleName("Caption closeBtn")
        closeButton.addClickListener(getattr(self, "_closeClicked"))
        self.panel.setWidget(0, 1, closeButton)
        self.panel.getFlexCellFormatter().setColSpan(1, 0, 2)
        cf = self.panel.getCellFormatter()
        cf.setWidth(0, 1, "16px")
        cf.setAlignment(0, 1,
                        HasHorizontalAlignment.ALIGN_RIGHT,
                        HasVerticalAlignment.ALIGN_MIDDLE)
        self.closeable = True

    def onEventPreview(self, event):
        # preventDefault on mousedown events, outside of the
        # dialog, to stop text-selection on dragging
        type = DOM.eventGetType(event)
        if type == 'mousedown':
            target = DOM.eventGetTarget(event)
            elem = self.caption.getElement()
            event_targets_popup = target and DOM.isOrHasChild(elem, target)
            if event_targets_popup:
                DOM.eventPreventDefault(event)
        return PopupPanel.onEventPreview(self, event)

    def getHTML(self):
        return self.caption.getHTML()

    def getText(self):
        return self.caption.getText()

    def setHTML(self, html):
        self.caption.setHTML(html)

    def setText(self, text):
        self.caption.setText(text)

    def onMouseDown(self, sender, x, y):
        self.dragging = True
        DOM.setCapture(self.gw.getElement())
        self.gw.show()
        self.dragStartX = x
        self.dragStartY = y

    def onMouseEnter(self, sender):
        pass

    def onMouseLeave(self, sender):
        pass

    def onMouseMove(self, sender, x, y):
        if self.dragging:
            absX = x + self.getAbsoluteLeft()
            absY = y + self.getAbsoluteTop()
            self.setPopupPosition(absX - self.dragStartX,
                                  absY - self.dragStartY)

    def onMouseUp(self, sender, x, y):
        self.endDragging()

    def onMouseGlassEnter(self, sender):
        pass

    def onMouseGlassLeave(self, sender):
        self.endDragging()

    def endDragging(self):
        self.dragging = False
        DOM.releaseCapture(self.gw.getElement())
        self.gw.hide()

    def remove(self, widget):
        if self.child != widget:
            return False

        self.panel.remove(widget)
        self.child = None
        return True

    def doAttachChildren(self):
        PopupPanel.doAttachChildren(self)
        self.caption.onAttach()

    def doDetachChildren(self):
        PopupPanel.doDetachChildren(self)
        self.caption.onDetach()

    def setWidget(self, widget):
        if self.child is not None:
            self.panel.remove(self.child)

        if widget is not None:
            self.panel.setWidget(1, 0, widget)

        self.child = widget

    def centerBox(self):
        self_width = self.getOffsetWidth()
        self_height = self.getOffsetHeight()

        height = Window.getClientHeight()
        width = Window.getClientWidth()

        center_x = int(width) / 2
        center_y = int(height) / 2

        self_top  = center_y - (int(self_height) / 2)
        self_left = center_x - (int(self_width)  / 2)

        self.setPopupPosition(self_left, self_top)

    def onWindowResized(self, width, height):
        super(DialogBox, self).onWindowResized(width, height)
        if self.centered:
            self.centerBox()

    def show(self):
        super(DialogBox, self).show()
        if self.centered:
            self.centerBox()

Factory.registerClass('pyjamas.ui.DialogBox', DialogBox)

