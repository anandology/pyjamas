# Copyright (C) 2010 Jim Washington
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

import time
from __pyjamas__ import wnd, doc
from pyjamas import DOM
from pyjamas.ui import GlassWidget
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui import Event
from pyjamas.Timer import Timer
from pyjamas.dnd.utils import DraggingWidget, isCanceled, \
     cloneElement, findDraggable, eventCoordinates, \
     getElementUnderMouse
from pyjamas.dnd.DataTransfer import DataTransfer, DragDataStore
from pyjamas.dnd.DragEvent import DragEvent
from pyjamas.dnd import READ_ONLY, READ_WRITE, PROTECTED

ACTIVELY_DRAGGING = 3
DRAGGING_NO_MOVEMENT_YET = 2
NOT_DRAGGING = 1

class DNDHelper(object):
    """
    DNDHelper is a singleton drag and drop agent.

    It acts as dragging/dropping agent for platforms that do not support html5
    drag and drop.
    """

    def __init__(self):
        self.dropTargets = []
        self.dragging = NOT_DRAGGING
        self.dragBusy = False
        self._currentTargetElement = None
        self.previousDropTarget = None
        self.draggingImage = None
        self.origMouseX = 0
        self.origMouseY = 0
        self.currentDragOperation = 'none'
        self.data = None
        self.returnTimer = Timer(notify=self.onReturningWidget)
        self.mouseEvent = None
        self.dragDataStore = None

    def setCurrentTargetElement(self, element):
        if self._currentTargetElement is not None:
            if not DOM.compare(self._currentTargetElement, element):
#                leave_event = self.makeDragEvent(self.mouseEvent, 'dragleave',
#                                                self.currentTargetElement)
                self.fireDNDEvent('dragleave', self.currentTargetElement,
                                  self.currentDropWidget)
#                self.currentDropWidget.onDragLeave(leave_event)
#                self.finalize(leave_event)
        self._currentTargetElement = element

    def getCurrentTargetElement(self):
        return self._currentTargetElement

    currentTargetElement = property(getCurrentTargetElement,
                                    setCurrentTargetElement)

    def getElement(self):
        """
        ie6 GlassWidget impl needs this
        """
        return self.dragWidget.getElement()

    def updateDropEffect(self, dataTransfer, event_type):
        """
        http://dev.w3.org/html5/spec/dnd.html#dragevent
        """
        # default for dragstart, drag, dragleave
        dropEffect='none'

        if event_type in ['dragover', 'dragenter']:
            ea = dataTransfer.getEffectAllowed()
            if ea == 'none':
                dropEffect = 'none'
            elif ea.startswith('copy') or ea == 'all':
                dropEffect = 'copy'
            elif ea.startswith('link'):
                dropEffect = 'link'
            elif ea == 'move':
                dropEffect = 'move'
            else:
                dropEffect = 'copy'
        elif event_type in ['drop', 'dragend']:
            dropEffect = self.currentDragOperation
        dataTransfer.dropEffect = dropEffect

    def updateDragOperation(self, event):
        """
        http://dev.w3.org/html5/spec/dnd.html
        """
        dataTransfer = event.dataTransfer
        ea = dataTransfer.effectAllowed
        de = dataTransfer.dropEffect
        if (de == 'copy' and ea in
            ['uninitialized', 'copy','copyLink', 'copyMove', 'all']):
            self.currentDragOperation = 'copy'
        elif (de == 'link' and ea in
            ['uninitialized', 'link', 'copyLink', 'linkMove', 'all']):
                self.currentDragOperation = 'link'
        elif (de == 'move' and ea in
              ['uninitialized', 'move', 'copyMove', 'linkMove', 'all']):
                self.currentDragOperation = 'move'
        else:
            self.currentDragOperation = 'none'

    def updateAllowedEffects(self, drag_event):
        dt = drag_event.dataTransfer
        self.dragDataStore.allowed_effects_state = dt.effectAllowed

    def registerTarget(self, target):
        """
        Rather than searching the entire document for drop target widgets and
        maybe drop targets within widgets, this implementation holds a list of
        widgets and searches only within this list for potential drop targets.
        """
        if not target in self.dropTargets:
            self.dropTargets.append(target)

    def unregisterTarget(self, target):
        """
        I dont know why, but a widget may no longer want to be registered
        as a drop target.
        """
        while target in self.dropTargets:
            self.dropTargets.remove(target)


    def setDragImage(self, element, x, y):
        self.dragLeftOffset = x
        self.dragTopOffset = y
        if element.tagName.lower().endswith('img'):
            src = DOM.getAttribute(element,'src')
            element = DOM.createElement('img')
            DOM.setAttribute(element, 'src', src)
        if not self.draggingImage:
            self.createDraggingImage(element)
        else:
            self.draggingImage.setImage(element)

    def addFeedbackElement(self, element):
        """
        This is called from DataTransfer
        """
        if self.draggingImage:
            self.draggingImage.addElement(element)
        else:
            self.createDraggingImage(element)

    def createDraggingImage(self, element):
        self.draggingImage = DraggingWidget(element)
        return self.draggingImage

    def setDragImageLocation(self, x, y):
        """
        Move the dragging image around.
        """
        elt_top = y - self.dragTopOffset
        elt_left = x - self.dragLeftOffset

        self.draggingImage.setStyleAttribute('top', elt_top )
        self.draggingImage.setStyleAttribute('left', elt_left)

    def getAbsoluteLeft(self):
        """
        GlassWidget wants this
        """
        return self.dragWidget.getAbsoluteLeft()

    def getAbsoluteTop(self):
        """
        GlassWidget wants this
        """
        return self.dragWidget.getAbsoluteTop()

    def makeDragEvent(self, event, type, target=None):
        dt = DataTransfer(self.dragDataStore)
        self.updateDropEffect(dt, type)
        drag_event = DragEvent(event, type, dt, target)
        return drag_event

    def finalize(self, event):
        self.dragDataStore.allowed_effects_state = \
        event.dataTransfer.effectAllowed
        if event.type in ['dragstart', 'drop']:
            self.dragDataStore.setMode(PROTECTED)
        event.dataTransfer.dataStore = None

    def fireDNDEvent(self, name, target, widget):
        if name == 'dragstart':
            self.dragDataStore.setMode(READ_WRITE)
        elif name == 'drop':
            self.dragDataStore.setMode(READ_ONLY)
        event = self.makeDragEvent(self.mouseEvent, name, target)

        if name == 'dragstart':
            widget.onDragStart(event)
        elif name == 'dragover':
            widget.onDragOver(event)
        elif name == 'drag':
            widget.onDrag(event)
        elif name == 'dragend':
            widget.onDragEnd(event)
        elif name == 'drop':
            widget.onDrop(event)
        elif name == 'dragleave':
            widget.onDragLeave(event)
        elif name == 'dragenter':
            widget.onDragEnter(event)
        self.finalize(event)
        return event

    def initFeedbackImage(self):
        ds = self.dragDataStore
        x = 0
        y = 0
        if ds.bitmap is not None:
            if ds.hotspot_coordinate is not None:
                offset = ds.hotspot_coordinate
                x = offset[0]
                y = offset[1]
            self.setDragImage(ds.bitmap, x, y)
            return
        if self.dragDataStore.elements:
            for element in self.dragDataStore.elements:
                self.addFeedbackElement(element)


    def onMouseMove(self, sender, x, y):
        event = DOM.eventGetCurrentEvent()
        self.mouseEvent = event
        button = DOM.eventGetButton(event)
        if not button == Event.BUTTON_LEFT:
            return
