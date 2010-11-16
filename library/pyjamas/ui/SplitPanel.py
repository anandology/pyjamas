"""
- /*
- * Copyright 2008 Google Inc.
- * Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
- * Copyright (C) 2010 Rich Newpol <rich.newpol@gmail.com>
- *
- * Licensed under the Apache License, Version 2.0 (the "License") you may not
- * use this file except in compliance with the License. You may obtain a copy
- * of the License at
- *
- * http:#www.apache.org/licenses/LICENSE-2.0
- *
- * Unless required by applicable law or agreed to in writing, software
- * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
- * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
- * License for the specific language governing permissions and limitations
- * under the License.
- */
"""

from __pyjamas__ import console
from pyjamas import DOM
from pyjamas import Window
from pyjamas.DeferredCommand import queue_Call
from pyjamas.EventController import EventGenerator
from pyjamas.ui import GlassWidget
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.AbsolutePanel import AbsolutePanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.MouseListener import MouseHandler, fireMouseEvent


class SplitPanelSplitter(SimplePanel, MouseHandler):
    """ a splitter is just a SimplePanel which can receive mouse events """

    def __init__(self, splitPanel, **kwargs):
        # keep a ref to our parent panel for event callback
        self._splitpanel = splitPanel
        SimplePanel.__init__(self, **kwargs)
        MouseHandler.__init__(self)
        self.addMouseListener(self)
        # set some constant styles
        elem = self.getElement()
        # the following allows splitter to be small enough in IE
        DOM.setStyleAttribute(elem, "overflow", "hidden")

    def onMouseDown(self, sender, x, y):
        """ catch a mouse down for parent """

        ev = DOM.eventGetCurrentEvent()
        # ignore right-button downs
        if DOM.eventGetButton(ev) != 1:
            return
        DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
        # parent will capture the mouse and handle the dragging from here
        self._splitpanel.startSplitterDrag(x, y)


