# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009, 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
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

from pyjamas.ui.PopupPanel import PopupPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui import HasHorizontalAlignment
from pyjamas.ui import HasVerticalAlignment
from pyjamas.ui import GlassWidget


class DialogBox(PopupPanel):
    _props = [
        ("caption", "Caption", "HTML", None),
    ]

    def __init__(self, autoHide=None, modal=True, **kwargs):
        # Init section
        self.dragging = False
        self.dragStartX = 0
        self.dragStartY = 0
        self.child = None
        self.panel = FlexTable(
            Height="100%",
            BorderWidth="0",
            CellPadding="0",
            CellSpacing="0",
        )
        cf = self.panel.getCellFormatter()
        cf.setHeight(1, 0, "100%")
        cf.setWidth(1, 0, "100%")
        cf.setAlignment(
            1, 0,
            HasHorizontalAlignment.ALIGN_CENTER,
            HasVerticalAlignment.ALIGN_MIDDLE,
        )

        # Arguments section
        self.modal = modal
        self.caption = HTML()
        self.panel.setWidget(0, 0, self.caption)
        self.caption.setStyleName("Caption")
        self.caption.addMouseListener(self)

        # Finalize
        kwargs['StyleName'] = kwargs.get('StyleName', "gwt-DialogBox")
        PopupPanel.__init__(self, autoHide, modal, **kwargs)
        PopupPanel.setWidget(self, self.panel)

    @classmethod
    def _getProps(self):
        return PopupPanel._getProps() + self._props

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
        GlassWidget.show(self)
        self.dragStartX = x
        self.dragStartY = y

    def onMouseEnter(self, sender):
        pass

    def onMouseLeave(self, sender):
        pass

    def onMouseMove(self, sender, x, y):
        if not self.dragging:
            return
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
        if not self.dragging:
            return
        self.dragging = False
        GlassWidget.hide()

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

    def onWindowResized(self, width, height):
        super(DialogBox, self).onWindowResized(width, height)

    def show(self):
        super(DialogBox, self).show()

Factory.registerClass('gwt.ui.DialogBox', 'DialogBox', DialogBox)
