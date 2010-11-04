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
from __pyjamas__ import doc, wnd
from pyjamas import DOM
from pyjamas.ui import GlassWidget
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui import Event
from pyjamas.ui.Widget import Widget
from pyjamas.Timer import Timer

ACTIVELY_DRAGGING = 3
DRAGGING_NO_MOVEMENT_YET = 2
NOT_DRAGGING = 1

def isIn(element, x, y):
    """
    Given an element and an absolute x and y, return True if the
    (x,y) coordinate is within the element. Otherwise, return False.
    """
    top = DOM.getAbsoluteTop(element)
    height = DOM.getIntAttribute(element, 'offsetHeight')
    if y >= top and y <= top + height:
        left = DOM.getAbsoluteLeft(element)
        width = DOM.getIntAttribute(element, 'offsetWidth')
        if x >= left and x <= left + width:
            return True
    return False


def isCanceled(event):
    """
    Has the DragEvent been canceled?
    Coding this module was much easier with this function.
    """
    return not(event.returnValue)

def findDraggable(element, x, y):
    """
    Find the element within a widget's main element that is
    draggable and under the mouse cursor. We need this for event delegation.

    """
    for elt in DOM.IterWalkChildren(element):
        try:
            draggable = elt.draggable
        except:
            draggable = False
        if draggable:
            if isIn(elt, x, y):
                return elt
    return None

def getComputedStyle(element, style=None):
    """
    Get computed style of an element, like in
    http://efreedom.com/Question/1-1848445/Duplicating-Element-Style-JavaScript
    """
    try:
        # ie
        element_style = element.currentStyle
    except:
        element_style = doc().defaultView.getComputedStyle(element, None)
    if style:
        return element_style[style]
    return element_style

def copyStyles(elem1, elem2):
    """
    Copy styles from one element to another, like in
    http://efreedom.com/Question/1-1848445/Duplicating-Element-Style-JavaScript
    """
    element_style = dict(getComputedStyle(elem1))
    for style in element_style:
        try:
            value = element_style[style]
            if isinstance(value, str):
                if not style == 'cssText':
                    DOM.setStyleAttribute(elem2, style, value)
        except:
            raise ValueError("not allowed: %s" % style)

def getTargetInChildren(element, x, y):
    """
    x and y are absolute coordinates within the document.
    Return the last child of element that contains (x,y).
    Return None if not found.
    """
    return_elt = None
    for elt in DOM.IterWalkChildren(element):
        hit = isIn(elt, x, y)
        if hit:
            return_elt = elt
    return return_elt

def getElementUnderMouse(widget, x,y):
        """
        Return the most specific element in widget that contains (x,y).
        """
        element = widget.getElement()
        hit = isIn(element, x, y)
        if hit:
            child_elem = getTargetInChildren(element, x, y)
            if child_elem:
                return child_elem
            return element
        return None

def eventCoordinates(event):
    """ Get the absolute coordinates of a mouse event.
    http://www.quirksmode.org/js/events_properties.html#position
    """
    try:
        test = event.pageX
    except:
        test = None
    if test:
        return event.pageX, event.pageY

    offsetX, offsetY = getScrollOffsets()
    pageX = event.clientX + offsetX
    pageY = event.clientY + offsetY
    return pageX, pageY

def getScrollOffsets():
    """
    Get the window scroll offset values.
    We only need these if pageX, pageY are not provided.

    The uncommented formulation seems to work.
    """

#    st = Window.getScrollTop()
#    sl = Window.getScrollLeft()
#    return sl, st

# http://www.howtocreate.co.uk/tutorials/javascript/browserwindow
    try:
        scrollOffsetY = wnd().pageYOffset
        scrollOffsetX = wnd().pageXOffset
        return scrollOffsetX, scrollOffsetY
    except:
        try:
            scrollOffsetY = doc().body.scrollTop
            scrollOffsetX = doc().body.scrollLeft
            return scrollOffsetX, scrollOffsetY
        except:
            scrollOffsetY = doc().documentElement.scrollTop
            scrollOffsetX = doc().documentElement.scrollLeft
            return scrollOffsetX, scrollOffsetY