class SplitPanel(AbsolutePanel, MouseHandler, EventGenerator):
    """ Provides the SplitPanel baseclass functionality
        A SplitPanel is an AbsolutePanel containing an HTMLTable
        with three cells. The first cell holds the first ScrollPanel,
        while the center cell holds a Splitter, and the last cell
        holds the other ScrollPanel.
    """

    def __init__(self, vertical=False, **kwargs):
        # set defaults
        if not 'StyleName' in kwargs:
            if vertical:    # vertical split panel
                kwargs['StyleName'] = "gwt-VerticalSplitPanel"
            else:
                kwargs['StyleName'] = "gwt-HorizontalSplitPanel"
        # splitter drag state vars
        self._drag_start = None
        self._pos = "50%"
        # orientation
        self._vertical = vertical
        # now init the bases
        AbsolutePanel.__init__(self, **kwargs)
        MouseHandler.__init__(self)
        # add our event support?
        self.addListenedEvent("Resize")
        # create the top/left widget container
        self._container1 = ScrollPanel()
        # create the bottom/right widget container
        self._container2 = ScrollPanel()
        # create the splitter
        self._splitter = SplitPanelSplitter(self)
        # add splitter handling
        self._splitter.addMouseListener(self)
        # add mouse event handling
        self.addMouseListener(self)
        # add the parts
        AbsolutePanel.add(self, self._container1, 0, 0)
        AbsolutePanel.add(self, self._splitter, 0, 0)
        AbsolutePanel.add(self, self._container2, 0, 0)

        # set the layout
        if vertical:    # vertical split panel
            self._splitter.setStyleName("vsplitter")
            self._splitter.setWidth("100%")
            self._container1.setWidth("100%")
            self._container2.setWidth("100%")
            # set drag cursor
            DOM.setStyleAttribute(self._splitter.getElement(),
                                    "cursor", "n-resize")
        else:   # horizontal split panel
            self._splitter.setStyleName("hsplitter")
            self._splitter.setHeight("100%")
            self._container1.setHeight("100%")
            self._container2.setHeight("100%")
            # set drag cursor
            DOM.setStyleAttribute(self._splitter.getElement(),
                                    "cursor", "e-resize")

    def onAttach(self):
        AbsolutePanel.onAttach(self)
        self.setSplitPosition()

    # fixup the container 2 size and position
    def _finalizePositions(self, pos=None):
        finalized = False
        if self._vertical:
            if pos is None:
                pos = self._container1.getOffsetHeight()
            space = self.getOffsetHeight()
            sz = self._splitter.getOffsetHeight()
            if space > 0 and sz > 0 and pos > 0:
                # limit pos
                if pos > space - sz:
                    pos = space - sz
                    self._container1.setHeight(pos)
                self.setWidgetPosition(self._splitter, 0, pos)
                self.setWidgetPosition(self._container2, 0, pos + sz)
                self._container2.setHeight(space - (pos + sz))
                finalized = True
        else:
            if pos is None:
                pos = self._container1.getOffsetWidth()
            space = self.getOffsetWidth()
            sz = self._splitter.getOffsetWidth()
            if space > 0 and sz > 0 and pos > 0:
                # limit pos
                if pos > space - sz:
                    pos = space - sz
                    self._container1.setWidth(pos)
                self.setWidgetPosition(self._splitter, pos, 0)
                self.setWidgetPosition(self._container2, pos + sz, 0)
                self._container2.setWidth(space - (pos + sz))
                finalized = True
        if finalized:
            self.dispatchResizeEvent(self, pos)
        return finalized

    # end a drag operation
    def _stopDragging(self):
        if self._drag_start is not None:
            # we are no longer dragging
            self._drag_start = None
            # deactivate the transparent overlay
            GlassWidget.hide()
            # don't let a mouse-up become a click event
            DOM.eventCancelBubble(DOM.eventGetCurrentEvent(), True)

    def _isDragging(self):
        return self._drag_start is not None

    # start a drag operation (called by splitter)
    def startSplitterDrag(self, x, y):
        if self._drag_start is None:
            # remember where on the slider we are dragging
            if self._vertical:
                self._drag_start = y
            else:
                self._drag_start = x
            # activate the transparent overlay to keep mouse events flowing to
            # the splitter (and to us) even if the mouse leaves the splitter
            GlassWidget.show(self)

    # add handlers for mouse events to support dragging the slider
    # NOTE: the x,y positioni s relative to the splitter
    def onMouseMove(self, sender, x, y):
        # if dragging, then use current mouse position
        #to reset splitter position
        if not self._isDragging():
            return
        # remove the offset into the splitter
        # where we started dragging
        if self._vertical:
            self._pos = y - self._drag_start
        else:
            self._pos = x - self._drag_start
        # apply limit
        if self._pos < 1:
            self._pos = 1
        # apply new position
        self.setSplitPosition()

    def onMouseUp(self, sender, x, y):
        ev = DOM.eventGetCurrentEvent()
        # ignore right-button ups
        if DOM.eventGetButton(ev) != 1:
            return
        DOM.eventPreventDefault(ev)
        # if we are dragging
        if self._isDragging():
            # stop dragging on mouse up
            self._stopDragging()

    # called when we start dragging
    def onMouseGlassEnter(self, sender):
        pass

    # called when we drag out of the window
    # (NOT called when we just stop dragging)
    def onMouseGlassLeave(self, sender):
        # we left the window, so stop dragging
        self._stopDragging()

    #
    # Start the inherited 'public' API
    #

    # specify splitter position in pix OR percentage
    # if pixels (number) specified, we can make change now
    # otherwise, we have to set the offset as specified, then
    # 'fixup' the remaining space after rendering
    def setSplitPosition(self, pos=None):
        if pos is not None:
            # remember last pos set
            self._pos = pos
        else:
            pos = self._pos
        if pos < 1:
            pos = 1
            self._pos = pos
        # change adjustable dimension
        if self._vertical:
            self._container1.setHeight(pos)
        else:
            self._container1.setWidth(pos)
        # if pix are given, we can try to finalize the positions
        finalized = False
        if isinstance(pos, int):
            finalized = self._finalizePositions(pos)
        # if needed, queue callback to finalize
        if not finalized:
            queue_Call(self._finalizePositions)

    def getWidget(self, index):
        if index == 0:
            return self._container1.getWidget()
        return self._container2.getWidget()

    def setWidget(self, index, widget):
        if index == 0:
            return self._container1.setWidget(widget)
        return self._container2.setWidget(widget)

    # Adds a widget to a pane
    def add(self, widget):
        if self.getWidget(0) == None:
            self.setWidget(0, widget)
        elif self.getWidget(1) == None:
            self.setWidget(1, widget)
        else:
            console.error("SimplePanel can only contain one child widget")

    # Removes a child widget.
    def remove(self, widget):
        if self.getWidget(0) == widget:
            self._container1.remove(widget)
        elif self.getWidget(1) == widget:
            self._container2.remove(widget)
        else:
            AbsolutePanel.remove(self, widget)

    # Gets the content element for the given index.
    def getElement(self, index=None):
        if index is None:
            return AbsolutePanel.getElement(self)
        return self.getWidget(index).getElement()

    # Gets the widget in the pane at end of the line direction for the layout
    def getEndOfLineWidget(self):
        return self.getWidget(1)

    # Gets the element that is acting as the splitter.
    def getSplitElement(self):
        return self._splitter.getElement()

    # Gets the widget in the pane at the start of line direction for the layout
    def getStartOfLineWidget(self):
        return self.getWidget(0)

    # Indicates whether the split panel is being resized.
    def isResizing(self):
        return False

    # Sets the widget in the pane at the end of line direction for the layout
    def setEndOfLineWidget(self, widget):
        self.setWidget(1, widget)

    def setStartOfLineWidget(self, widget):
        self.setWidget(0, widget)
