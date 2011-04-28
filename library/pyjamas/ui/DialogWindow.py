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
from DialogBox import DialogBox
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


class DialogWindow(DialogBox):
    _props = [
        ("caption", "Caption", "HTML", None),
    ]

    def __init__(self, autoHide=None, modal=True, centered=False,
                 caption=None, minimize=None, maximize=None, close=None,
                 captionStyle=None,
                 **kwargs):
        # Init section
        DialogBox.__init__(self, autoHide, modal, centered, **kwargs)
        self._dialogListeners = []
        self._minimized = None
        self._maximized = None

        # Arguments section
        if isinstance(caption, basestring):
            self.caption.setText(caption)
        elif caption is not None:
            self.caption = caption
            self.caption.addMouseListener(self)
        if captionStyle is not None:
            self.caption.setStyleName(captionStyle)
        else:
            self.caption.addStyleName('WindowCaption')
        self.setControls(minimize, maximize, close)

    def createDefaultControl(self, control_type):
        if control_type == 'minimize':
            return Button("_")
        elif control_type == 'maximize':
            return Button("^")
        elif control_type == 'close':
            return Button("X")
        raise ValueError("Invalid control '%s'" % control_type)

    def setControls(self, minimize, maximize, close):
        if minimize is True:
            self.minimizeWidget = self.createDefaultControl('minimize')
        elif isinstance(minimize, basestring):
            self.minimizeWidget = Image(minimize)
        else:
            self.minimizeWidget = minimize
        if maximize is True:
            self.maximizeWidget = self.createDefaultControl('maximize')
        elif isinstance(maximize, basestring):
            self.maximizeWidget = Image(maximize)
        else:
            self.maximizeWidget = maximize
        if close is True:
            self.closeWidget = self.createDefaultControl('close')
        elif isinstance(close, basestring):
            self.closeWidget = Image(close)
        else:
            self.closeWidget = close
        if (isinstance(self.minimizeWidget, UIObject) or
            isinstance(self.maximizeWidget, UIObject) or
            isinstance(self.closeWidget, UIObject)):
            cf = self.panel.getCellFormatter()
            captionStyle = self.caption.getStyleName()
            captionPanel = FlexTable(
                Width="99%",
                BorderWidth="0",
                CellPadding="0",
                CellSpacing="0",
            )
            controls = HorizontalPanel()
            controls.setStyleName("Controls")
            controls.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)
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
            self.caption.removeStyleName(captionStyle)
            self.panel.setWidget(0, 0, captionPanel)
            captionPanel.setWidget(0, 0, self.caption)
            captionPanel.setWidget(0, 1, controls)
            captionPanel.setStyleName(captionStyle)
            cf = captionPanel.getCellFormatter()
            cf.setWidth(0, 1, '1%')

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

    def onMouseUp(self, sender, x, y):
        if self.dragStartX != x or self.dragStartY != y:
            self.onActivate()
        DialogBox.endDragging(self)

Factory.registerClass('pyjamas.ui.DialogWindow', 'DialogWindow', DialogWindow)