class DraggingWidget(Widget):
    """
    A widget for holding the dragging feedback elements.
    """
    def __init__(self, element=None):
        Widget.__init__(self, Element=DOM.createElement('div'))
        self.children = []
        if element is not None:
            clone = self.cloneElement(element)
            self.addChild(clone)
        self.setStyleAttribute('position', 'absolute')

    def addChild(self, element):
        DOM.appendChild(self.getElement(),element)
        self.children.append(element)

    def cloneElement(self, element):
        clone = element.cloneNode(True)
        copyStyles(element, clone)
        return clone

    def setImage(self,element):
        container = self.getElement()
        clone = self.cloneElement(element)
        while self.children:
            child = self.children.pop()
            DOM.removeChild(container, child)
        self.addChild(clone)

    def addElement(self, element):
        clone = self.cloneElement(element)
        self.addChild(clone)

    def updateCursor(self, operation):
        # TODO: change cursors.  Probably means making custom cursors.
        if operation == 'copy':
            pass
        elif operation == 'link':
            pass
        elif operation == 'move':
            pass
        else:
            self.setStyleAttribute('cursor', 'auto')


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

    def setCurrentTargetElement(self, element):
        if self._currentTargetElement is not None:
            if not DOM.compare(self._currentTargetElement, element):
                leave_event = DragEvent(self.mouseEvent,'dragleave',
                                                self.currentTargetElement)
                self.currentDropWidget.onDragLeave(leave_event)
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

    def stashData(self,dataTransfer):
        """
        Hold the data from a dragstart event until it is dropped.
        """
        self.data = dataTransfer._data

    def updateDropEffect(self, event_type):
        """
        http://dev.w3.org/html5/spec/dnd.html
        """
        dropEffect='none'
        if self.draggingImage:
            if event_type in ['dragover', 'dragenter']:
                ea = self.effectAllowed
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
            self.dropEffect = dropEffect
            self.draggingImage.updateCursor(dropEffect)

    def updateDragOperation(self):
        """
        http://dev.w3.org/html5/spec/dnd.html
        """
        if (self.dropEffect == 'copy' and self.effectAllowed in
            ['uninitialized', 'copy','copyLink', 'copyMove', 'all']):
            self.currentDragOperation = 'copy'
        elif (self.dropEffect == 'link' and self.effectAllowed in
            ['uninitialized', 'link', 'copyLink', 'linkMove', 'all']):
                self.currentDragOperation = 'link'
        elif (self.dropEffect == 'move' and self.effectAllowed in
              ['uninitialized', 'move', 'copyMove', 'linkMove', 'all']):
                self.currentDragOperation = 'move'
        else:
            self.currentDragOperation = 'none'

    def registerTarget(self,target):
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

    def provideTypes(self, event):
        """
        Put a dummy data member in the dataTransfer member of the event
        so that types may be delivered to the event handlers.
        """
        dt = event.dataTransfer
        keys = self.data.keys()
        for item in keys:
            dt.setData(item, '')

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

    def addElement(self, element):
        """
        This is called from DataTransfer
        """
        if self.draggingImage:
            self.draggingImage.addElement(element)
        else:
            self.createDraggingImage(element)

    def createDraggingImage(self, element):
        self.draggingImage = DraggingWidget(element)

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
            self.effectAllowed = 'uninitialized'
            self.dropEffect = 'none'
            self.currentDragOperation = 'none'
            dragStartEvent = DragEvent(event, 'dragstart')
            self.dragWidget.onDragStart(dragStartEvent)
            if not isCanceled(dragStartEvent):
                fromElement = self.dragWidget.getElement()
                dt = dragStartEvent.dataTransfer
                self.stashData(dt)
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
                # Dragging image might have been set in the dragstart
                # event through dataTransfer. If we do not have one,
                # create one by cloning the indicated element.
                if not self.draggingImage:
                    self.setDragImage(fromElement,
                                      self.origMouseX - self.origLeft,
                                      self.origMouseY - self.origTop)
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
        self.dropEffect = 'none'
        drag_event = DragEvent(event,'drag')
        self.dragWidget.onDrag(drag_event)
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
                    enter_event = DragEvent(event,'dragenter', drop_element)
                    self.provideTypes(enter_event)
                    drop_widget.onDragEnter(enter_event)
                    if isCanceled(enter_event):
                        self.currentTargetElement = drop_element
                        self.currentDropWidget = drop_widget

                if self.currentTargetElement is not None:
                    # disable dropping if over event is not canceled
                    over_event = DragEvent(event, 'dragover', drop_element)
                    self.provideTypes(over_event)
                    self.currentDropWidget.onDragOver(over_event)
                    if isCanceled(over_event):
                        self.updateDragOperation()
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

    def onMouseUp(self, sender, x, y):
        event = DOM.eventGetCurrentEvent()
        self.dragging = NOT_DRAGGING
        if self.draggingImage:
            GlassWidget.hide()
            if (self.currentDragOperation == 'none'
                    or not self.currentTargetElement):
                if self.currentTargetElement:
                    leave_event = DragEvent(event,'dragleave',
                                            self.currentTargetElement)
                    self.currentDropWidget.onDragLeave(leave_event)
                self.returnDrag()
            else:
                drop_event = DragEvent(event,'drop', self.currentTargetElement)
                drop_event.dataTransfer._data = self.data
                self.dropEffect = self.currentDragOperation
                self.currentDropWidget.onDrop(drop_event)
                if isCanceled(drop_event):
                    self.currentDragOperation = self.dropEffect
                else:
                    self.currentDragOperation = 'none'
                self.zapDragImage()
                dragEnd_event = DragEvent(event,'dragend')
                self.dropEffect = self.currentDragOperation
                self.dragWidget.onDragEnd(dragEnd_event)

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