## The following commented code lets the native dnd happen in IE. sucks.
## But it may enable dragging our widgets out of IE into other apps.
#        else:
#            try:
#                self.dragWidget.getElement().dragDrop()
#                return
#            except:
#                pass

        # Adjust x and y to absolute coordinates.
        x, y = eventCoordinates(event)

        if self.dragging == DRAGGING_NO_MOVEMENT_YET:
            self.currentDragOperation = 'none'
            fromElement = self.dragWidget.getElement()
            # Is the widget itself draggable?
            try:
                draggable = fromElement.draggable
            except:
                draggable = False
            # if not, find the draggable element at (x, y) in the widget
            if not draggable:
                fromElement = findDraggable(sender.getElement(),
                    self.origMouseX, self.origMouseY)
            # Nothing draggable found. return.
            if fromElement is None:
                self.dragging = NOT_DRAGGING
                return
            # Get the location for the dragging widget
            self.origTop = DOM.getAbsoluteTop(fromElement)
            self.origLeft = DOM.getAbsoluteLeft(fromElement)
            self.dragLeftOffset = self.origMouseX - self.origLeft
            self.dragTopOffset = self.origMouseY - self.origTop
#            self.setDragImage(fromElement,
#                             self.origMouseX - self.origLeft,
#                             self.origMouseY - self.origTop)
            self.dragDataStore.elements = [fromElement]
            dragStartEvent = self.fireDNDEvent('dragstart', None,
                                               self.dragWidget)
            if not isCanceled(dragStartEvent):
                self.initFeedbackImage()
                RootPanel().add(self.draggingImage)
                self.setDragImageLocation(x, y)
                self.dragging = ACTIVELY_DRAGGING
                GlassWidget.show(self)
        elif self.dragging == ACTIVELY_DRAGGING:
            try:
                doc().selection.empty()
            except:
                wnd().getSelection().removeAllRanges()

            self.setDragImageLocation(x, y)

            # If we are still working on the previous iteration, or if we have
            # done this recently, we'll wait for the next event.
            if self.dragBusy or time.time() - self.drag_time < 0.25:
                return

            self.doDrag(event, x, y)
            self.drag_time = time.time()



    def doDrag(self, event, x, y):
        self.dragBusy = True
        #self.dragDataStore.dropEffect = 'none'
        drag_event = self.fireDNDEvent('drag', None, self.dragWidget)
        # drag event was not canceled
        if not isCanceled(drag_event):
            target = None
            widget = None
            # Find the most specific element under the cursor and the widget
            # with the drop listener for it.
            for widget in self.dropTargets:
                target = getElementUnderMouse(widget, x, y)
                if target is not None:
                    break
            if target:
                drop_widget = widget
                drop_element = target
                if (not self.currentTargetElement or
                    not DOM.compare(drop_element, self.currentTargetElement)):
