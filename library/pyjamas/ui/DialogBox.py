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

from pyjamas.ui.UIObject import UIObject
from PopupPanel import PopupPanel
from HTML import HTML
from FlexTable import FlexTable
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui import HasHorizontalAlignment
from pyjamas.ui import HasVerticalAlignment
from pyjamas.ui.Image import Image
from pyjamas.ui.Button import Button
from pyjamas.ui import GlassWidget
from pyjamas.ui import HasAlignment
import pyjamas.Window

# Depends on CSS
#.gwt-DialogBox .Minimize {
#     width: 18px;
#     height: 22px;
#     margin: 0;
#     padding: 0;
#     border: 0;
#     background: transparent url(window_minimize.gif) no-repeat center top;
#     text-indent: -1000em;
#}
# And the same for .Maximize and .Close


class DialogBox(PopupPanel):
    _props = [
        ("caption", "Caption", "HTML", None),
    ]

    def __init__(self, autoHide=None, modal=True, centered=False,
                 caption=None, minimize=None, maximize=None, close=None,
                 captionStyle=None,
                 **kwargs):
        # Init section
        self._dialogListeners = []
        self.dragging = False
        self._minimized = None
        self._maximized = None
        self.closeable = False
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
        self.centered = centered
        if caption is None:
            self.caption = HTML()
        elif isinstance(caption, basestring):
            self.caption = HTML()
            self.caption.setText(caption)
        else:
            self.caption = caption
        self.panel.setWidget(0, 0, self.caption)
        self.caption.setStyleName(captionStyle or "Caption")
        self.caption.addMouseListener(self)
        self.setControls(minimize, maximize, close)

        # Finalize
        kwargs['StyleName'] = kwargs.get('StyleName', "gwt-DialogBox")
        PopupPanel.__init__(self, autoHide, modal, **kwargs)
        PopupPanel.setWidget(self, self.panel)

    @classmethod
    def _getProps(self):
        return PopupPanel._getProps() + self._props

    def setControls(self, minimize, maximize, close):
        if minimize is True:
            self.minimizeWidget = Button("_")
        elif isinstance(minimize, basestring):
            self.minimizeWidget = Image(minimize)
        else:
            self.minimizeWidget = minimize
        if maximize is True:
            self.maximizeWidget = Button("^")
        elif isinstance(maximize, basestring):
            self.maximizeWidget = Image(maximize)
        else:
            self.maximizeWidget = maximize
        if close is True:
            self.closeWidget = Button("X")
        elif isinstance(close, basestring):
            self.closeWidget = Image(close)
        else:
            self.closeWidget = close
        if (
            isinstance(self.minimizeWidget, UIObject) or
            isinstance(self.maximizeWidget, UIObject) or
            isinstance(self.closeWidget, UIObject)
        ):
            cf = self.panel.getCellFormatter()
            captionPanel = FlexTable(
                Height="100%",
                Width="100%",
                BorderWidth="0",
                CellPadding="0",
                CellSpacing="0",
            )
            captionPanel.setStyleName(self.caption.getStyleName())
            controls = HorizontalPanel()
            controls.setStyleName("Controls")
            controls.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)
            cf.setColSpan(1, 0, 2)
            cf.setAlignment(
                0, 1,
                HasAlignment.ALIGN_RIGHT,
                HasAlignment.ALIGN_MIDDLE,
            )
            if isinstance(self.minimizeWidget, UIObject):
                self.minimizeWidget.setStyleName("Minimize")
                controls.add(self.minimizeWidget)
                self.minimizeWidget.addClickListener(
                    getattr(self, "onMinimize"),
                )
            if isinstance(self.maximizeWidget, UIObject):
                self.maximizeWidget.setStyleName("Maximize")
                controls.add(self.maximizeWidget)
                self.maximizeWidget.addClickListener(
                    getattr(self, "onMaximize"),
                )
            if isinstance(self.closeWidget, UIObject):
                self.closeWidget.setStyleName("Close")
                controls.add(self.closeWidget)
                self.closeWidget.addClickListener(
                    getattr(self, "onClose"),
                )
                self.closeable = True
            captionPanel.add(self.caption, 0, 0)
            captionPanel.add(controls, 0, 1)
            cf = captionPanel.getCellFormatter()
            cf.setWidth(0, 0, "100%")
            self.panel.setWidget(0, 0, captionPanel)

    def getDialogListeners(self, listener):
        return self._dialogListeners

    def addDialogListener(self, listener):
        self._dialogListeners.append(listener)

    def removeDialogListener(self, listener):
        self._dialogListeners.remove(listener)

    def _runDialogListener(self, action):
        cont = True
        for listener in self._dialogListeners:
            if hasattr(listener, action):
                if getattr(listener, action)() is False:
                    cont = False
        return cont

    def onActivate(self):
        if self._runDialogListener("onActivate") is False:
            return
        self.hide()
        self.show()

    def _toggleMaximize(self):
        if self._maximized:
            top, left, height, width = self._maximized
            self._maximized = None
            height = width = ""
        else:
            top = self.getPopupTop()
            left = self.getPopupLeft()
            height = self.getHeight()
            width = self.getWidth()
            self._maximized = (top, left, height, width)
            top = left = 0
            height = int(pyjamas.Window.getClientHeight()) - 4
            width = int(pyjamas.Window.getClientWidth()) - 4
        self.setPopupPosition(left, top)
        self.panel.setHeight(height)
        self.panel.setWidth(width)

    def onMaximize(self, sender):
        if self._runDialogListener("onMaximize") is False:
            return
        self._toggleMaximize()
        widget = self.panel.getWidget(1, 0)
        if not widget.isVisible():
            widget.setVisible(True)
        self.hide()
        self.show()

    def onMinimize(self, sender):
        if self._runDialogListener("onMinimize") is False:
            return
        widget = self.child
        if widget is not None:
            if widget.isVisible():
                widget.setVisible(False)
                self.setHeight("")
                self.setWidth("")
                if self._maximized:
                    self._minimized = self._maximized
                    self._toggleMaximize()
                else:
                    self._minimized = None
            else:
                if self._minimized is not None:
                    self._toggleMaximize()
                widget.setVisible(True)

    def onClose(self, sender):
        if self._runDialogListener("onClose") is False:
            return
        self.hide()

    def setCloseable(self, closeable):
        """ Note: only use this to set closeable to True,
            and do not attempt to set closeable to False:
            it won't work.
            This is deprecated. Use setControls instead.
        """
        if isinstance(self.closeWidget, UIObject) or not closeable:
            return
        self.setControls(
            self.minimizeWidget,
            self.maximizeWidget,
            "window_close.gif",
        )

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
        if self.dragStartX != x and self.dragStartY != y:
            self.onActivate()
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
        if self.centered:
            self.centerBox()

    def show(self):
        super(DialogBox, self).show()
        if self.centered:
            self.centerBox()

Factory.registerClass('pyjamas.ui.DialogBox', 'DialogBox', DialogBox)