class DOMStringList(object):
    """
DOMStringList implementation
http://www.w3.org/TR/2003/WD-DOM-Level-3-Core-20030226/core.html#DOMStringList
    """
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable:
                self._data.append(str(item))

    def _getLength(self):
        return len(self._data)

    length = property(_getLength)

    def item(self, index):
        try:
            return self._data[index]
        except:
            return None


class Uri_list(object):
    """
    text/uri-list implementation

    see http://www.rfc-editor.org/rfc/rfc2483.txt
    """
    def __init__(self, data=None):
        self._data = []
        if data:
            # presume crlf-delimited data
            for item in data.split('\r\n'):
                self._data.append(item.strip())

    def add_url(self, url):
        self._data.append(url)

    def get_first_url(self):
        for item in self._data:
            if item[0] != '#':
                return item
        return ''

    def __str__(self):
        if self._data:
            return '\r\n'.join(self._data) + '\r\n'
        return ''


class DataTransfer(object):
    """
    DataTransfer implementation
    http://dev.w3.org/html5/spec/dnd.html#datatransfer
    """

    def __init__(self):
        self._data = {}

    def setDropEffect(self, effect):
        if effect in ('none', 'copy', 'link' ,'move'):
            dndHelper.dropEffect = effect

    def getDropEffect(self):
        return dndHelper.dropEffect

    dropEffect = property(getDropEffect, setDropEffect)

    def setEffectAllowed(self, effect):
        if effect in ('none', 'copy', 'copyLink', 'copyMove',
            'link', 'linkMove', 'move', 'all', 'uninitialized'):
            dndHelper.effectAllowed = effect

    def getEffectAllowed(self):
        return dndHelper.effectAllowed

    effectAllowed = property(getEffectAllowed, setEffectAllowed)

    def setData(self, format, data=None):
        if data is None:
            raise TypeError(
                "Need both format (e.g., MIME type) and data for setData.")
        format = format.lower().strip()
        if format == 'text' or format == 'text/plain':
            self._data['text/plain'] = data
        elif format == 'url' or format == 'text/uri-list':
            try:
                uri_data = self._data['text/uri-list']
            except KeyError:
                uri_data = Uri_list()
                self._data['text/uri-list'] = uri_data
            uri_data.add_url(data)
        else:
            self._data[format] = data
        return True

    def getTypes(self):
        keys = self._data.keys()
        if 'text/plain' in keys:
            keys.append('Text')
        if 'text/uri-list' in keys:
            keys.append('Url')