#                    enter_event = self.makeDragEvent(event,'dragenter',
#                                                     drop_element)
                    enter_event = self.fireDNDEvent('dragenter', drop_element,
                                                    drop_widget)
#                    drop_widget.onDragEnter(enter_event)
#                    self.finalize(enter_event)
                    if isCanceled(enter_event):
                        self.currentTargetElement = drop_element
                        self.currentDropWidget = drop_widget

                if self.currentTargetElement is not None:
                    # disable dropping if over event is not canceled
#                    over_event = self.makeDragEvent(event, 'dragover',
#                                                    drop_element)
                    over_event = self.fireDNDEvent('dragover', drop_element,
                                self.currentDropWidget)
#                    self.currentDropWidget.onDragOver(over_event)
#                    self.finalize(over_event)
                    if isCanceled(over_event):
                        self.updateDragOperation(over_event)
                    else:
                        self.currentDragOperation = 'none'
                    self.draggingImage.updateCursor(self.currentDragOperation)
            else:
                self.currentTargetElement = None

        else:
            self.currentDragOperation = 'none'
        self.dragBusy = False

    def onMouseDown(self, sender, x, y):
        self.dragWidget = sender
        event = DOM.eventGetCurrentEvent()
        self.mouseEvent = event
        button = DOM.eventGetButton(event)
        if button != Event.BUTTON_LEFT:
            return
        x, y = eventCoordinates(event)
        self.origMouseX = x
        self.origMouseY = y
        self.dragging = DRAGGING_NO_MOVEMENT_YET
        self.drag_time = time.time()
        self.dragDataStore = DragDataStore()

    def onMouseUp(self, sender, x, y):
#        event = DOM.eventGetCurrentEvent()
        self.dragging = NOT_DRAGGING
        if self.draggingImage:
            GlassWidget.hide()
            if (self.currentDragOperation == 'none'
                    or not self.currentTargetElement):
                if self.currentTargetElement:
#                    leave_event = self.makeDragEvent(event, 'dragleave',
#                        self.currentTargetElement)
                    self.fireDNDEvent('dragleave', self.currentTargetElement,
                                      self.currentDropWidget)
#                    self.currentDropWidget.onDragLeave(leave_event)
#                    self.finalize(leave_event)
                self.returnDrag()
            else:
#                self.dragDataStore.mode = READ_ONLY
#                drop_event = self.makeDragEvent(event, 'drop',
#                    self.currentTargetElement)
                drop_event = self.fireDNDEvent('drop', self.currentTargetElement,
                                  self.currentDropWidget)
                self.dropEffect = self.currentDragOperation
#                self.currentDropWidget.onDrop(drop_event)
#                self.finalize(drop_event)
                if isCanceled(drop_event):
                    self.currentDragOperation = self.dropEffect
                else:
                    self.currentDragOperation = 'none'
                self.zapDragImage()
                self.fireDNDEvent('dragend', None, self.dragWidget)
#                dragEnd_event = self.makeDragEvent(event, 'dragend')
                self.dropEffect = self.currentDragOperation
#                self.dragWidget.onDragEnd(dragEnd_event)
#                self.finalize(dragEnd_event)

    def zapDragImage(self):
        RootPanel().remove(self.draggingImage)
        self.draggingImage = None

    def returnDrag(self):
        self.moveItemTo(self.draggingImage,self.origLeft, self.origTop)

    def returnXY(self, start, destination, count):
        start_x, start_y = start
        destination_x, destination_y = destination
        diff_x = (start_x - destination_x) / count
        diff_y = (start_y - destination_y) / count
        while (abs(start_x - destination_x) > 10
               or abs(start_y - destination_y) > 10):
            start_x -= diff_x
            start_y -= diff_y
            yield start_x, start_y
        raise StopIteration

    def onReturningWidget(self):
        try:
            next_loc = self.return_iterator.next()
        except StopIteration:
            self.zapDragImage()
            return
        x, y = next_loc
        self.draggingImage.setStyleAttribute('top', str(y))
        self.draggingImage.setStyleAttribute('left', str(x))
        self.returnTimer.schedule(50)

    def moveItemTo(self, widget, x, y):
        self.returnWidget = widget
        returnWidgetDestination = x, y
        widgetStart = widget.getAbsoluteLeft(), widget.getAbsoluteTop()
        self.return_iterator = self.returnXY(widgetStart,
                        returnWidgetDestination, 10)
        self.returnTimer.schedule(50)

    def onMouseEnter(self, sender):
        pass

    def onMouseLeave(self, sender):
        if self.dragging == DRAGGING_NO_MOVEMENT_YET:
            self.dragging = NOT_DRAGGING

    def onMouseGlassEnter(self, sender):
         pass

    def onMouseGlassLeave(self, sender):
         pass

dndHelper = None

def initDNDHelper():
    global dndHelper
    if dndHelper is None:
        dndHelper = DNDHelper()

initDNDHelper()