#        if self.files:
#            keys.append('Files')
        return DOMStringList(keys)

    types = property(getTypes)

    def getData(self, format):
        format = format.strip().lower()
        if format == 'text':
            if 'text/plain' in self._data:
                return self._data['text/plain']
        elif format == 'url' or format == 'text/uri-list':
            if 'text/uri-list' in self._data:
                return self._data['text/uri-list'].get_first_url()
        elif format in self._data:
            return self._data[format]
        else:
            return ""

    def clearData(self, format=None):
        if format is None:
            self._data = {}
        else:
            format = format.lower()
            if format in self._data:
                del self._data[format]

    def addElement(self,element):
        dndHelper.addElement(element)

    def setDragImage(self, element, x=0, y=0):
        dndHelper.setDragImage(element, x, y)


class DragEvent(object):
    """
    simulates a drag/drop event.
    """
    relatedTarget = None
    detail = 0
    returnValue = True
    def __init__(self, evt, type, target=None):
        self.evt = evt
        self.type = type
        if target:
            self.target = target
        else:
            try:
                self.target = evt.target
            except:
                # ie
                self.target = evt.srcElement
        self.dataTransfer = DataTransfer()
        dndHelper.updateDropEffect(type)
    # rather than copying a bunch of attributes on init, we provide a bunch
    # of property statements.  These properties hardly ever get looked at
    # during dnd events anyway, but they're there if we need them.
    def getScreenX(self):
        return self.evt.screenX
    screenX = property(getScreenX)

    def getScreenY(self):
        return self.evt.screenY
    screenY = property(getScreenY)

    def getClientX(self):
        return self.evt.clientX
    clientX = property(getClientX)

    def getClientY(self):
        return self.evt.clientY
    clientY = property(getClientY)

    def getAltKey(self):
        return self.evt.altKey
    altKey = property(getAltKey)

    def getCtrlKey(self):
        return self.evt.ctrlKey
    ctrlKey = property(getCtrlKey)

    def getShiftKey(self):
        return self.evt.shiftKey
    shiftKey = property(getShiftKey)

    def getMetaKey(self):
        return self.evt.metaKey
    metaKey = property(getMetaKey)

    def getButton(self):
        return self.evt.button
    button = property(getButton)

    def preventDefault(self):
        """
        ie6 sets returnValue to False, so we do, too.
        """
        self.returnValue = False

    def initDragEvent(self, type, canBubble, cancelable, dummy, detail, screenX,
                      screenY, clientX, clientY, ctrlKey, altKey, shiftKey,
                      metaKey, button, relatedTarget, dataTransfer):
        """
        Just raise NotImplemented.  Provided only for completeness with the
        Interface.
        """
        raise NotImplemented("Instanciate this class with a mouse event.")
#        self.type = type
#        self.canBubble = canBubble
#        self.cancelable = cancelable
#        self.dummy = dummy
#        self.detail = detail
#        self.screenX = screenX
#        self.screenY = screenY
#        self.clientX = clientX
#        self.clientY = clientY
#        self.ctrlKey = ctrlKey
#        self.altKey = altKey
#        self.shiftKey = shiftKey
#        self.metaKey = metaKey
#        self.button = button
#        self.relatedTarget = relatedTarget
#        self.dataTransfer = dataTransfer


