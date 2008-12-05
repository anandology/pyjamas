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
from __pyjamas__ import JS, console
import DOM
import pygwt
from DeferredCommand import DeferredCommand
import pyjslib
from History import History
import Window
from sets import Set


class Event:
    """
    This class contains flags and integer values used by the event system.
    
    It is not meant to be subclassed or instantiated.
    """
    BUTTON_LEFT   = 1
    BUTTON_MIDDLE = 4
    BUTTON_RIGHT  = 2
    
    ONBLUR        = 0x01000
    ONCHANGE      = 0x00400
    ONCLICK       = 0x00001
    ONDBLCLICK    = 0x00002
    ONERROR       = 0x10000
    ONFOCUS       = 0x00800
    ONKEYDOWN     = 0x00080
    ONKEYPRESS    = 0x00100
    ONKEYUP       = 0x00200
    ONLOAD        = 0x08000
    ONLOSECAPTURE = 0x02000
    ONMOUSEDOWN   = 0x00004
    ONMOUSEMOVE   = 0x00040
    ONMOUSEOUT    = 0x00020
    ONMOUSEOVER   = 0x00010
    ONMOUSEUP     = 0x00008
    ONSCROLL      = 0x04000
    
    FOCUSEVENTS   = 0x01800 # ONFOCUS | ONBLUR
    KEYEVENTS     = 0x00380 # ONKEYDOWN | ONKEYPRESS | ONKEYUP
    MOUSEEVENTS   = 0x0007C # ONMOUSEDOWN | ONMOUSEUP | ONMOUSEMOVE | ONMOUSEOVER | ONMOUSEOUT


# FocusListenerCollection
class FocusListener:
    def fireFocusEvent(self, listeners, sender, event):
        type = DOM.eventGetType(event)
        if type == "focus":
            for listener in listeners:
                listener.onFocus(sender)
        elif type == "blur":
            for listener in listeners:
                listener.onLostFocus(sender)


# KeyboardListener + KeyboardListenerCollection
class KeyboardListener:
    KEY_ALT = 18
    KEY_BACKSPACE = 8
    KEY_CTRL = 17
    KEY_DELETE = 46
    KEY_DOWN = 40
    KEY_END = 35
    KEY_ENTER = 13
    KEY_ESCAPE = 27
    KEY_HOME = 36
    KEY_LEFT = 37
    KEY_PAGEDOWN = 34
    KEY_PAGEUP = 33
    KEY_RIGHT = 39
    KEY_SHIFT = 16
    KEY_TAB = 9
    KEY_UP = 38
    
    MODIFIER_ALT = 4
    MODIFIER_CTRL = 2
    MODIFIER_SHIFT = 1

    def getKeyboardModifiers(self, event):
        shift = 0
        ctrl = 0
        alt = 0
        
        if DOM.eventGetShiftKey(event):
            shift = KeyboardListener.MODIFIER_SHIFT
    
        if DOM.eventGetCtrlKey(event):
            ctrl = KeyboardListener.MODIFIER_CTRL
            
        if DOM.eventGetAltKey(event):
            alt = KeyboardListener.MODIFIER_ALT
    
        return shift | ctrl | alt


    def fireKeyboardEvent(self, listeners, sender, event):
        modifiers = KeyboardListener.getKeyboardModifiers(self, event)
    
        type = DOM.eventGetType(event)
        if type == "keydown":
            for listener in listeners:
                listener.onKeyDown(sender, DOM.eventGetKeyCode(event), modifiers)
        elif type == "keyup":
            for listener in listeners:
                listener.onKeyUp(sender, DOM.eventGetKeyCode(event), modifiers)
        elif type == "keypress":
            for listener in listeners:
                listener.onKeyPress(sender, DOM.eventGetKeyCode(event), modifiers)


# MouseListenerCollection
class MouseListener:
    def fireMouseEvent(self, listeners, sender, event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(sender.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(sender.getElement())
    
        type = DOM.eventGetType(event)
        if type == "mousedown":
            for listener in listeners:
                listener.onMouseDown(sender, x, y)
        elif type == "mouseup":
            for listener in listeners:
                listener.onMouseUp(sender, x, y)
        elif type == "mousemove":
            for listener in listeners:
                listener.onMouseMove(sender, x, y)
        elif type == "mouseover":
            from_element = DOM.eventGetFromElement(event)
            if not DOM.isOrHasChild(sender.getElement(), from_element):
                for listener in listeners:
                    listener.onMouseEnter(sender)
        elif type == "mouseout":
            to_element = DOM.eventGetToElement(event)
            if not DOM.isOrHasChild(sender.getElement(), to_element):
                for listener in listeners:
                    listener.onMouseLeave(sender)


class UIObject:

    def getAbsoluteLeft(self):
        return DOM.getAbsoluteLeft(self.getElement())

    def getAbsoluteTop(self):
        return DOM.getAbsoluteTop(self.getElement())

    def getElement(self):
        """Get the DOM element associated with the UIObject, if any"""
        return self.element

    def getOffsetHeight(self):
        return DOM.getIntAttribute(self.element, "offsetHeight")
    
    def getOffsetWidth(self):
        return DOM.getIntAttribute(self.element, "offsetWidth")

    def getStyleName(self):
        return DOM.getAttribute(self.element, "className")

    def getTitle(self):
        return DOM.getAttribute(self.element, "title")

    def setElement(self, element):
        """Set the DOM element associated with the UIObject."""
        self.element = element

    def setHeight(self, height):
        """Set the height of the element associated with this UIObject.  The
           value should be given as a CSS value, such as 100px, 30%, or 50pi"""
        DOM.setStyleAttribute(self.element, "height", height)

    def getHeight(self):
        return DOM.getStyleAttribute(self.element, "height")

    def setPixelSize(self, width, height):
        """Set the width and height of the element associated with this UIObject
           in pixels.  Width and height should be numbers."""
        if width >= 0:
            self.setWidth(width + "px")
        if height >= 0:
            self.setHeight(height + "px")

    def setSize(self, width, height):
        """Set the width and height of the element associated with this UIObject.  The
           values should be given as a CSS value, such as 100px, 30%, or 50pi"""
        self.setWidth(width)
        self.setHeight(height)

    def addStyleName(self, style):
        """Append a style to the element associated with this UIObject.  This is
        a CSS class name.  It will be added after any already-assigned CSS class for
        the element."""
        self.setStyleName(self.element, style, True)

    def removeStyleName(self, style):
        """Remove a style from the element associated with this UIObject.  This is
        a CSS class name."""
        self.setStyleName(self.element, style, False)

    # also callable as: setStyleName(self, style)
    def setStyleName(self, element, style=None, add=True):
        """When called with a single argument, this replaces all the CSS classes
        associated with this UIObject's element with the given parameter.  Otherwise,
        this is assumed to be a worker function for addStyleName and removeStyleName."""
        # emulate setStyleName(self, style)
        if style == None:
            style = element
            DOM.setAttribute(self.element, "className", style)
            return
        
        oldStyle = DOM.getAttribute(element, "className")
        if oldStyle == None:
            oldStyle = ""
        idx = oldStyle.find(style)

        # Calculate matching index
        lastPos = len(oldStyle)
        while idx != -1:
            if idx == 0 or (oldStyle[idx - 1] == " "):
                last = idx + len(style)
                if (last == lastPos) or ((last < lastPos) and (oldStyle[last] == " ")):
                    break
            idx = oldStyle.find(style, idx + 1)

        if add:
            if idx == -1:
                DOM.setAttribute(element, "className", oldStyle + " " + style)
        else:
            if idx != -1:
                begin = oldStyle[:idx]
                end = oldStyle[idx + len(style):]
                DOM.setAttribute(element, "className", begin + end)

    def setTitle(self, title):
        DOM.setAttribute(self.element, "title", title)

    def setWidth(self, width):
        """Set the width of the element associated with this UIObject.  The
           value should be given as a CSS value, such as 100px, 30%, or 50pi"""
        DOM.setStyleAttribute(self.element, "width", width)

    def getWidth(self):
        return DOM.getStyleAttribute(self.element, "width")

    def sinkEvents(self, eventBitsToAdd):
        """Request that the given events be delivered to the event handler for this
        element.  The event bits passed are added (using inclusive OR) to the events
        already "sunk" for the element associated with the UIObject.  The event bits
        are a combination of values from class L{Event}."""
        if self.element:
            DOM.sinkEvents(self.getElement(), eventBitsToAdd | DOM.getEventsSunk(self.getElement()))

    def setzIndex(self, index):
        DOM.setIntStyleAttribute(self.element, "zIndex", index)

    def isVisible(self, element=None):
        """Determine whether this element is currently visible, by checking the CSS
        property 'display'"""
        if not element:
            element = self.element
        return element.style.display != "none"

    # also callable as: setVisible(visible)
    def setVisible(self, element, visible=None):
        """Set whether this element is visible or not.  If a single parameter is
        given, the self.element is used.  This modifies the CSS property 'display',
        which means that an invisible element not only is not drawn, but doesn't
        occupy any space on the page."""
        if visible==None:
            visible = element
            element = self.element

        if visible:
            element.style.display = ""
        else:
            element.style.display = "none"

    def unsinkEvents(self, eventBitsToRemove):
        """Reverse the operation of sinkEvents.  See L{UIObject.sinkevents}."""
        DOM.sinkEvents(self.getElement(), ~eventBitsToRemove & DOM.getEventsSunk(self.getElement()))


class Widget(UIObject):
    """
        Base class for most of the UI classes.  This class provides basic services
        used by any Widget, including management of parents and adding/removing the
        event handler association with the DOM.
    """
    def __init__(self):
        self.attached = False
        self.parent = None
        self.layoutData = None

    def getLayoutData(self):
        return self.layoutData
    
    def getParent(self):
        """Widgets are kept in a hierarchy, and widgets that have been added to a panel
        will have a parent widget that contains them.  This retrieves the containing
        widget for this widget."""
        return self.parent

    def isAttached(self):
        """Return whether or not this widget has been attached to the document."""
        return self.attached

    def onBrowserEvent(self, event):
        pass

    def onLoad(self):
        pass

    def doDetachChildren(self):
        pass

    def doAttachChildren(self):
        pass

    def onAttach(self):
        """Called when this widget has an element, and that element is on the document's
        DOM tree, and we have a parent widget."""
        if self.isAttached():
            return
        self.attached = True
        DOM.setEventListener(self.getElement(), self)
        self.doAttachChildren()
        self.onLoad()
        
    def onDetach(self):
        """Called when this widget is being removed from the DOM tree of the document."""
        if not self.isAttached():
            return
        self.doDetachChildren()
        self.attached = False
        DOM.setEventListener(self.getElement(), None)

    def setLayoutData(self, layoutData):
        self.layoutData = layoutData

    def setParent(self, parent):
        """Update the parent attribute.  If the parent is currently attached to the DOM this
        assumes we are being attached also and calls onAttach()."""
        oldparent = self.parent
        self.parent = parent
        if parent == None:
            if oldparent != None and oldparent.attached:
                self.onDetach()
        elif parent.attached:
            self.onAttach()

    def removeFromParent(self):
        """Remove ourself from our parent.  The parent widget will call setParent(None) on
        us automatically"""
        if hasattr(self.parent, "remove"):
            self.parent.remove(self)

    def getID(self):
        """Get the id attribute of the associated DOM element."""
        return DOM.getAttribute(self.getElement(), "id")

    def setID(self, id):
        """Set the id attribute of the associated DOM element."""
        DOM.setAttribute(self.getElement(), "id", id)


class FocusWidget(Widget):

    def __init__(self, element):
        Widget.__init__(self)
        self.clickListeners = []
        self.focusListeners = []
        self.keyboardListeners = []

        self.setElement(element)
        self.sinkEvents(Event.ONCLICK | Event.FOCUSEVENTS | Event.KEYEVENTS)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)
        
    def addFocusListener(self, listener):
        self.focusListeners.append(listener)

    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)

    def getTabIndex(self):
        return Focus.getTabIndex(self, self.getElement())

    def isEnabled(self):
        return not DOM.getBooleanAttribute(self.getElement(), "disabled")

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "click":
            for listener in self.clickListeners:
                if hasattr(listener, "onClick"): listener.onClick(self, event)
                else: listener(self, event)
        elif type == "blur" or type == "focus":
            FocusListener.fireFocusEvent(self, self.focusListeners, self, event)
        elif type == "keydown" or type == "keypress" or type == "keyup":
            KeyboardListener.fireKeyboardEvent(self, self.keyboardListeners, self, event)

    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def removeFocusListener(self, listener):
        self.focusListeners.remove(listener)

    def removeKeyboardListener(self, listener):
        self.keyboardListeners.remove(listener)

    def setAccessKey(self, key):
        DOM.setAttribute(self.getElement(), "accessKey", "" + key)
        
    def setEnabled(self, enabled):
        DOM.setBooleanAttribute(self.getElement(), "disabled", not enabled)

    def setFocus(self, focused):
        if (focused):
            Focus.focus(self, self.getElement())
        else:
            Focus.blur(self, self.getElement())

    def setTabIndex(self, index):
        Focus.setTabIndex(self, self.getElement(), index)


class ButtonBase(FocusWidget):

    def __init__(self, element):
        FocusWidget.__init__(self, element)

    def getHTML(self):
        return DOM.getInnerHTML(self.getElement())

    def getText(self):
        return DOM.getInnerText(self.getElement())

    def setHTML(self, html):
        DOM.setInnerHTML(self.getElement(), html)

    def setText(self, text):
        DOM.setInnerText(self.getElement(), text)


class Button(ButtonBase):

    def __init__(self, html=None, listener=None):
        """
        Create a new button widget.
        
        @param html: Html content (e.g. the button label); see setHTML()
        @param listener: A new click listener; see addClickListener()
        
        """
        ButtonBase.__init__(self, DOM.createButton())
        self.adjustType(self.getElement())
        self.setStyleName("gwt-Button")
        if html:
            self.setHTML(html)
        if listener:
            self.addClickListener(listener)

    def adjustType(self, button):
        JS("""
        if (button.type == 'submit') {
            try { button.setAttribute("type", "button"); } catch (e) { }
        }
        """)

    def click(self):
        """
        Simulate a button click.
        """
        self.getElement().click()


class CheckBox(ButtonBase):
    
    def __init__(self, label=None, asHTML=False):
        self.initElement(DOM.createInputCheck())
        
        self.setStyleName("gwt-CheckBox")
        if label:
            if asHTML:
                self.setHTML(label)
            else:
                self.setText(label)

    def initElement(self, element):
        ButtonBase.__init__(self, DOM.createSpan())
        self.inputElem = element
        self.labelElem = DOM.createLabel()

        self.unsinkEvents(Event.FOCUSEVENTS| Event.ONCLICK)
        DOM.sinkEvents(self.inputElem, Event.FOCUSEVENTS | Event.ONCLICK | DOM.getEventsSunk(self.inputElem))
        
        DOM.appendChild(self.getElement(), self.inputElem)
        DOM.appendChild(self.getElement(), self.labelElem)
        
        uid = "check" + self.getUniqueID()
        DOM.setAttribute(self.inputElem, "id", uid)
        DOM.setAttribute(self.labelElem, "htmlFor", uid)

    # emulate static
    def getUniqueID(self):
        JS("""
        _CheckBox_unique_id++;
        return _CheckBox_unique_id;
        };
        var _CheckBox_unique_id=0;
        {
        """)

    def getHTML(self):
        return DOM.getInnerHTML(self.labelElem)

    def getName(self):
        return DOM.getAttribute(self.inputElem, "name")

    def getText(self):
        return DOM.getInnerText(self.labelElem)

    def setChecked(self, checked):
        DOM.setBooleanAttribute(self.inputElem, "checked", checked)
        DOM.setBooleanAttribute(self.inputElem, "defaultChecked", checked)

    def isChecked(self):
        if self.isAttached():
            propName = "checked"
        else:
            propName = "defaultChecked"
            
        return DOM.getBooleanAttribute(self.inputElem, propName)

    def isEnabled(self):
        return not DOM.getBooleanAttribute(self.inputElem, "disabled")

    def setEnabled(self, enabled):
        DOM.setBooleanAttribute(self.inputElem, "disabled", not enabled)

    def setFocus(self, focused):
        if focused:
            Focus.focus(self, self.inputElem)
        else:
            Focus.blur(self, self.inputElem)

    def setHTML(self, html):
        DOM.setInnerHTML(self.labelElem, html)

    def setName(self, name):
        DOM.setAttribute(self.inputElem, "name", name)

    def setTabIndex(self, index):
        Focus.setTabIndex(self, self.inputElem, index)

    def setText(self, text):
        DOM.setInnerText(self.labelElem, text)

    def onDetach(self):
        self.setChecked(self.isChecked())
        ButtonBase.onDetach(self)


class RadioButton(CheckBox):
    def __init__(self, group, label=None, asHTML=False):
        self.initElement(DOM.createInputRadio(group))

        self.setStyleName("gwt-RadioButton")
        if label:
            if asHTML:
                self.setHTML(label)
            else:
                self.setText(label)


class Composite(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.widget = None

    def initWidget(self, widget):
        if self.widget != None:
            return

        widget.removeFromParent()
        self.setElement(widget.getElement())

        self.widget = widget
        widget.setParent(self)

    def isAttached(self):
        if self.widget:
            return self.widget.isAttached()
        return False

    def onAttach(self):
        #print "Composite.onAttach", self
        self.widget.onAttach()
        DOM.setEventListener(self.getElement(), self);

        self.onLoad()
        
    def onDetach(self):
        self.widget.onDetach()
        
    def setWidget(self, widget):
        self.initWidget(widget)

    def onBrowserEvent(self, event):
        #print "Composite onBrowserEvent", self, event
        self.widget.onBrowserEvent(event)

class Panel(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.children = []

    def add(self):
        console.error("This panel does not support no-arg add()")

    def clear(self):
        # use this method, due to list changing as it's being iterated.
        children = []
        for child in panel.children:
            children.append(child)

        for child in children:
            panel.remove(child)

    def disown(self, widget):
        if widget.getParent() != self:
            console.error("widget %o is not a child of this panel %o", widget, self)
        else:
            element = widget.getElement()
            widget.setParent(None)
            parentElement = DOM.getParent(element)
            if parentElement:
                DOM.removeChild(parentElement, element)

    def adopt(self, widget, container):
        if container:
            widget.removeFromParent()
            DOM.appendChild(container, widget.getElement())
        widget.setParent(self)

    def remove(self, widget):
        pass

    def doAttachChildren(self):
        for child in self:
            child.onAttach()

    def doDetachChildren(self):
        for child in self:
            child.onDetach()

    def __iter__(self):
        return self.children.__iter__()


class CellFormatter:
    
    def __init__(self, outer):
        self.outer = outer
    
    def addStyleName(self, row, column, styleName):
        self.outer.prepareCell(row, column)
        self.outer.setStyleName(self.getElement(row, column), styleName, True)

    def getElement(self, row, column):
        self.outer.checkCellBounds(row, column)
        return DOM.getChild(self.outer.rowFormatter.getRow(self.outer.bodyElem, row), column)

    def getStyleName(self, row, column):
        return DOM.getAttribute(self.getElement(row, column), "className")

    def isVisible(self, row, column):
        element = self.getElement(row, column)
        return self.outer.isVisible(element)

    def removeStyleName(self, row, column, styleName):
        self.outer.checkCellBounds(row, column)
        self.outer.setStyleName(self.getElement(row, column), styleName, False)

    def setAlignment(self, row, column, hAlign, vAlign):
        self.setHorizontalAlignment(row, column, hAlign)
        self.setVerticalAlignment(row, column, vAlign)

    def setHeight(self, row, column, height):
        self.outer.prepareCell(row, column)
        element = self.getCellElement(self.outer.bodyElem, row, column)
        DOM.setStyleAttribute(element, "height", height)

    def setHorizontalAlignment(self, row, column, align):
        self.outer.prepareCell(row, column)
        element = self.getCellElement(self.outer.bodyElem, row, column)
        DOM.setAttribute(element, "align", align)

    def setStyleName(self, row, column, styleName):
        self.outer.prepareCell(row, column)
        self.setAttr(row, column, "className", styleName)

    def setVerticalAlignment(self, row, column, align):
        self.outer.prepareCell(row, column)
        DOM.setStyleAttribute(self.getCellElement(self.outer.bodyElem, row, column), "verticalAlign", align)

    def setVisible(self, row, column, visible):
        element = self.ensureElement(row, column)
        self.outer.setVisible(element, visible)

    def setWidth(self, row, column, width):
        self.outer.prepareCell(row, column)
        DOM.setStyleAttribute(self.getCellElement(self.outer.bodyElem, row, column), "width", width)

    def setWordWrap(self, row, column, wrap):
        self.outer.prepareCell(row, column)
        if wrap:
            wrap_str = ""
        else:
            wrap_str = "nowrap"
        
        DOM.setStyleAttribute(self.getElement(row, column), "whiteSpace", wrap_str)

    def getCellElement(self, table, row, col):
        JS("""
        var out = table.rows[row].cells[col];
        return (out == null ? null : out);
        """)

    def getRawElement(self, row, column):
        return self.getCellElement(self.outer.bodyElem, row, column)

    def ensureElement(self, row, column):
        self.outer.prepareCell(row, column)
        return DOM.getChild(self.outer.rowFormatter.ensureElement(row), column)

    def getAttr(self, row, column, attr):
        elem = self.getElement(row, column)
        return DOM.getAttribute(elem, attr)

    def setAttr(self, row, column, attrName, value):
        elem = self.getElement(row, column)
        DOM.setAttribute(elem, attrName, value)



class RowFormatter:

    def __init__(self, outer):
        self.outer = outer

    def addStyleName(self, row, styleName):
        self.outer.setStyleName(self.ensureElement(row), styleName, True)

    def getElement(self, row):
        self.outer.checkRowBounds(row)
        return self.getRow(self.outer.bodyElem, row)
        
    def getStyleName(self, row):
        return DOM.getAttribute(self.getElement(row), "className")

    def isVisible(self, row):
        element = self.getElement(row)
        return self.outer.isVisible(element)

    def removeStyleName(self, row, styleName):
        self.outer.setStyleName(self.getElement(row), styleName, False)

    def setStyleName(self, row, styleName):
        elem = self.ensureElement(row)
        DOM.setAttribute(elem, "className", styleName)
        
    def setVerticalAlign(self, row, align):
        DOM.setStyleAttribute(self.ensureElement(row), "verticalAlign", align)

    def setVisible(self, row, visible):
        element = self.ensureElement(row)
        self.outer.setVisible(element, visible)

    def ensureElement(self, row):
        self.outer.prepareRow(row)
        return self.getRow(self.outer.bodyElem, row)

    def getRow(self, element, row):
        JS("""
        return element.rows[row];
        """)

    def setAttr(self, row, attrName, value):
        element = self.ensureElement(row)
        DOM.setAttribute(element, attrName, value)


class HTMLTable(Panel):
    
    def __init__(self):
        Panel.__init__(self)
        self.cellFormatter = CellFormatter(self)
        self.rowFormatter = RowFormatter(self)
        self.tableListeners = []
        self.widgetMap = {}

        self.tableElem = DOM.createTable()
        self.bodyElem = DOM.createTBody()
        DOM.appendChild(self.tableElem, self.bodyElem)
        self.setElement(self.tableElem)
        self.sinkEvents(Event.ONCLICK)

    def addTableListener(self, listener):
        self.tableListeners.append(listener)

    def clear(self):
        for row in range(self.getRowCount()):
            for col in range(self.getCellCount(row)):
                child = self.getWidget(row, col)
                if child != None:
                    self.removeWidget(child)
        # assert len(self.widgetMap) == 0

    def clearCell(self, row, column):
        td = self.cellFormatter.getElement(row, column)
        return self.internalClearCell(td)

    def getCellCount(self, row):
        return 0

    def getCellFormatter(self):
        return self.cellFormatter
    
    def getCellPadding(self):
        return DOM.getIntAttribute(self.tableElem, "cellPadding")
    
    def getCellSpacing(self):
        return DOM.getIntAttribute(self.tableElem, "cellSpacing")

    def getHTML(self, row, column):
        element = self.cellFormatter.getElement(row, column)
        return DOM.getInnerHTML(element)

    def getRowCount(self):
        return 0
        
    def getRowFormatter(self):
        return self.rowFormatter
        
    def getText(self, row, column):
        self.checkCellBounds(row, column)
        element = self.cellFormatter.getElement(row, column)
        return DOM.getInnerText(element)

    # also callable as getWidget(widgetElement)
    def getWidget(self, row, column=None):
        if column == None:
            key = self.computeKeyForElement(row)
        else:
            self.checkCellBounds(row, column)
            key = self.computeKey(row, column)

        if key == None:
            return None
        return self.widgetMap[key]

    def isCellPresent(self, row, column):
        # GWT uses "and", possibly a bug
        if row >= self.getRowCount() or row < 0:
            return False
        
        if column < 0 or column >= self.getCellCount(row):
            return False
        
        return True

    def __iter__(self):
        return self.widgetMap.itervalues()

    def onBrowserEvent(self, event):
        if DOM.eventGetType(event) == "click":
            td = self.getEventTargetCell(event)
            if not td:
                return

            tr = DOM.getParent(td)
            body = DOM.getParent(tr)
            row = DOM.getChildIndex(body, tr)
            column = DOM.getChildIndex(tr, td)
        
            for listener in self.tableListeners:
                if listener.onCellClicked:
                    listener.onCellClicked(self, row, column)
                else:
                    listener(self)

    def remove(self, widget):
        if widget.getParent() != self:
            return False
        
        self.removeWidget(widget)
        return True

    def removeTableListener(self, listener):
        self.tableListeners.remove(listener)

    def setBorderWidth(self, width):
        DOM.setAttribute(self.tableElem, "border", width)

    def setCellPadding(self, padding):
        DOM.setIntAttribute(self.tableElem, "cellPadding", padding)

    def setCellSpacing(self, spacing):
        DOM.setIntAttribute(self.tableElem, "cellSpacing", spacing)

    def setHTML(self, row, column, html):
        self.prepareCell(row, column)
        td = self.cleanCell(row, column)
        if html != None:
            DOM.setInnerHTML(td, html)

    def setText(self, row, column, text):
        self.prepareCell(row, column)
        td = self.cleanCell(row, column)
        if text != None:
            DOM.setInnerText(td, text)

    def setWidget(self, row, column, widget):
        self.prepareCell(row, column)
        if widget == None:
            return

        widget.removeFromParent()
        td = self.cleanCell(row, column)
        widget_hash = hash(widget)
        element = widget.getElement()
        DOM.setAttribute(element, "__hash", widget_hash)
        self.widgetMap[widget_hash] = widget
        self.adopt(widget, td)

    def cleanCell(self, row, column):
        td = self.cellFormatter.getRawElement(row, column)
        self.internalClearCell(td)
        return td

    def computeKey(self, row, column):
        element = self.cellFormatter.getRawElement(row, column)
        child = DOM.getFirstChild(element)
        if child == None:
            return None

        return self.computeKeyForElement(child)

    def computeKeyForElement(self, widgetElement):
        return DOM.getAttribute(widgetElement, "__hash")

    def removeWidget(self, widget):
        self.disown(widget)

        del self.widgetMap[self.computeKeyForElement(widget.getElement())]
        return True

    def checkCellBounds(self, row, column):
        self.checkRowBounds(row)
        #if column<0: raise IndexError, "Column " + column + " must be non-negative: " + column

        cellSize = self.getCellCount(row)
        #if cellSize<column: raise IndexError, "Column " + column + " does not exist, col at row " + row + " size is " + self.getCellCount(row) + "cell(s)"

    def checkRowBounds(self, row):
        rowSize = self.getRowCount()
        #if row >= rowSize or row < 0: raise IndexError, "Row " + row + " does not exist, row size is " + self.getRowCount()

    def createCell(self):
        return DOM.createTD()
        
    def getBodyElement(self):
        return self.bodyElem

    # also callable as getDOMCellCount(row)
    def getDOMCellCount(self, element, row=None):
        if row == None:
            return self.getDOMCellCountImpl(self.bodyElem, element)
        return self.getDOMCellCountImpl(element, row)

    def getDOMCellCountImpl(self, element, row):
        JS("""
        return element.rows[row].cells.length;
        """)

    # also callable as getDOMRowCount(element)
    def getDOMRowCount(self, element=None):
        if element == None:
            element = self.bodyElem
        return self.getDOMRowCountImpl(element)

    def getDOMRowCountImpl(self, element):
        JS("""
        return element.rows.length;
        """)

    def getEventTargetCell(self, event):
        td = DOM.eventGetTarget(event)
        while td != None:
            if DOM.getAttribute(td, "tagName").lower() == "td":
                tr = DOM.getParent(td)
                body = DOM.getParent(tr)
                if DOM.compare(body, self.bodyElem):
                    return td
            if DOM.compare(td, self.bodyElem):
                return None
            td = DOM.getParent(td)
        
        return None

    def insertCell(self, row, column):
        tr = self.rowFormatter.getRow(self.bodyElem, row)
        td = self.createCell()
        DOM.insertChild(tr, td, column)

    def insertCells(self, row, column, count):
        tr = self.rowFormatter.getRow(self.bodyElem, row)
        for i in range(column, column + count):
            td = self.createCell()
            DOM.insertChild(tr, td, i)

    def insertRow(self, beforeRow):
        if beforeRow != self.getRowCount():
            self.checkRowBounds(beforeRow)
        
        tr = DOM.createTR()
        DOM.insertChild(self.bodyElem, tr, beforeRow)
        return beforeRow

    def internalClearCell(self, td):
        maybeChild = DOM.getFirstChild(td)
        widget = None
        if maybeChild != None:
            widget = self.getWidget(maybeChild)

        if widget != None:
            self.removeWidget(widget)
            return True

        DOM.setInnerHTML(td, "")
        return False

    def prepareCell(self, row, column):
        pass

    def prepareRow(self, row):
        pass

    def removeCell(self, row, column):
        self.checkCellBounds(row, column)
        td = self.cleanCell(row, column)
        tr = self.rowFormatter.getRow(self.bodyElem, row)
        DOM.removeChild(tr, td)

    def removeRow(self, row):
        for column in range(self.getCellCount(row)):
            self.cleanCell(row, column)
        DOM.removeChild(self.bodyElem, self.rowFormatter.getRow(self.bodyElem, row))

    def setCellFormatter(self, cellFormatter):
        self.cellFormatter = cellFormatter

    def setRowFormatter(self, rowFormatter):
        self.rowFormatter = rowFormatter
    

class Grid(HTMLTable):
    
    def __init__(self, rows=0, columns=0):
        HTMLTable.__init__(self)
        self.cellFormatter = CellFormatter(self)
        self.rowFormatter = RowFormatter(self)
        self.numColumns = 0
        self.numRows = 0
        if rows > 0 or columns > 0:
            self.resize(rows, columns)

    def resize(self, rows, columns):
        self.resizeColumns(columns)
        self.resizeRows(rows)

    def resizeColumns(self, columns):
        if self.numColumns == columns:
            return
        
        if self.numColumns > columns:
            for i in range(0, self.numRows):
                for j in range(self.numColumns - 1, columns - 1, -1):
                    self.removeCell(i, j)
        else:
            for i in range(self.numRows):
                for j in range(self.numColumns, columns):
                    self.insertCell(i, j)
        self.numColumns = columns

    def resizeRows(self, rows):
        if self.numRows == rows:
            return

        if self.numRows < rows:
            self.addRows(self.getBodyElement(), rows - self.numRows, self.numColumns)
            self.numRows = rows
        else:
            while self.numRows > rows:
                self.numRows -= 1
                self.removeRow(self.numRows)

    def createCell(self):
        td = HTMLTable.createCell(self)
        DOM.setInnerHTML(td, "&nbsp;")
        return td

    def clearCell(self, row, column):
        td = self.cellFormatter.getElement(row, column)
        b = HTMLTable.internalClearCell(self, td)
        DOM.setInnerHTML(td, "&nbsp;")
        return b

    def prepareCell(self, row, column):
        pass

    def prepareRow(self, row):
        pass

    def getCellCount(self, row):
        return self.numColumns
    
    def getColumnCount(self):
        return self.numColumns
    
    def getRowCount(self):
        return self.numRows

    def addRows(self, table, numRows, columns):
        JS("""
        var td = $doc.createElement("td");
        td.innerHTML = "&nbsp;";
        var row = $doc.createElement("tr");
        for(var cellNum = 0; cellNum < columns; cellNum++) {
            var cell = td.cloneNode(true);
            row.appendChild(cell);
        }
        table.appendChild(row);
        for(var rowNum = 1; rowNum < numRows; rowNum++) {
            table.appendChild(row.cloneNode(true));
        }
        """)


class FlexCellFormatter(CellFormatter):
    def __init__(self, outer):
        CellFormatter.__init__(self, outer)
    
    def getColSpan(self, row, column):
        return DOM.getIntAttribute(self.getElement(row, column), "colSpan")

    def getRowSpan(self, row, column):
        return DOM.getIntAttribute(self.getElement(row, column), "rowSpan")
        
    def setColSpan(self, row, column, colSpan):
        DOM.setIntAttribute(self.ensureElement(row, column), "colSpan", colSpan)

    def setRowSpan(self, row, column, rowSpan):
        DOM.setIntAttribute(self.ensureElement(row, column), "rowSpan", rowSpan)


class FlexTable(HTMLTable):
    def __init__(self):
        HTMLTable.__init__(self)
        self.cellFormatter = FlexCellFormatter(self)
        self.rowFormatter = RowFormatter(self)

    def addCell(self, row):
        self.insertCell(row, self.getCellCount(row))

    def getCellCount(self, row):
        self.checkRowBounds(row)
        return self.getDOMCellCount(self.getBodyElement(), row)

    def getFlexCellFormatter(self):
        return self.getCellFormatter()

    def getRowCount(self):
        return self.getDOMRowCount()

    def removeCells(self, row, column, num):
        for i in range(num):
            self.removeCell(row, column)

    def prepareCell(self, row, column):
        self.prepareRow(row)
        #if column < 0: throw new IndexOutOfBoundsException("Cannot create a column with a negative index: " + column);
        
        cellCount = self.getCellCount(row)
        required = column + 1 - cellCount
        if required > 0:
            self.addCells(self.getBodyElement(), row, required)

    def prepareRow(self, row):
        #if row < 0: throw new IndexOutOfBoundsException("Cannot create a row with a negative index: " + row);

        rowCount = self.getRowCount()
        for i in range(rowCount, row + 1):
            self.insertRow(i)

    def addCells(self, table, row, num):
        JS("""
        var rowElem = table.rows[row];
        for(var i = 0; i < num; i++){
            var cell = $doc.createElement("td");
            rowElem.appendChild(cell);
        }
        """)


class ComplexPanel(Panel):
    """
        Superclass for widgets with multiple children.
    """
    def __init__(self):
        Panel.__init__(self)
        self.children = []
    
    def add(self, widget, container):
        self.insert(widget, container, len(self.children))

    def getChildren(self):
        return self.children
    
    def insert(self, widget, container, beforeIndex):
        if widget.getParent() == self:
            return

        self.adopt(widget, container)
        self.children.insert(beforeIndex, widget)

        # this code introduces an obscure IE6 bug that corrupts its DOM tree!
        #widget.removeFromParent()
        #self.children.insert(beforeIndex, widget)
        #DOM.insertChild(container, widget.getElement(), beforeIndex)
        #self.adopt(widget, container)

    def remove(self, widget):
        if widget not in self.children:
            return False

        self.disown(widget)
        #elem = self.getElement()
        #DOM.removeChild(DOM.getParent(elem), elem)
        self.children.remove(widget)
        return True


class AbsolutePanel(ComplexPanel):

    def __init__(self):
        ComplexPanel.__init__(self)
        self.setElement(DOM.createDiv())
        DOM.setStyleAttribute(self.getElement(), "position", "relative")
        DOM.setStyleAttribute(self.getElement(), "overflow", "hidden")

    def add(self, widget, left=None, top=None):
        ComplexPanel.add(self, widget, self.getElement())

        if left != None:
            self.setWidgetPosition(widget, left, top)

    def setWidgetPosition(self, widget, left, top):
        self.checkWidgetParent(widget)
        
        h = widget.getElement()
        if (left == -1) and (top == -1):
            DOM.setStyleAttribute(h, "left", "")
            DOM.setStyleAttribute(h, "top", "")
            DOM.setStyleAttribute(h, "position", "static")
        else:
            DOM.setStyleAttribute(h, "position", "absolute")
            DOM.setStyleAttribute(h, "left", left + "px")
            DOM.setStyleAttribute(h, "top", top + "px")

    def getWidgetLeft(self, widget):
        self.checkWidgetParent(widget)
        return DOM.getIntAttribute(widget.getElement(), "offsetLeft")

    def getWidgetTop(self, widget):
        self.checkWidgetParent(widget)
        return DOM.getIntAttribute(widget.getElement(), "offsetTop")

    def checkWidgetParent(self, widget):
        if widget.getParent() != self:
            console.error("Widget must be a child of this panel.")


class Label(Widget):

    def __init__(self, text=None, wordWrap=True):
        Widget.__init__(self)
        self.horzAlign = ""
        self.clickListeners = []
        self.mouseListeners = []
        
        self.setElement(DOM.createDiv())
        self.sinkEvents(Event.ONCLICK | Event.MOUSEEVENTS)
        self.setStyleName("gwt-Label")
        if text:
            self.setText(text)

        self.setWordWrap(wordWrap)
            
    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def getHorizontalAlignment(self):
        return self.horzAlign

    def getText(self):
        return DOM.getInnerText(self.getElement())

    def getWordWrap(self):
        return not (DOM.getStyleAttribute(self.getElement(), "whiteSpace") == "nowrap")

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        #print "Label onBrowserEvent", type, self.clickListeners
        if type == "click":
            for listener in self.clickListeners:
                if listener.onClick: listener.onClick(self, event)
                else: listener(self, event)
        elif type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener.fireMouseEvent(self, self.mouseListeners, self, event)

    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def removeMouseListener(self, listener):
        self.mouseListeners.remove(listener)

    def setHorizontalAlignment(self, align):
        self.horzAlign = align
        DOM.setStyleAttribute(self.getElement(), "textAlign", align)

    def setText(self, text):
        DOM.setInnerText(self.getElement(), text)

    def setWordWrap(self, wrap):
        if wrap:
            style = "normal"
        else:
            style = "nowrap"
        DOM.setStyleAttribute(self.getElement(), "whiteSpace", style)


class HTML(Label):
    
    def __init__(self, html=None, wordWrap=True):
        Label.__init__(self)
    
        self.setElement(DOM.createDiv())
        self.sinkEvents(Event.ONCLICK | Event.MOUSEEVENTS)
        self.setStyleName("gwt-HTML")
        if html:
            self.setHTML(html)
            
        self.setWordWrap(wordWrap)
    
    def getHTML(self):
        return DOM.getInnerHTML(self.getElement())

    def setHTML(self, html):
        DOM.setInnerHTML(self.getElement(), html)


class HasHorizontalAlignment:
    ALIGN_LEFT = "left"
    ALIGN_CENTER = "center"
    ALIGN_RIGHT = "right"


class HasVerticalAlignment:
    ALIGN_TOP = "top"
    ALIGN_MIDDLE = "middle"
    ALIGN_BOTTOM = "bottom"


class HasAlignment:
    ALIGN_BOTTOM = "bottom"
    ALIGN_MIDDLE = "middle"
    ALIGN_TOP = "top"
    ALIGN_CENTER = "center"
    ALIGN_LEFT = "left"
    ALIGN_RIGHT = "right"


class CellPanel(ComplexPanel):
    
    def __init__(self):
        ComplexPanel.__init__(self)
        
        self.table = DOM.createTable()
        self.body = DOM.createTBody()
        self.spacing = None
        self.padding = None
        DOM.appendChild(self.table, self.body)
        self.setElement(self.table)

    def getTable(self):
        return self.table

    def getBody(self):
        return self.body

    def getSpacing(self):
        return self.spacing

    def getPadding(self):
        return self.padding

    def getWidgetTd(self, widget):
        if widget.getParent() != self:
            return None
        return DOM.getParent(widget.getElement())

    def setBorderWidth(self, width):
        DOM.setAttribute(self.table, "border", "" + width)

    def setCellHeight(self, widget, height):
        td = DOM.getParent(widget.getElement())
        DOM.setAttribute(td, "height", height)

    def setCellHorizontalAlignment(self, widget, align):
        td = self.getWidgetTd(widget)
        if td != None:
            DOM.setAttribute(td, "align", align)

    def setCellVerticalAlignment(self, widget, align):
        td = self.getWidgetTd(widget)
        if td != None:
            DOM.setStyleAttribute(td, "verticalAlign", align)

    def setCellWidth(self, widget, width):
        td = DOM.getParent(widget.getElement())
        DOM.setAttribute(td, "width", width)

    def setSpacing(self, spacing):
        self.spacing = spacing
        DOM.setIntAttribute(self.table, "cellSpacing", spacing)

    def setPadding(self, padding):
        self.padding = padding
        DOM.setIntAttribute(self.table, "cellPadding", padding)


class HorizontalPanel(CellPanel):
    
    def __init__(self):
        CellPanel.__init__(self)

        self.horzAlign = HasHorizontalAlignment.ALIGN_LEFT
        self.vertAlign = HasVerticalAlignment.ALIGN_TOP
        
        self.tableRow = DOM.createTR()
        DOM.appendChild(self.getBody(), self.tableRow)
        
        DOM.setAttribute(self.getTable(), "cellSpacing", "0")
        DOM.setAttribute(self.getTable(), "cellPadding", "0")

    def add(self, widget):
        self.insert(widget, self.getWidgetCount())

    def getHorizontalAlignment(self):
        return self.horzAlign
    
    def getVerticalAlignment(self):
        return self.vertAlign

    def getWidget(self, index):
        return self.children[index]

    def getWidgetCount(self):
        return len(self.children)

    def getWidgetIndex(self, child):
        return self.children.index(child)

    def insert(self, widget, beforeIndex):
        widget.removeFromParent()
        
        td = DOM.createTD()
        DOM.insertChild(self.tableRow, td, beforeIndex)
        
        CellPanel.insert(self, widget, td, beforeIndex)
        
        self.setCellHorizontalAlignment(widget, self.horzAlign)
        self.setCellVerticalAlignment(widget, self.vertAlign)

    def remove(self, widget):
        if widget.getParent() != self:
            return False

        td = DOM.getParent(widget.getElement())
        DOM.removeChild(self.tableRow, td)

        CellPanel.remove(widget)
        return True

    def setHorizontalAlignment(self, align):
        self.horzAlign = align

    def setVerticalAlignment(self, align):
        self.vertAlign = align


class VerticalPanel(CellPanel):
    
    def __init__(self):
        CellPanel.__init__(self)

        self.horzAlign = HasHorizontalAlignment.ALIGN_LEFT
        self.vertAlign = HasVerticalAlignment.ALIGN_TOP
        
        DOM.setAttribute(self.getTable(), "cellSpacing", "0")
        DOM.setAttribute(self.getTable(), "cellPadding", "0")

    def add(self, widget):
        self.insert(widget, self.getWidgetCount())
    
    def getHorizontalAlignment(self):
        return self.horzAlign
    
    def getVerticalAlignment(self):
        return self.vertAlign

    def getWidget(self, index):
        return self.children[index]

    def getWidgetCount(self):
        return len(self.children)

    def getWidgetIndex(self, child):
        return self.children.index(child)
    
    def setWidget(self, index, widget):
        """Replace the widget at the given index with a new one"""
        existing = self.getWidget(index)
        if existing:
            self.remove(existing)
        self.insert(widget, index)
        
    def insert(self, widget, beforeIndex):
        widget.removeFromParent()
        
        tr = DOM.createTR()
        td = DOM.createTD()
        
        DOM.insertChild(self.getBody(), tr, beforeIndex)
        DOM.appendChild(tr, td)
        
        CellPanel.insert(self, widget, td, beforeIndex)
        
        self.setCellHorizontalAlignment(widget, self.horzAlign)
        self.setCellVerticalAlignment(widget, self.vertAlign)

    def remove(self, widget):
        if pyjslib.isNumber(widget):
            widget = self.getWidget(widget)
        
        if widget.getParent() != self:
            return False

        td = DOM.getParent(widget.getElement())
        tr = DOM.getParent(td)
        DOM.removeChild(self.getBody(), tr)
        
        CellPanel.remove(self, widget)
        return True

    def setHorizontalAlignment(self, align):
        self.horzAlign = align

    def setVerticalAlignment(self, align):
        self.vertAlign = align


class LayoutData:
    def __init__(self, direction):
        self.direction = direction
        self.hAlign = "left"
        self.height = ""
        self.td = None
        self.vAlign = "top"
        self.width = ""


class DockPanel(CellPanel):
    
    CENTER = "center"
    EAST = "east"
    NORTH = "north"
    SOUTH = "south"
    WEST = "west"
    
    def __init__(self):
        CellPanel.__init__(self)

        self.horzAlign = HasHorizontalAlignment.ALIGN_LEFT
        self.vertAlign = HasVerticalAlignment.ALIGN_TOP
        self.center = None
        self.dock_children = [] # TODO: can self.children be used instead?

        DOM.setIntAttribute(self.getTable(), "cellSpacing", 0)
        DOM.setIntAttribute(self.getTable(), "cellPadding", 0)

    def add(self, widget, direction):
        if direction == self.CENTER:
            if self.center != None:
                console.error("Only one CENTER widget may be added")
            self.center = widget

        layout = LayoutData(direction)
        widget.setLayoutData(layout)
        self.setCellHorizontalAlignment(widget, self.horzAlign)
        self.setCellVerticalAlignment(widget, self.vertAlign)
        
        self.dock_children.append(widget)
        self.realizeTable(widget)

    def getHorizontalAlignment(self):
        return self.horzAlign
    
    def getVerticalAlignment(self):
        return self.vertAlign

    def getWidgetDirection(self, widget):
        if widget.getParent() != self:
            return None
        return widget.getLayoutData().direction

    def remove(self, widget):
        if widget == self.center:
            self.center = None

        ret = CellPanel.remove(self, widget)
        if ret:
            self.dock_children.remove(widget)
            self.realizeTable(None)
        return ret

    def setCellHeight(self, widget, height):
        data = widget.getLayoutData()
        data.height = height
        if data.td:
            DOM.setStyleAttribute(data.td, "height", data.height)

    def setCellHorizontalAlignment(self, widget, align):
        data = widget.getLayoutData()
        data.hAlign = align
        if data.td:
            DOM.setAttribute(data.td, "align", data.hAlign)

    def setCellVerticalAlignment(self, widget, align):
        data = widget.getLayoutData()
        data.vAlign = align
        if data.td:
            DOM.setStyleAttribute(data.td, "verticalAlign", data.vAlign)

    def setCellWidth(self, widget, width):
        data = widget.getLayoutData()
        data.width = width
        if data.td:
            DOM.setStyleAttribute(data.td, "width", data.width)
            
    def setHorizontalAlignment(self, align):
        self.horzAlign = align

    def setVerticalAlignment(self, align):
        self.vertAlign = align

    def realizeTable(self, beingAdded):
        bodyElement = self.getBody()

        while DOM.getChildCount(bodyElement) > 0:
            DOM.removeChild(bodyElement, DOM.getChild(bodyElement, 0))

        rowCount = 1
        colCount = 1
        for child in self.dock_children:
            dir = child.getLayoutData().direction
            if dir == self.NORTH or dir == self.SOUTH:
                rowCount += 1
            elif dir == self.EAST or dir == self.WEST:
                colCount += 1

        rows = []
        for i in range(rowCount):
            rows[i] = DockPanelTmpRow()
            rows[i].tr = DOM.createTR()
            DOM.appendChild(bodyElement, rows[i].tr)

        westCol = 0
        eastCol = colCount - 1
        northRow = 0
        southRow = rowCount - 1
        centerTd = None
        
        for child in self.dock_children:
            layout = child.getLayoutData()
            
            td = DOM.createTD()
            layout.td = td
            DOM.setAttribute(layout.td, "align", layout.hAlign)
            DOM.setStyleAttribute(layout.td, "verticalAlign", layout.vAlign)
            DOM.setAttribute(layout.td, "width", layout.width)
            DOM.setAttribute(layout.td, "height", layout.height)
            
            if layout.direction == self.NORTH:
                DOM.insertChild(rows[northRow].tr, td, rows[northRow].center)
                self.appendAndMaybeAdopt(td, child.getElement(), beingAdded)
                DOM.setIntAttribute(td, "colSpan", eastCol - westCol + 1)
                northRow += 1
            elif layout.direction == self.SOUTH:
                DOM.insertChild(rows[southRow].tr, td, rows[southRow].center)
                self.appendAndMaybeAdopt(td, child.getElement(), beingAdded)
                DOM.setIntAttribute(td, "colSpan", eastCol - westCol + 1)
                southRow -= 1
            elif layout.direction == self.WEST:
                row = rows[northRow]
                DOM.insertChild(row.tr, td, row.center)
                row.center += 1
                self.appendAndMaybeAdopt(td, child.getElement(), beingAdded)
                DOM.setIntAttribute(td, "rowSpan", southRow - northRow + 1)
                westCol += 1
            elif layout.direction == self.EAST:
                row = rows[northRow]
                DOM.insertChild(row.tr, td, row.center)
                self.appendAndMaybeAdopt(td, child.getElement(), beingAdded)
                DOM.setIntAttribute(td, "rowSpan", southRow - northRow + 1)
                eastCol -= 1
            elif layout.direction == self.CENTER:
                centerTd = td

        if self.center != None:
            row = rows[northRow]
            DOM.insertChild(row.tr, centerTd, row.center)
            self.appendAndMaybeAdopt(centerTd, self.center.getElement(), beingAdded)

    def appendAndMaybeAdopt(self, parent, child, beingAdded):
        if beingAdded != None:
            if DOM.compare(child, beingAdded.getElement()):
                CellPanel.add(self, beingAdded, parent)
                return
        DOM.appendChild(parent, child)


class DockPanelTmpRow:
    center = 0
    tr = None


rootPanels = {}

class RootPanelCls(AbsolutePanel):
    def __init__(self, element=None):
        AbsolutePanel.__init__(self)
        if element == None:
            element = self.getBodyElement()
        
        self.setElement(element)
        self.onAttach()

    def getBodyElement(self):
        JS("""
        return $doc.body;
        """)
    
    @classmethod
    def get(cls, id=None):
        """
        
        """
        global rootPanels
        
        if rootPanels.has_key(id):
            return rootPanels[id]
        
        element = None
        if id:
            element = DOM.getElementById(id)
            if not element:
                return None

        if len(rootPanels) < 1:
            cls.hookWindowClosing()
        
        panel = RootPanel(element)
        rootPanels[id] = panel
        return panel

    @classmethod
    def hookWindowClosing(cls):
        Window.addWindowCloseListener(cls)

    @classmethod
    def onWindowClosed(cls):
        global rootPanels
        
        for panel in rootPanels.itervalues():
            panel.onDetach()

    @classmethod
    def onWindowClosing(cls):
        return None

def RootPanel(element):
	if pyjslib.isString(element):
		return RootPanelCls().get(element)
	return RootPanelCls(element)
	

class Hyperlink(Widget):

    def __init__(self, text="", asHTML=False, targetHistoryToken=""):
        Widget.__init__(self)
        self.clickListeners = []
        self.targetHistoryToken = ""

        self.setElement(DOM.createDiv())
        self.anchorElem = DOM.createAnchor()
        DOM.appendChild(self.getElement(), self.anchorElem)
        self.sinkEvents(Event.ONCLICK)
        self.setStyleName("gwt-Hyperlink")

        if asHTML:
            self.setHTML(text)
        else:
            self.setText(text)
        
        if targetHistoryToken:
            self.setTargetHistoryToken(targetHistoryToken)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def getHTML(self):
        return DOM.getInnerHTML(self.anchorElem)

    def getTargetHistoryToken(self):
        return self.targetHistoryToken

    def getText(self):
        return DOM.getInnerText(self.anchorElem)

    def onBrowserEvent(self, event):
        if DOM.eventGetType(event) == "click":
            for listener in self.clickListeners:
                if listener.onClick: listener.onClick(self, event)
                else: listener(self, event)
            History().newItem(self.targetHistoryToken)
            DOM.eventPreventDefault(event)

    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def setHTML(self, html):
        DOM.setInnerHTML(self.anchorElem, html)

    def setTargetHistoryToken(self, targetHistoryToken):
        self.targetHistoryToken = targetHistoryToken
        DOM.setAttribute(self.anchorElem, "href", "#" + targetHistoryToken)

    def setText(self, text):
        DOM.setInnerText(self.anchorElem, text)


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


class FlowPanel(ComplexPanel):
    def __init__(self):
        ComplexPanel.__init__(self)
        self.setElement(DOM.createDiv())
    
    def add(self, w):
        ComplexPanel.add(self, w, self.getElement())

    def getWidget(self, index):
        return self.children[index]

    def getWidgetCount(self):
        return len(self.children)

    def getWidgetIndex(self, child):
        return self.children.index(child)

    def remove(self, index):
        if pyjslib.isNumber(index):
            index = self.getWidget(index)
        return ComplexPanel.remove(self, index)


HTMLPanel_sUid = 0

class HTMLPanel(ComplexPanel):
    def __init__(self, html):
        ComplexPanel.__init__(self)
        self.setElement(DOM.createDiv())
        DOM.setInnerHTML(self.getElement(), html)

    def add(self, widget, id):
        element = self.getElementById(self.getElement(), id)
        if element == None:
            # throw new NoSuchElementException()
            return
        ComplexPanel.add(self, widget, element)

    def createUniqueId(self):
        global HTMLPanel_sUid
        
        HTMLPanel_sUid += 1
        return "HTMLPanel_" + HTMLPanel_sUid
    
    def getElementById(self, element, id):
        element_id = DOM.getAttribute(element, "id")
        if element_id != None and element_id == id:
            return element
        
        child = DOM.getFirstChild(element)
        while child != None:
            ret = self.getElementById(child, id)
            if ret != None:
                return ret
            child = DOM.getNextSibling(child)
        
        return None


class DeckPanel(ComplexPanel):
    def __init__(self):
        ComplexPanel.__init__(self)
        self.visibleWidget = None
        self.setElement(DOM.createDiv())

    def add(self, widget):
        self.insert(widget, self.getWidgetCount())

    def getVisibleWidget(self):
        return self.getWidgetIndex(self.visibleWidget)

    def getWidget(self, index):
        return self.children[index]

    def getWidgetCount(self):
        return len(self.children)

    def getWidgetIndex(self, child):
        return self.children.index(child)

    def insert(self, widget, beforeIndex):
        if (self.beforeIndex < 0) or (self.beforeIndex > self.getWidgetCount()):
            # throw new IndexOutOfBoundsException();
            return
        
        ComplexPanel.insert(self, widget, self.getElement(), beforeIndex)
        
        child = widget.getElement()
        DOM.setStyleAttribute(child, "width", "100%")
        DOM.setStyleAttribute(child, "height", "100%")
        widget.setVisible(False)

    def remove(self, widget):
        if pyjslib.isNumber(widget):
            widget = self.getWidget(widget)
            
        if not ComplexPanel.remove(self, widget):
            return False

        if self.visibleWidget == widget:
            self.visibleWidget = None

        return True

    def showWidget(self, index):
        self.checkIndex(index)

        if self.visibleWidget != None:
            self.visibleWidget.setVisible(False)

        self.visibleWidget = self.getWidget(index)
        self.visibleWidget.setVisible(True)

    def checkIndex(self, index):
        if (index < 0) or (index >= self.getWidgetCount()):
            # throw new IndexOutOfBoundsException();
            pass


class SimplePanel(Panel):
    """
        A panel which contains a single widget.  Useful if you have an area where
        you'd like to be able to replace the widget with another, or if you need to
        wrap something in a DIV.
    """
    def __init__(self, element=None):
        Panel.__init__(self)
        if element == None:
            element = DOM.createDiv()
        self.setElement(element)

    def add(self, widget):
        if self.getWidget() != None:
            console.error("SimplePanel can only contain one child widget")
            return
        self.setWidget(widget)

    def getWidget(self):
        if len(self.children):
            return self.children[0]
        return None

    def remove(self, widget):
        if self.getWidget() == widget:
            return False
        self.disown(widget)
        self.getContainerElement().removeChild(widget.getElement())
        del self.children[0]
        return True

    def getContainerElement(self):
        return self.getElement()

    def setWidget(self, widget):
        if self.getWidget() == widget:
            return

        if self.getWidget() != None:
            self.remove(self.getWidget())
        
        if widget != None:
            self.adopt(widget, self.getContainerElement())
            self.children[0] = widget


class ScrollPanel(SimplePanel):
    def __init__(self, child=None):
        SimplePanel.__init__(self)
        self.scrollListeners = []
        
        self.setAlwaysShowScrollBars(False)
        self.sinkEvents(Event.ONSCROLL)
        
        if child != None:
            self.setWidget(child)

    def addScrollListener(self, listener):
        self.scrollListeners.append(listener)

    def ensureVisible(self, item):
        scroll = self.getElement()
        element = item.getElement()
        self.ensureVisibleImpl(scroll, element)

    def getScrollPosition(self):
        return DOM.getIntAttribute(self.getElement(), "scrollTop")

    def getHorizontalScrollPosition(self):
        return DOM.getIntAttribute(self.getElement(), "scrollLeft")

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "scroll":
            for listener in self.scrollListeners:
                listener.onScroll(self, self.getHorizontalScrollPosition(), self.getScrollPosition())

    def removeScrollListener(self, listener):
        self.scrollListeners.remove(listener)

    def setAlwaysShowScrollBars(self, alwaysShow):
        if alwaysShow:
            style = "scroll"
        else:
            style = "auto"
        DOM.setStyleAttribute(self.getElement(), "overflow", style)

    def setScrollPosition(self, position):
        DOM.setIntAttribute(self.getElement(), "scrollTop", position)

    def setHorizontalScrollPosition(self, position):
        DOM.setIntAttribute(self.getElement(), "scrollLeft", position)

    def ensureVisibleImpl(self, scroll, e):
        JS("""
        if (!e) return;

        var item = e;
        var realOffset = 0;
        while (item && (item != scroll)) {
            realOffset += item.offsetTop;
            item = item.offsetParent;
            }

        scroll.scrollTop = realOffset - scroll.offsetHeight / 2;
        """)


class PopupPanel(SimplePanel):
    def __init__(self, autoHide=False):
        self.popupListeners = []
        self.showing = False
        self.autoHide = False
        
        SimplePanel.__init__(self, self.createElement())
        DOM.setStyleAttribute(self.getElement(), "position", "absolute")
        if autoHide:
            self.autoHide = autoHide

    def addPopupListener(self, listener):
        self.popupListeners.append(listener)

    def getPopupLeft(self):
        return DOM.getIntAttribute(self.getElement(), "offsetLeft")

    def getPopupTop(self):
        return DOM.getIntAttribute(self.getElement(), "offsetTop")

    # PopupImpl.createElement
    def createElement(self):
        return DOM.createDiv()
    
    def hide(self, autoClosed=False):
        if not self.showing:
            return
        self.showing = False
        DOM.removeEventPreview(self)
        
        RootPanel().get().remove(self)
        self.onHideImpl(self.getElement())
        for listener in self.popupListeners:
            if listener.onPopupClosed: listener.onPopupClosed(self, autoClosed)
            else: listener(self, autoClosed)

    def onEventPreview(self, event):
        target = DOM.eventGetTarget(event)
        event_targets_popup = target and DOM.isOrHasChild(self.getElement(), target)
        type = DOM.eventGetType(event)
        #print "onEventPreview popup", type, event_targets_popup
        if type == "keydown":
            return self.onKeyDownPreview(DOM.eventGetKeyCode(event), KeyboardListener.getKeyboardModifiers(self, event)) and event_targets_popup
        elif type == "keyup":
            return self.onKeyUpPreview(DOM.eventGetKeyCode(event), KeyboardListener.getKeyboardModifiers(self, event)) and event_targets_popup
        elif type == "keypress":
            return self.onKeyPressPreview(DOM.eventGetKeyCode(event), KeyboardListener.getKeyboardModifiers(self, event)) and event_targets_popup
        elif type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "click" or type == "dblclick":
            if DOM.getCaptureElement() == None:
		if not event_targets_popup and self.autoHide \
                                           and (type == "mousedown"):
                    self.hide(True)
                    return True

        return event_targets_popup

    def onKeyDownPreview(self, key, modifiers):
        return True

    def onKeyPressPreview(self, key, modifiers):
        return True

    def onKeyUpPreview(self, key, modifiers):
        return True

    # PopupImpl.onHide
    def onHideImpl(self, popup):
        pass

    # PopupImpl.onShow
    def onShowImpl(self, popup):
        pass
    
    def removePopupListener(self, listener):
        self.popupListeners.remove(listener)

    def setPopupPosition(self, left, top):
        if left < 0:
            left = 0
        if top < 0:
            top = 0

        element = self.getElement()
        DOM.setStyleAttribute(element, "left", left + "px")
        DOM.setStyleAttribute(element, "top", top + "px")

    def show(self):
        if self.showing:
            return
        
        self.showing = True
        DOM.addEventPreview(self)

        RootPanel().get().add(self)
        self.onShowImpl(self.getElement())


class MenuItem(UIObject):
    # also callable as:
    #   MenuItem(text, cmd)
    #   MenuItem(text, asHTML, cmd)
    #   MenuItem(text, subMenu)
    #   MenuItem(text, asHTML)
    def __init__(self, text, asHTML, subMenu=None):
        cmd = None
        if subMenu == None:
            if hasattr(asHTML, "execute"): # text, cmd
                cmd = asHTML
                asHTML = False
            elif hasattr(asHTML, "onShow"): # text, subMenu
                subMenu = asHTML
                asHTML = False
            # else: text, asHTML
        elif hasattr(subMenu, "execute"): # text, asHTML, cmd
            cmd = subMenu
            subMenu = None
        # else: text, asHTML, subMenu

        self.command = None
        self.parentMenu = None
        self.subMenu = None

        self.setElement(DOM.createTD())
        self.sinkEvents(Event.ONCLICK | Event.ONMOUSEOVER | Event.ONMOUSEOUT)
        self.setSelectionStyle(False)
                
        if asHTML:
            self.setHTML(text)
        else:
            self.setText(text)

        self.setStyleName("gwt-MenuItem")

        if cmd:
            self.setCommand(cmd)
        if subMenu:
            self.setSubMenu(subMenu)

    def getCommand(self):
        return self.command

    def getHTML(self):
        return DOM.getInnerHTML(self.getElement())

    def getParentMenu(self):
        return self.parentMenu
    
    def getSubMenu(self):
        return self.subMenu
    
    def getText(self):
        return DOM.getInnerText(self.getElement())

    def setCommand(self, cmd):
        self.command = cmd

    def setHTML(self, html):
        DOM.setInnerHTML(self.getElement(), html)
        
    def setSubMenu(self, subMenu):
        self.subMenu = subMenu
    
    def setText(self, text):
        DOM.setInnerText(self.getElement(), text)

    def setParentMenu(self, parentMenu):
        self.parentMenu = parentMenu

    def setSelectionStyle(self, selected):
        if selected:
            self.addStyleName("gwt-MenuItem-selected")
        else:
            self.removeStyleName("gwt-MenuItem-selected")


class MenuBar(Widget):
    def __init__(self, vertical=False):
        Widget.__init__(self)
        self.body = None
        self.items = []
        self.parentMenu = None
        self.popup = None
        self.selectedItem = None
        self.shownChildMenu = None
        self.vertical = False
        self.autoOpen = False

        Widget.__init__(self)
        
        table = DOM.createTable()
        self.body = DOM.createTBody()
        DOM.appendChild(table, self.body)

        if not vertical:
            tr = DOM.createTR()
            DOM.appendChild(self.body, tr)

        self.vertical = vertical
        
        outer = DOM.createDiv()
        DOM.appendChild(outer, table)
        self.setElement(outer)
        self.setStyleName("gwt-MenuBar")

    # also callable as:
    #   addItem(item)
    #   addItem(text, cmd)
    #   addItem(text, popup)
    #   addItem(text, asHTML, cmd)
    def addItem(self, item, asHTML=None, popup=None):
        if not hasattr(item, "setSubMenu"):
            item = MenuItem(item, asHTML, popup)

        if self.vertical:
            tr = DOM.createTR()
            DOM.appendChild(self.body, tr)
        else:
            tr = DOM.getChild(self.body, 0)

        DOM.appendChild(tr, item.getElement())
        
        item.setParentMenu(self)
        item.setSelectionStyle(False)
        self.items.append(item)
        return item
    
    def clearItems(self):
        container = self.getItemContainerElement()
        while DOM.getChildCount(container) > 0:
            DOM.removeChild(container, DOM.getChild(container, 0))
        self.items = []

    def getAutoOpen(self):
        return self.autoOpen

    def onBrowserEvent(self, event):
        Widget.onBrowserEvent(self, event)
        
        item = self.findItem(DOM.eventGetTarget(event))
        if item == None:
            return
        
        type = DOM.eventGetType(event)
        if type == "click":
            self.doItemAction(item, True)
        elif type == "mouseover":
            self.itemOver(item)
        elif type == "mouseout":
            self.itemOver(None)

    def onPopupClosed(self, sender, autoClosed):
        if autoClosed:
            self.closeAllParents()

        self.onHide()
        self.shownChildMenu = None
        self.popup = None

    def removeItem(self, item):
        idx = self.items.index(item)
        if idx == -1:
            return
        
        container = self.getItemContainerElement()
        DOM.removeChild(container, DOM.getChild(container, idx))
        del self.items[idx]

    def setAutoOpen(self, autoOpen):
        self.autoOpen = autoOpen

    def closeAllParents(self):
        curMenu = self
        while curMenu != None:
            curMenu.close()
        
            if (curMenu.parentMenu == None) and (curMenu.selectedItem != None):
                curMenu.selectedItem.setSelectionStyle(False)
                curMenu.selectedItem = None

            curMenu = curMenu.parentMenu

    def doItemAction(self, item, fireCommand):
        if (self.shownChildMenu != None) and (item.getSubMenu() == self.shownChildMenu):
            return

        if (self.shownChildMenu != None):
            self.shownChildMenu.onHide()
            self.popup.hide()

        if item.getSubMenu() == None:
            if fireCommand:
                self.closeAllParents()
    
                cmd = item.getCommand()
                if cmd != None:
                    DeferredCommand().add(cmd)
            return

        self.selectItem(item)
        self.popup = MenuBarPopupPanel(item)
        self.popup.addPopupListener(self)

        if self.vertical:
            self.popup.setPopupPosition(item.getAbsoluteLeft() + item.getOffsetWidth(), item.getAbsoluteTop())
        else:
            self.popup.setPopupPosition(item.getAbsoluteLeft(), item.getAbsoluteTop() + item.getOffsetHeight())

        self.shownChildMenu = item.getSubMenu()
        sub_menu = item.getSubMenu()
        sub_menu.parentMenu = self
        
        self.popup.show()

    def onDetach(self):
        if self.popup != None:
            self.popup.hide()

        Widget.onDetach(self)

    def itemOver(self, item):
        if item == None:
            if (self.selectedItem != None) and (self.shownChildMenu == self.selectedItem.getSubMenu()):
                return

        self.selectItem(item)
        
        if item != None:
            if (self.shownChildMenu != None) or (self.parentMenu != None) or self.autoOpen:
                self.doItemAction(item, False)

    def close(self):
        if self.parentMenu != None:
            self.parentMenu.popup.hide()

    def findItem(self, hItem):
        for item in self.items:
            if DOM.isOrHasChild(item.getElement(), hItem):
                return item
            
        return None

    def getItemContainerElement(self):
        if self.vertical:
            return self.body
        else:
            return DOM.getChild(self.body, 0)

    def onHide(self):
        if self.shownChildMenu != None:
            self.shownChildMenu.onHide()
            self.popup.hide()

    def onShow(self):
        if len(self.items) > 0:
            self.selectItem(self.items[0])

    def selectItem(self, item):
        if item == self.selectedItem:
            return

        if self.selectedItem != None:
            self.selectedItem.setSelectionStyle(False)
        
        if item != None:
            item.setSelectionStyle(True)

        self.selectedItem = item


class MenuBarPopupPanel(PopupPanel):
    def __init__(self, item):
        self.item = item
        PopupPanel.__init__(self, True)
        
        self.setWidget(item.getSubMenu())
        item.getSubMenu().onShow()

    def onEventPreview(self, event):
        type = DOM.eventGetType(event)
        if type == "click":
            target = DOM.eventGetTarget(event)
            parentMenuElement = self.item.getParentMenu().getElement()
            if DOM.isOrHasChild(parentMenuElement, target):
                return False
        return PopupPanel.onEventPreview(self, event)


class ListBox(FocusWidget):
    def __init__(self):
        self.changeListeners = []
        self.INSERT_AT_END = -1
        FocusWidget.__init__(self, DOM.createSelect())
        self.sinkEvents(Event.ONCHANGE)
        self.setStyleName("gwt-ListBox")

    def addChangeListener(self, listener):
        self.changeListeners.append(listener)

    def addItem(self, item, value = None):
        self.insertItem(item, value, self.INSERT_AT_END)

    def clear(self):
        h = self.getElement()
        while DOM.getChildCount(h) > 0:
            DOM.removeChild(h, DOM.getChild(h, 0))

    def getItemCount(self):
        return DOM.getChildCount(self.getElement())

    def getItemText(self, index):
        child = DOM.getChild(self.getElement(), index)
        return DOM.getInnerText(child)

    def getName(self):
        return DOM.getAttribute(self.getElement(), "name")

    def getSelectedIndex(self):
        return DOM.getIntAttribute(self.getElement(), "selectedIndex")

    def getValue(self, index):
        self.checkIndex(index)

        option = DOM.getChild(self.getElement(), index)
        return DOM.getAttribute(option, "value")

    def getVisibleItemCount(self):
        return DOM.getIntAttribute(self.getElement(), "size")

    # also callable as insertItem(item, index)
    def insertItem(self, item, value, index=None):
        if index == None:
            index = value
            value = None
        DOM.insertListItem(self.getElement(), item, value, index)

    def isItemSelected(self, index):
        self.checkIndex(index)
        option = DOM.getChild(self.getElement(), index)
        return DOM.getBooleanAttribute(option, "selected")

    def isMultipleSelect(self):
        return DOM.getBooleanAttribute(self.getElement(), "multiple")

    def onBrowserEvent(self, event):
        if DOM.eventGetType(event) == "change":
            for listener in self.changeListeners:
                if listener.onChange:
                    listener.onChange(self)
                else:
                    listener(self)
        else:
            FocusWidget.onBrowserEvent(self, event)
    
    def removeChangeListener(self, listener):
        self.changeListeners.remove(listener)

    def removeItem(self, idx):
        child = DOM.getChild(self.getElement(), idx)
        DOM.removeChild(self.getElement(), child)

    def setItemSelected(self, index, selected):
        self.checkIndex(index)
        option = DOM.getChild(self.getElement(), index)
        DOM.setBooleanAttribute(option, "selected", selected)

    def setMultipleSelect(self, multiple):
        DOM.setBooleanAttribute(self.getElement(), "multiple", multiple)
            
    def setName(self, name):
        DOM.setAttribute(self.getElement(), "name", name)

    def setSelectedIndex(self, index):
        DOM.setIntAttribute(self.getElement(), "selectedIndex", index)
    
    def selectValue(self, value):
        for n in range(self.getItemCount()):
            # http://code.google.com/p/pyjamas/issues/detail?id=63
            if self.getItemText(n) == value:
                self.setSelectedIndex(n)
                return n
        return None
    
    def setItemText(self, index, text):
        self.checkIndex(index)
        if text == None:
            console.error("Cannot set an option to have null text")
            return
        DOM.setOptionText(self.getElement(), text, index)

    def setValue(self, index, value):
        self.checkIndex(index)

        option = DOM.getChild(self.getElement(), index)
        DOM.setAttribute(option, "value", value)

    def setVisibleItemCount(self, visibleItems):
        DOM.setIntAttribute(self.getElement(), "size", visibleItems)

    def checkIndex(self, index):
        elem = self.getElement()
        if (index < 0) or (index >= DOM.getChildCount(elem)):
            #throw new IndexOutOfBoundsException();
            pass


class DialogBox(PopupPanel):
    def __init__(self, autoHide=None):
        PopupPanel.__init__(self, autoHide)
        self.caption = HTML()
        self.child = None
        self.dragging = False
        self.dragStartX = 0
        self.dragStartY = 0
        self.panel = FlexTable()
        
        self.panel.setWidget(0, 0, self.caption)
        self.panel.setHeight("100%")
        self.panel.setBorderWidth(0)
        self.panel.setCellPadding(0)
        self.panel.setCellSpacing(0)
        self.panel.getCellFormatter().setHeight(1, 0, "100%")
        self.panel.getCellFormatter().setWidth(1, 0, "100%")
        self.panel.getCellFormatter().setAlignment(1, 0, HasHorizontalAlignment.ALIGN_CENTER, HasVerticalAlignment.ALIGN_MIDDLE)
        PopupPanel.setWidget(self, self.panel)
    
        self.setStyleName("gwt-DialogBox")
        self.caption.setStyleName("Caption")
        self.caption.addMouseListener(self)

    def getHTML(self):
        return self.caption.getHTML()

    def getText(self):
        return self.caption.getText()

    def onEventPreview(self, event):
        # preventDefault on mosedown events, outside of the
        # dialog, to stop text-selection on dragging
        type = DOM.eventGetType(event)
        if type == 'mousedown':
            target = DOM.eventGetTarget(event)
            event_targets_popup = target and DOM.isOrHasChild(self.getElement(), target)
            if event_targets_popup:
                DOM.eventPreventDefault(event)
        return PopupPanel.onEventPreview(self, event)

    def onMouseDown(self, sender, x, y):
        self.dragging = True
        DOM.setCapture(self.caption.getElement())
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
            self.setPopupPosition(absX - self.dragStartX, absY - self.dragStartY)

    def onMouseUp(self, sender, x, y):
        self.dragging = False
        DOM.releaseCapture(self.caption.getElement())

    def remove(self, widget):
        if self.child != widget:
            return False

        self.panel.remove(widget)
        return True

    def setHTML(self, html):
        self.caption.setHTML(html)

    def setText(self, text):
        self.caption.setText(text)

    def doAttachChildren(self):
        PopupPanel.doAttachChildren(self)
        self.caption.onAttach()

    def doDetachChildren(self):
        PopupPanel.doDetachChildren(self)
        self.caption.onDetach()

    def setWidget(self, widget):
        if self.child != None:
            self.panel.remove(self.child)

        if widget != None:
            self.panel.setWidget(1, 0, widget)

        self.child = widget


class Frame(Widget):
    def __init__(self, url=""):
        Widget.__init__(self)
        self.setElement(DOM.createIFrame())

        if url:
            self.setUrl(url)

    def getUrl(self):
        return DOM.getAttribute(self.getElement(), "src")

    def setUrl(self, url):
        return DOM.setAttribute(self.getElement(), "src", url)


class ClickDelegatePanel(Composite):

    def __init__(self, p, child, cDelegate, kDelegate) :

        Composite.__init__(self)

        self.clickDelegate = cDelegate
        self.keyDelegate = kDelegate

        self.focusablePanel = SimplePanel(Focus().createFocusable())
        self.focusablePanel.setWidget(child)
        wrapperWidget = p.createTabTextWrapper()
        if wrapperWidget == None:
            self.initWidget(self.focusablePanel)
        else :
            wrapperWidget.setWidget(self.focusablePanel)
            self.initWidget(wrapperWidget)

        # bug in click handling - Labels steal clicks!
        child.addClickListener(self)
        if hasattr(child, "addKeyboardListener"):
            child.addKeyboardListener(kDelegate)

        self.sinkEvents(Event.ONCLICK | Event.ONKEYDOWN)

    # receive Label's onClick and pass it through, pretending it came from us
    def onClick(self, sender, event):
        self.clickDelegate.onClick(self, event)

    def getFocusablePanel(self):
        return self.focusablePanel

    def onBrowserEvent(self, event) :
        type = DOM.eventGetType(event)
        if type == "click":
            self.onClick(self, event)

        elif type == "keydown":
            modifiers = KeyboardListener().getKeyboardModifiers(event)
            if hasattr(self.keyDelegate, "onKeyDown"):
                self.keyDelegate.onKeyDown(self, DOM.eventGetKeyCode(event),
                                       modifiers)


class TabBar(Composite):

    STYLENAME_DEFAULT = "gwt-TabBarItem"

    def __init__(self):
        Composite.__init__(self)
        self.panel = HorizontalPanel()
        self.selectedTab = None
        self.tabListeners = []
        
        self.initWidget(self.panel)
        self.sinkEvents(Event.ONCLICK)
        self.setStyleName("gwt-TabBar")
        
        self.panel.setVerticalAlignment(HasAlignment.ALIGN_BOTTOM)
        
        first = HTML("&nbsp;", True)
        rest = HTML("&nbsp;", True)
        first.setStyleName("gwt-TabBarFirst")
        rest.setStyleName("gwt-TabBarRest")
        first.setHeight("100%")
        rest.setHeight("100%")
        
        self.panel.add(first)
        self.panel.add(rest)
        first.setHeight("100%")
        self.panel.setCellHeight(first, "100%")
        self.panel.setCellWidth(rest, "100%")

    def addTab(self, text, asHTML=False):
        self.insertTab(text, asHTML, self.getTabCount())

    def addTabListener(self, listener):
        self.tabListeners.append(listener)

    def getSelectedTab(self):
        if self.selectedTab == None:
            return -1
        return self.panel.getWidgetIndex(self.selectedTab) - 1

    def getTabCount(self):
        return self.panel.getWidgetCount() - 2

    def getTabHTML(self, index):
        if index >= self.getTabCount():
            return None
        delPanel = self.panel.getWidget(index + 1)
        focusablePanel = delPanel.getFocusablePanel()
        widget = focusablePanel.getWidget()
        if hasattr(widget, "getHTML"):
            return widget.getHTML()
        elif hasattr(widget, "getText"): # assume it's a Label if it has getText
            return widget.getText()
        else:
            fpe = DOM.getParent(self.focusablePanel.getElement())
            return DOM.getInnerHTML(fpe)

    def createTabTextWrapper(self):
        return None

    def insertTab(self, text, asHTML, beforeIndex=None):
        """ 1st arg can, instead of being 'text', be a widget
        """
        if beforeIndex == None:
            beforeIndex = asHTML
            asHTML = False

        if (beforeIndex < 0) or (beforeIndex > self.getTabCount()):
            #throw new IndexOutOfBoundsException();
            pass

        if pyjslib.isString(text):
            if asHTML:
                item = HTML(text)
            else:
                item = Label(text)
            item.setWordWrap(False)
        else:
            # passing in a widget, it's expected to have its own style
            item = text

        self.insertTabWidget(item, beforeIndex)

    def insertTabWidget(self, widget, beforeIndex):

        delWidget = ClickDelegatePanel(self, widget, self, self)
        delWidget.setStyleName(self.STYLENAME_DEFAULT)

        focusablePanel = delWidget.getFocusablePanel()
        self.panel.insert(delWidget, beforeIndex + 1)

        self.setStyleName(DOM.getParent(delWidget.getElement()),
                          self.STYLENAME_DEFAULT + "-wrapper", True)

        #print "insertTabWidget", DOM.getParent(delWidget.getElement()), DOM.getAttribute(DOM.getParent(delWidget.getElement()), "className")


    def onClick(self, sender):
        for i in range(1, self.panel.getWidgetCount() - 1):
            if self.panel.getWidget(i) == sender:
                return self.selectTab(i - 1)
        return False

    def removeTab(self, index):
        self.checkTabIndex(index)

        toRemove = self.panel.getWidget(index + 1)
        if toRemove == self.selectedTab:
            self.selectedTab = None
        self.panel.remove(toRemove)

    def removeTabListener(self, listener):
        self.tabListeners.remove(listener)

    def selectTab(self, index):
        self.checkTabIndex(index)
        
        for listener in self.tabListeners:
            if not listener.onBeforeTabSelected(self, index):
                return False
        
        self.setSelectionStyle(self.selectedTab, False)
        if index == -1:
            self.selectedTab = None
            return True

        self.selectedTab = self.panel.getWidget(index + 1)
        self.setSelectionStyle(self.selectedTab, True)

        for listener in self.tabListeners:
            listener.onTabSelected(self, index)

        return True

    def checkTabIndex(self, index):
        if (index < -1) or (index >= self.getTabCount()):
            #throw new IndexOutOfBoundsException();
            pass

    def setSelectionStyle(self, item, selected):
        if item != None:
            if selected:
                item.addStyleName("gwt-TabBarItem-selected")
                self.setStyleName(DOM.getParent(item.getElement()),
                                "gwt-TabBarItem-wrapper-selected", True)

            else:
                item.removeStyleName("gwt-TabBarItem-selected")
                self.setStyleName(DOM.getParent(item.getElement()),
                                "gwt-TabBarItem-wrapper-selected", False)


class TabPanel(Composite):
    def __init__(self, tabBar=None):
        Composite.__init__(self)
        self.tab_children = [] # TODO: can self.children be used instead?
        self.deck = DeckPanel()
        if tabBar == None:
            self.tabBar = TabBar()
        else:
            self.tabBar = tabBar
        self.tabListeners = []

        panel = VerticalPanel()
        panel.add(self.tabBar)
        panel.add(self.deck)

        panel.setCellHeight(self.deck, "100%")
        self.tabBar.setWidth("100%")
        self.tabBar.addTabListener(self)
        self.initWidget(panel)
        self.setStyleName("gwt-TabPanel")
        self.deck.setStyleName("gwt-TabPanelBottom")
        
    def add(self, widget, tabText=None, asHTML=False):
        if tabText == None:
            console.error("A tabText parameter must be specified with add().")
        self.insert(widget, tabText, asHTML, self.getWidgetCount())

    def addTabListener(self, listener):
        self.tabListeners.append(listener)

    def clear(self):
        while self.getWidgetCount() > 0:
            self.remove(self.getWidget(0))

    def getDeckPanel(self):
        return self.deck

    def getTabBar(self):
        return self.tabBar

    def getWidget(self, index):
        return self.tab_children[index]

    def getWidgetCount(self):
        return len(self.tab_children)

    def getWidgetIndex(self, child):
        return self.tab_children.index(child)

    def insert(self, widget, tabText, asHTML, beforeIndex=None):
        if beforeIndex == None:
            beforeIndex = asHTML
            asHTML = False

        self.tab_children.insert(beforeIndex, widget)
        self.tabBar.insertTab(tabText, asHTML, beforeIndex)
        self.deck.insert(widget, beforeIndex)

    def __iter__(self):
        return self.tab_children.__iter__()

    def onBeforeTabSelected(self, sender, tabIndex):
        for listener in self.tabListeners:
            if not listener.onBeforeTabSelected(sender, tabIndex):
                return False
        return True

    def onTabSelected(self, sender, tabIndex):
        self.deck.showWidget(tabIndex)
        for listener in self.tabListeners:
            listener.onTabSelected(sender, tabIndex)

    def remove(self, widget):
        if pyjslib.isNumber(widget):
            widget = self.getWidget(widget)

        index = self.getWidgetIndex(widget)
        if index == -1:
            return False

        self.tab_children.remove(widget)
        self.tabBar.removeTab(index)
        self.deck.remove(widget)
        return True

    def removeTabListener(self, listener):
        self.tabListeners.remove(listener)

    def selectTab(self, index):
        self.tabBar.selectTab(index)


class StackPanel(ComplexPanel):

    def __init__(self):
        ComplexPanel.__init__(self)
        self.body = None
        self.visibleStack = -1
        
        table = DOM.createTable()
        self.setElement(table)
        
        self.body = DOM.createTBody()
        DOM.appendChild(table, self.body)
        DOM.setIntAttribute(table, "cellSpacing", 0)
        DOM.setIntAttribute(table, "cellPadding", 0)
        
        DOM.sinkEvents(table, Event.ONCLICK)
        self.setStyleName("gwt-StackPanel")
        
    def add(self, widget, stackText="", asHTML=False):
        widget.removeFromParent()
        index = self.getWidgetCount()
        
        tr = DOM.createTR()
        td = DOM.createTD()
        DOM.appendChild(self.body, tr)
        DOM.appendChild(tr, td)
        self.setStyleName(td, "gwt-StackPanelItem", True)
        DOM.setIntAttribute(td, "__index", index)
        DOM.setAttribute(td, "height", "1px")
        
        tr = DOM.createTR()
        td = DOM.createTD()
        DOM.appendChild(self.body, tr)
        DOM.appendChild(tr, td)
        DOM.setAttribute(td, "height", "100%")
        DOM.setAttribute(td, "vAlign", "top")

        ComplexPanel.add(self, widget, td)
        
        self.setStackVisible(index, False)
        if self.visibleStack == -1:
            self.showStack(0)
            
        if stackText != "":
            self.setStackText(self.getWidgetCount() - 1, stackText, asHTML)

    def getWidget(self, index):
        return self.children[index]

    def getWidgetCount(self):
        return len(self.children)

    def getWidgetIndex(self, child):
        return self.children.index(child)

    def onBrowserEvent(self, event):
        if DOM.eventGetType(event) == "click":
            index = self.getDividerIndex(DOM.eventGetTarget(event))
            if index != -1:
                self.showStack(index)

    # also callable as remove(child) and remove(index)
    def remove(self, child, index=None):
        if index == None:
            if pyjslib.isNumber(child):
                index = child
                child = self.getWidget(child)
            else:
                index = self.getWidgetIndex(child)

        if child.getParent() != self:
            return False

        if self.visibleStack == index:
            self.visibleStack = -1
        elif self.visibleStack > index:
            self.visibleStack -= 1

        rowIndex = 2 * index
        tr = DOM.getChild(self.body, rowIndex)
        DOM.removeChild(self.body, tr)
        tr = DOM.getChild(self.body, rowIndex)
        DOM.removeChild(self.body, tr)
        ComplexPanel.remove(self, child)
        rows = self.getWidgetCount() * 2

        #for (int i = rowIndex; i < rows; i = i + 2) {
        for i in range(rowIndex, rows, 2):
            childTR = DOM.getChild(self.body, i)
            td = DOM.getFirstChild(childTR)
            curIndex = DOM.getIntAttribute(td, "__index")
            #assert (curIndex == (i / 2) - 1);
            DOM.setIntAttribute(td, "__index", index)
            index += 1

        return True

    def setStackText(self, index, text, asHTML=False):
        if index >= self.getWidgetCount():
            return

        td = DOM.getChild(DOM.getChild(self.body, index * 2), 0)
        if asHTML:
            DOM.setInnerHTML(td, text)
        else:
            DOM.setInnerText(td, text)
    
    def showStack(self, index):
        if (index >= self.getWidgetCount()) or (index == self.visibleStack):
            return

        if self.visibleStack >= 0:
            self.setStackVisible(self.visibleStack, False)
        
        self.visibleStack = index
        self.setStackVisible(self.visibleStack, True)

    def getDividerIndex(self, elem):
        while (elem != None) and not DOM.compare(elem, self.getElement()):
            expando = DOM.getAttribute(elem, "__index")
            if expando != None:
                return int(expando)
            
            elem = DOM.getParent(elem)
        
        return -1

    def setStackVisible(self, index, visible):
        tr = DOM.getChild(self.body, (index * 2))
        if tr == None:
            return

        td = DOM.getFirstChild(tr)
        self.setStyleName(td, "gwt-StackPanelItem-selected", visible)
        
        tr = DOM.getChild(self.body, (index * 2) + 1)
        self.setVisible(tr, visible)
        self.getWidget(index).setVisible(visible)

    def getSelectedIndex(self):
        return self.visibleStack


class TextBoxBase(FocusWidget):
    ALIGN_CENTER = "center"
    ALIGN_JUSTIFY = "justify"
    ALIGN_LEFT = "left"
    ALIGN_RIGHT = "right"
    
    def __init__(self, element):
        self.changeListeners = []
        self.clickListeners = []
        self.currentEvent = None
        self.keyboardListeners = []
        
        FocusWidget.__init__(self, element)
        self.sinkEvents(Event.ONCHANGE)

    def addChangeListener(self, listener):
        self.changeListeners.append(listener)
    
    def addClickListener(self, listener):
        self.clickListeners.append(listener)
        
    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)
        
    def cancelKey(self):
        if self.currentEvent != None:
            DOM.eventPreventDefault(self.currentEvent)
    
    def getCursorPos(self):
        JS("""
        try {
            var element = this.getElement()
            return element.selectionStart;
        } catch (e) {
            return 0;
        }
        """)

    def getName(self):
        return DOM.getAttribute(self.getElement(), "name")

    def getSelectedText(self):
        start = self.getCursorPos()
        length = self.getSelectionLength()
        text = self.getText()
        return text[start:start + length]
    
    def getSelectionLength(self):
        JS("""
        try{
            var element = this.getElement()
            return element.selectionEnd - element.selectionStart;
        } catch (e) {
            return 0;
        }
        """)

    def getText(self):
        return DOM.getAttribute(self.getElement(), "value")
    
    # BUG: keyboard & click events already fired in FocusWidget.onBrowserEvent
    def onBrowserEvent(self, event):
        FocusWidget.onBrowserEvent(self, event)

        type = DOM.eventGetType(event)
        #if DOM.eventGetTypeInt(event) & Event.KEYEVENTS:
            #self.currentEvent = event
            #KeyboardListener.fireKeyboardEvent(self.keyboardListeners, self, event)
            #self.currentEvent = None
        #elif type == "click":
            #for listener in self.clickListeners:
                #if listener.onClick: listener.onClick(self, event)
                #else: listener(self)
        #elif type == "change":
            #for listener in self.changeListeners:
                #if listener.onChange: listener.onChange(self, event)
                #else: listener(self)
        if type == "change":
            for listener in self.changeListeners:
                if listener.onChange: listener.onChange(self)
                else: listener(self)

    def removeChangeListener(self, listener):
        self.changeListeners.remove(listener)
    
    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def removeKeyboardListener(self, listener):
        self.keyboardListeners.remove(listener)

    def selectAll(self):
        length = len(self.getText())
        if length > 0:
            self.setSelectionRange(0, length)

    def setCursorPos(self, pos):
        self.setSelectionRange(pos, 0)
        
    def setKey(self, key):
        if self.currentEvent != None:
            DOM.eventSetKeyCode(self.currentEvent, key)

    def setName(self, name):
        DOM.setAttribute(self.getElement(), "name", name)

    def setSelectionRange(self, pos, length):
        if length < 0:
            # throw new IndexOutOfBoundsException("Length must be a positive integer. Length: " + length);
            console.error("Length must be a positive integer. Length: " + length)

        if (pos < 0) or (length + pos > len(self.getText())):
            #throw new IndexOutOfBoundsException("From Index: " + pos + "  To Index: " + (pos + length) + "  Text Length: " + getText().length());
            console.error("From Index: " + pos + "  To Index: " + (pos + length) + "  Text Length: " + len(self.getText()))

        element = self.getElement()
        element.setSelectionRange(pos, pos + length)
        
    def setText(self, text):
        DOM.setAttribute(self.getElement(), "value", text)

    def setTextAlignment(self, align):
        DOM.setStyleAttribute(self.getElement(), "textAlign", align)


class TextBox(TextBoxBase):
    def __init__(self):
        TextBoxBase.__init__(self, DOM.createInputText())
        self.setStyleName("gwt-TextBox")
        
    def getMaxLength(self):
        return DOM.getIntAttribute(self.getElement(), "maxLength")
    
    def getVisibleLength(self):
        return DOM.getIntAttribute(self.getElement(), "size")
    
    def setMaxLength(self, length):
        DOM.setIntAttribute(self.getElement(), "maxLength", length)
    
    def setVisibleLength(self, length):
        DOM.setIntAttribute(self.getElement(), "size", length)
        

class PasswordTextBox(TextBoxBase):
    def __init__(self):
        TextBoxBase.__init__(self, DOM.createInputPassword())
        self.setStyleName("gwt-PasswordTextBox")


class TextArea(TextBoxBase):
    """
    HTML textarea widget, allowing multi-line text entry.  Use setText/getText to 
    get and access the current text.
    """
    def __init__(self):
        TextBoxBase.__init__(self, DOM.createTextArea())
        self.setStyleName("gwt-TextArea")
    
    def getCharacterWidth(self):
        return DOM.getIntAttribute(self.getElement(), "cols")
    
    def getCursorPos(self):
        return TextBoxBase.getCursorPos(self)
    
    def getVisibleLines(self):
        return DOM.getIntAttribute(self.getElement(), "rows")
    
    def setCharacterWidth(self, width):
        DOM.setIntAttribute(self.getElement(), "cols", width)
    
    def setVisibleLines(self, lines):
        DOM.setIntAttribute(self.getElement(), "rows", lines)


class TreeContentPanel(SimplePanel):
    def __init__(self, element):
        SimplePanel.__init__(self, element)
        self.tree_item = None

    def getTreeItem(self):
        return self.tree_item

    def setTreeItem(self, tree_item):
        self.tree_item = tree_item

    def setParent(self, widget):
        # throw new UnsupportedOperationException("Cannot directly setParent on a WidgetTreeItem's ContentPanel");
        console.error("Cannot directly setParent on a WidgetTreeItem's ContentPanel")

    def treeSetParent(self, widget):
        SimplePanel.setParent(self, widget)


class TreeItem(UIObject):

    # also callable as TreeItem(widget)
    def __init__(self, html=None):
        self.children = []
        self.contentPanel = None
        self.itemTable = None
        self.contentElem = None
        self.imgElem = None
        self.childSpanElem = None
        self.open = False
        self.parent = None
        self.selected = False
        self.tree = None
        self.userObject = None

        self.setElement(DOM.createDiv())
        
        self.itemTable = DOM.createTable()
        self.contentElem = DOM.createSpan()
        self.childSpanElem = DOM.createSpan()
        self.imgElem = DOM.createImg()

        tbody = DOM.createTBody()
        tr = DOM.createTR()
        tdImg = DOM.createTD()
        tdContent = DOM.createTD()
        DOM.appendChild(self.itemTable, tbody)
        DOM.appendChild(tbody, tr)
        DOM.appendChild(tr, tdImg)
        DOM.appendChild(tr, tdContent)
        DOM.setStyleAttribute(tdImg, "verticalAlign", "middle")
        DOM.setStyleAttribute(tdContent, "verticalAlign", "middle")
        DOM.setStyleAttribute(self.getElement(), "cursor", "pointer")
  
        DOM.appendChild(self.getElement(), self.itemTable)
        DOM.appendChild(self.getElement(), self.childSpanElem)
        DOM.appendChild(tdImg, self.imgElem)
        DOM.appendChild(tdContent, self.contentElem)
        
        DOM.setAttribute(self.getElement(), "position", "relative")
        DOM.setStyleAttribute(self.contentElem, "display", "inline")
        DOM.setStyleAttribute(self.getElement(), "whiteSpace", "nowrap")
        DOM.setAttribute(self.itemTable, "whiteSpace", "nowrap")
        DOM.setStyleAttribute(self.childSpanElem, "whiteSpace", "nowrap")
        self.setStyleName(self.contentElem, "gwt-TreeItem", True)

        if html != None:
            if pyjslib.isString(html):
                self.setHTML(html)
            else:
                self.setWidget(html)
    
    # also callable as addItem(widget) and addItem(itemText)
    def addItem(self, item):
        if not hasattr(item, "getTree"):
            #if not item.getTree:
            item = TreeItem(item)

        if (item.getParentItem() != None) or (item.getTree() != None):
            item.remove()

        item.setTree(self.tree)
        item.setParentItem(self)
        self.children.append(item)
        DOM.setStyleAttribute(item.getElement(), "marginLeft", 16 + "px")
        DOM.appendChild(self.childSpanElem, item.getElement())
        if len(self.children) == 1:
            self.updateState()

        return item

    def getChild(self, index):
        if (index < 0) or (index >= len(self.children)):
            return None
        
        return self.children[index]
    
    def getChildCount(self):
        return len(self.children)

    def getChildIndex(self, child):
        return self.children.index(child)

    def getHTML(self):
        return DOM.getInnerHTML(self.contentElem)

    def getText(self):
        return DOM.getInnerText(self.contentElem)
    
    def getParentItem(self):
        return self.parent

    def getState(self):
        return self.open

    def getTree(self):
        return self.tree

    def getUserObject(self):
        return self.userObject

    def getWidget(self):
        if self.contentPanel == None:
            return None

        return self.contentPanel.getWidget()

    def isSelected(self):
        return self.selected
    
    def remove(self):
        if self.parent != None:
            self.parent.removeItem(self)
        elif self.tree != None:
            self.tree.removeItem(self)

    def removeItem(self, item):
        if item not in self.children:
            return

        item.setTree(None)
        item.setParentItem(None)
        self.children.remove(item)
        DOM.removeChild(self.childSpanElem, item.getElement())
        if len(self.children) == 0:
            self.updateState()
            
    def removeItems(self):
        while self.getChildCount() > 0:
            self.removeItem(self.getChild(0))

    def setHTML(self, html):
        self.clearContentPanel()
        DOM.setInnerHTML(self.contentElem, html)

    def setText(self, text):
        self.clearContentPanel()
        DOM.setInnerText(self.contentElem, text)

    def setSelected(self, selected):
        if self.selected == selected:
            return
        self.selected = selected
        self.setStyleName(self.contentElem, "gwt-TreeItem-selected", selected)

    def setState(self, open, fireEvents=True):
        if open and len(self.children) == 0:
            return

        self.open = open
        self.updateState()
        
        if fireEvents:
            self.tree.fireStateChanged(self)

    def setUserObject(self, userObj):
        self.userObject = userObj

    def setWidget(self, widget):
        self.ensureContentPanel()
        self.contentPanel.setWidget(widget)

    def clearContentPanel(self):
        if self.contentPanel != None:
            child = self.contentPanel.getWidget()
            if child != None:
                self.contentPanel.remove(child)

            if self.tree != None:
                self.tree.disown(self.contentPanel)
                self.contentPanel = None

    def ensureContentPanel(self):
        if self.contentPanel == None:
            DOM.setInnerHTML(self.contentElem, "")
            self.contentPanel = TreeContentPanel(self.contentElem)
            self.contentPanel.setTreeItem(self)
            if self.getTree() != None:
                self.tree.adopt(self.contentPanel)

    def addTreeItems(self, accum):
        for item in self.children:
            accum.append(item)
            item.addTreeItems(accum)

    def getChildren(self):
        return self.children

    def getContentElem(self):
        return self.contentElem

    def getContentHeight(self):
        return DOM.getIntAttribute(self.itemTable, "offsetHeight")

    def getImageElement(self):
        return self.imgElem

    def getTreeTop(self):
        item = self
        ret = 0

        while item != None:
            ret += DOM.getIntAttribute(item.getElement(), "offsetTop")
            item = item.getParentItem()

        return ret

    def getFocusableWidget(self):
        widget = self.getWidget()
        if hasattr(widget, "setFocus"):
            return widget
        return None

    def imgSrc(self, img):
        if self.tree == None:
            return img
        src = self.tree.getImageBase() + img
        return src

    def setParentItem(self, parent):
        self.parent = parent

    def setTree(self, tree):
        if self.tree == tree:
            return

        if self.tree != None:
            if self.tree.getSelectedItem() == self:
                self.tree.setSelectedItem(None)

            if self.contentPanel != None:
                self.tree.disown(self.contentPanel)
    
        self.tree = tree
        for child in self.children:
            child.setTree(tree)
        self.updateState()
        if tree != None and self.contentPanel != None:
                tree.adopt(self.contentPanel)

    def updateState(self):
        if len(self.children) == 0:
            self.setVisible(self.childSpanElem, False)
            DOM.setAttribute(self.imgElem, "src", self.imgSrc("tree_white.gif"))
            return
            
        if self.open:
            self.setVisible(self.childSpanElem, True)
            DOM.setAttribute(self.imgElem, "src", self.imgSrc("tree_open.gif"))
        else:
            self.setVisible(self.childSpanElem, False)
            DOM.setAttribute(self.imgElem, "src", self.imgSrc("tree_closed.gif"))

    def updateStateRecursive(self):
        self.updateState()
        for i in range(len(self.children)):
            child = self.children[i]
            child.updateStateRecursive()


class RootTreeItem(TreeItem):
    def addItem(self, item):
        if (item.getParentItem() != None) or (item.getTree() != None):
            item.remove()
        item.setTree(self.getTree())
        
        item.setParentItem(None)
        self.children.append(item)
        
        DOM.setIntStyleAttribute(item.getElement(), "marginLeft", 0)

    def removeItem(self, item):
        if item not in self.children:
            return
        
        item.setTree(None)
        item.setParentItem(None)
        self.children.remove(item)


class Tree(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.root = None
        self.childWidgets = Set()
        self.curSelection = None
        self.focusable = None
        self.focusListeners = []
        self.mouseListeners = []
        self.imageBase = pygwt.getModuleBaseURL()
        self.keyboardListeners = []
        self.listeners = []
        self.lastEventType = ""

        self.setElement(DOM.createDiv())
        DOM.setStyleAttribute(self.getElement(), "position", "relative")
        self.focusable = Focus.createFocusable()
        DOM.setStyleAttribute(self.focusable, "fontSize", "0")
        DOM.setStyleAttribute(self.focusable, "position", "absolute")
        DOM.setIntStyleAttribute(self.focusable, "zIndex", -1)
        DOM.appendChild(self.getElement(), self.focusable)

        self.sinkEvents(Event.MOUSEEVENTS | Event.ONCLICK | Event.KEYEVENTS)
        #DOM.sinkEvents(self.focusable, Event.FOCUSEVENTS | Event.KEYEVENTS | DOM.getEventsSunk(self.focusable))
        DOM.sinkEvents(self.focusable, Event.FOCUSEVENTS)

        self.root = RootTreeItem()
        self.root.setTree(self)
        self.setStyleName("gwt-Tree")

    def add(self, widget):
        self.addItem(widget)

    def addFocusListener(self, listener):
        self.focusListeners.append(listener)

    def addItem(self, item):
        if pyjslib.isString(item):
            item = TreeItem(item)

        ret = self.root.addItem(item)
        DOM.appendChild(self.getElement(), item.getElement())

        return ret

    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)
    
    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def addTreeListener(self, listener):
        self.listeners.append(listener)

    def clear(self):
        size = self.root.getChildCount()
        for i in range(size, 0, -1):
            self.root.getChild(i-1).remove()

    def ensureSelectedItemVisible(self):
        if self.curSelection == None:
            return

        parent = self.curSelection.getParentItem()
        while parent != None:
            parent.setState(True)
            parent = parent.getParentItem()

    def getImageBase(self):
        return self.imageBase
    
    def getItem(self, index):
        return self.root.getChild(index)

    def getItemCount(self):
        return self.root.getChildCount()

    def getSelectedItem(self):
        return self.curSelection

    def getTabIndex(self):
        return Focus.getTabIndex(self, self.focusable)

    def __iter__(self):
        return self.childWidgets.__iter__()

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)

        if type == "click":
            e = DOM.eventGetTarget(event)
            if not self.shouldTreeDelegateFocusToElement(e):
                self.setFocus(True)
        elif type == "mousedown":
            MouseListener.fireMouseEvent(self, self.mouseListeners, self, event)
            self.elementClicked(self.root, DOM.eventGetTarget(event))
        elif type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener.fireMouseEvent(self, self.mouseListeners, self, event)
        elif type == "blur" or type == "focus":
            FocusListener.fireFocusEvent(self, self.focusListeners, self, event)
        elif type == "keydown":
            if self.curSelection == None:
                if self.root.getChildCount() > 0:
                    self.onSelection(self.root.getChild(0), True)
                Widget.onBrowserEvent(self, event)
                return

            if self.lastEventType == "keydown":
                return

            keycode = DOM.eventGetKeyCode(event)
            if keycode == KeyboardListener.KEY_UP:
                self.moveSelectionUp(self.curSelection, True)
                DOM.eventPreventDefault(event)
            elif keycode == KeyboardListener.KEY_DOWN:
                self.moveSelectionDown(self.curSelection, True)
                DOM.eventPreventDefault(event)
            elif keycode == KeyboardListener.KEY_LEFT:
                if self.curSelection.getState():
                    self.curSelection.setState(False)
                DOM.eventPreventDefault(event)
            elif keycode == KeyboardListener.KEY_RIGHT:
                if not self.curSelection.getState():
                    self.curSelection.setState(True)
                DOM.eventPreventDefault(event)
        elif type == "keyup":
            if DOM.eventGetKeyCode(event) == KeyboardListener.KEY_TAB:
                chain = []
                self.collectElementChain(chain, self.getElement(), DOM.eventGetTarget(event))
                item = self.findItemByChain(chain, 0, self.root)
                if item != self.getSelectedItem():
                    self.setSelectedItem(item, True)
        elif type == "keypress":
            KeyboardListener.fireKeyboardEvent(self, self.keyboardListeners, self, event)
        
        Widget.onBrowserEvent(self, event)
        self.lastEventType = type

    def remove(self, widget):
        #throw new UnsupportedOperationException("Widgets should never be directly removed from a tree")
        console.error("Widgets should never be directly removed from a tree")

    def removeFocusListener(self, listener):
        self.focusListeners.remove(listener)

    def removeItem(self, item):
        self.root.removeItem(item)
        DOM.removeChild(self.getElement(), item.getElement())

    def removeItems(self):
        while self.getItemCount() > 0:
            self.removeItem(self.getItem(0))

    def removeKeyboardListener(self, listener):
        self.keyboardListeners.remove(listener)

    def removeTreeListener(self, listener):
        self.listeners.remove(listener)

    def setAccessKey(self, key):
        Focus.setAccessKey(self, self.focusable, key)

    def setFocus(self, focus):
        if focus:
            Focus.focus(self, self.focusable)
        else:
            Focus.blur(self, self.focusable)

    def setImageBase(self, baseUrl):
        self.imageBase = baseUrl
        self.root.updateStateRecursive()

    def setSelectedItem(self, item, fireEvents=True):
        if item == None:
            if self.curSelection == None:
                return
            self.curSelection.setSelected(False)
            self.curSelection = None
            return

        self.onSelection(item, fireEvents)
    
    def setTabIndex(self, index):
        Focus.setTabIndex(self, self.focusable, index)

    def treeItemIterator(self):
        accum = []
        self.root.addTreeItems(accum)
        return accum.__iter__()

    def collectElementChain(self, chain, hRoot, hElem):
        if (hElem == None) or DOM.compare(hElem, hRoot):
            return

        self.collectElementChain(chain, hRoot, DOM.getParent(hElem))
        chain.append(hElem)

    def elementClicked(self, root, hElem):
        chain = []
        self.collectElementChain(chain, self.getElement(), hElem)

        item = self.findItemByChain(chain, 0, root)
        if item != None:
            if DOM.compare(item.getImageElement(), hElem):
                item.setState(not item.getState(), True)
                return True
            elif DOM.isOrHasChild(item.getElement(), hElem):
                self.onSelection(item, True)
                return True

        return False

    def findDeepestOpenChild(self, item):
        if not item.getState():
            return item
        return self.findDeepestOpenChild(item.getChild(item.getChildCount() - 1))
    
    def findItemByChain(self, chain, idx, root):
        if idx == len(chain):
            return root

        hCurElem = chain[idx]
        for i in range(root.getChildCount()):
            child = root.getChild(i)
            if DOM.compare(child.getElement(), hCurElem):
                retItem = self.findItemByChain(chain, idx + 1, root.getChild(i))
                if retItem == None:
                    return child
                return retItem
        
        return self.findItemByChain(chain, idx + 1, root)

    def moveFocus(self, selection):
        focusableWidget = selection.getFocusableWidget()
        if focusableWidget != None:
            focusableWidget.setFocus(True)
            DOM.scrollIntoView(focusableWidget.getElement())
        else:
            selectedElem = selection.getContentElem()
            containerLeft = self.getAbsoluteLeft()
            containerTop = self.getAbsoluteTop()
        
            left = DOM.getAbsoluteLeft(selectedElem) - containerLeft
            top = DOM.getAbsoluteTop(selectedElem) - containerTop
            width = DOM.getIntAttribute(selectedElem, "offsetWidth")
            height = DOM.getIntAttribute(selectedElem, "offsetHeight")
        
            DOM.setIntStyleAttribute(self.focusable, "left", left)
            DOM.setIntStyleAttribute(self.focusable, "top", top)
            DOM.setIntStyleAttribute(self.focusable, "width", width)
            DOM.setIntStyleAttribute(self.focusable, "height", height)
        
            DOM.scrollIntoView(self.focusable)
            Focus.focus(self, self.focusable)

    def moveSelectionDown(self, sel, dig):
        if sel == self.root:
            return

        parent = sel.getParentItem()
        if parent == None:
            parent = self.root
        idx = parent.getChildIndex(sel)

        if not dig or not sel.getState():
            if idx < parent.getChildCount() - 1:
                self.onSelection(parent.getChild(idx + 1), True)
            else:
                self.moveSelectionDown(parent, False)
        elif sel.getChildCount() > 0:
            self.onSelection(sel.getChild(0), True)

    def moveSelectionUp(self, sel, climb):
        parent = sel.getParentItem()
        if parent == None:
            parent = self.root
        idx = parent.getChildIndex(sel)

        if idx > 0:
            sibling = parent.getChild(idx - 1)
            self.onSelection(self.findDeepestOpenChild(sibling), True)
        else:
            self.onSelection(parent, True)

    def onSelection(self, item, fireEvents):
        if item == self.root:
            return

        if self.curSelection != None:
            self.curSelection.setSelected(False)

        self.curSelection = item

        if self.curSelection != None:
            self.moveFocus(self.curSelection)
            self.curSelection.setSelected(True)
            if fireEvents and len(self.listeners):
                for listener in self.listeners:
                    listener.onTreeItemSelected(item)

    def doAttachChildren(self):
        for child in self:
            child.onAttach()
        DOM.setEventListener(self.focusable, self);

    def doDetachChildren(self):
        for child in self:
            child.onDetach()
        DOM.setEventListener(self.focusable, None);

    def onLoad(self):
        self.root.updateStateRecursive()

    def adopt(self, content):
        self.childWidgets.add(content)
        content.treeSetParent(self)

    def disown(self, item):
        self.childWidgets.remove(item)
        item.treeSetParent(None)

    def fireStateChanged(self, item):
        for listener in self.listeners:
            listener.onTreeItemStateChanged(item)
    
    def getChildWidgets(self):
        return self.childWidgets

    def shouldTreeDelegateFocusToElement(self, elem):
        JS("""
        var focus = ((elem.nodeName == "SELECT") || (elem.nodeName == "INPUT")  || (elem.nodeName == "CHECKBOX"));
        return focus;
        """)


class FocusPanel(SimplePanel):
    def __init__(self, child=None):
        self.clickListeners = []
        self.focusListeners = []
        self.keyboardListeners = []
        self.mouseListeners = []

        SimplePanel.__init__(self, Focus.createFocusable(self))
        self.sinkEvents(Event.FOCUSEVENTS | Event.KEYEVENTS | Event.ONCLICK | Event.MOUSEEVENTS)

        if child:
            self.setWidget(child)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)
    
    def addFocusListener(self, listener):
        self.focusListeners.append(listener)

    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def getTabIndex(self):
        return Focus.getTabIndex(self, self.getElement())
        
    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        
        if type == "click":
            for listener in self.clickListeners:
                if listener.onClick: listener.onClick(self, event)
                else: listener(self, event)
        elif type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener.fireMouseEvent(self, self.mouseListeners, self, event)
        elif type == "blur" or type == "focus":
            FocusListener.fireFocusEvent(self, self.focusListeners, self, event)
        elif type == "keydown" or type == "keypress" or type == "keyup":
            KeyboardListener.fireKeyboardEvent(self, self.keyboardListeners, self, event)
        
    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def removeFocusListener(self, listener):
        self.focusListeners.remove(listener)

    def removeKeyboardListener(self, listener):
        self.keyboardListeners.remove(listener)

    def removeMouseListener(self, listener):
        self.mouseListeners.remove(listener)

    def setAccessKey(self, key):
        Focus.setAccessKey(self, self.getElement(), key)
    
    def setFocus(self, focused):
        if (focused):
            Focus.focus(self, self.getElement())
        else:
            Focus.blur(self, self.getElement())

    def setTabIndex(self, index):
        Focus.setTabIndex(self, self.getElement(), index)


# FocusImpl
class Focus:

    def blur(self, elem):
        JS("""
        elem.blur();
        """)
    
    def createFocusable(self):
        JS("""
        var e = $doc.createElement("DIV");
        e.tabIndex = 0;
        return e;
        """)

    def focus(self, elem):
        JS("""
        elem.focus();
        """)
    
    def getTabIndex(self, elem):
        JS("""
        return elem.tabIndex;
        """)
    
    def setAccessKey(self, elem, key):
        JS("""
        elem.accessKey = key;
        """)
    
    def setTabIndex(self, elem, index):
        JS("""
        elem.tabIndex = index;
        """)


class FileUpload(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.setElement(DOM.createElement("input"))
        DOM.setAttribute(self.getElement(), "type", "file")
        self.setStyleName("gwt-FileUpload")

    def getFilename(self):
        return DOM.getAttribute(self.getElement(), "value")

    def getName(self):
        return DOM.getAttribute(self.getElement(), "name")

    def setName(self, name):
        DOM.setAttribute(self.getElement(), "name", name)


class Hidden(Widget):
    def __init__(self, name=None, value=None):
        Widget.__init__(self)
        element = DOM.createElement("input")
        self.setElement(element)
        DOM.setAttribute(element, "type", "hidden")

        if name != None:
            self.setName(name)

        if value != None:
            self.setValue(value)
    
    def getDefaultValue(self):
        return DOM.getAttribute(self.getElement(), "defaultValue")
    
    def getName(self):
        return DOM.getAttribute(self.getElement(), "name")

    def getValue(self):
        return DOM.getAttribute(self.getElement(), "value")

    def setDefaultValue(self, defaultValue):
        DOM.setAttribute(self.getElement(), "defaultValue", defaultValue)

    def setName(self, name):
        if name == None:
            #throw new NullPointerException("Name cannot be null");
            console.error("Name cannot be null")
        elif len(name) == 0:
            #throw new IllegalArgumentException("Name cannot be an empty string.");
            console.error("Name cannot be an empty string.")
        DOM.setAttribute(self.getElement(), "name", name)

    def setValue(self, value):
        DOM.setAttribute(self.getElement(), "value", value)


class NamedFrame(Frame):
    def __init__(self, name):
        Frame.__init__(self)
        div = DOM.createDiv()
        DOM.setInnerHTML(div, "<iframe name='" + name + "'>")

        iframe = DOM.getFirstChild(div)
        self.setElement(iframe)

    def getName(self):
        return DOM.getAttribute(self.getElement(), "name")


class EventObject:
    def __init__(self, source):
       self.source = source
    def getSource(self):
       return self.source
   
class FormSubmitEvent(EventObject):
    def __init__(self, source):
       EventObject.__init__(self, source)
       self.cancel = False # ?
       
    def isCancelled(self):
       return self.cancel
   
    def setCancelled(self, cancel):
       self.cancel = cancel

class FormSubmitCompleteEvent(EventObject):
    def __init__(self, source, results):
       EventObject.__init__(self, source)
       self.results = results
    def getResults(self):
       return self.results

FormPanel_formId = 0

class FormPanel(SimplePanel):
    ENCODING_MULTIPART = "multipart/form-data"
    ENCODING_URLENCODED = "application/x-www-form-urlencoded"
    METHOD_GET = "get"
    METHOD_POST = "post"

    def __init__(self, target = None):
        global FormPanel_formId

        if hasattr(target, "getName"):
            target = target.getName()

        SimplePanel.__init__(self, DOM.createForm())

        self.formHandlers = []
        self.iframe = None

        FormPanel_formId += 1
        formName = "FormPanel_" + str(FormPanel_formId)
        DOM.setAttribute(self.getElement(), "target", formName)
        DOM.setInnerHTML(self.getElement(), "<iframe name='" + formName + "'>")
        self.iframe = DOM.getFirstChild(self.getElement())
        
        DOM.setIntStyleAttribute(self.iframe, "width", 0)
        DOM.setIntStyleAttribute(self.iframe, "height", 0)
        DOM.setIntStyleAttribute(self.iframe, "border", 0)
        
        self.sinkEvents(Event.ONLOAD)

        if target != None:
            self.setTarget(target)

    def addFormHandler(self, handler):
        self.formHandlers.append(handler)

    def getAction(self):
        return DOM.getAttribute(self.getElement(), "action")

    # FormPanelImpl.getEncoding
    def getEncoding(self):
        JS("""
        return this.getElement().enctype;
        """)

    def getMethod(self):
        return DOM.getAttribute(self.getElement(), "method")

    def getTarget(self):
        return DOM.getAttribute(self.getElement(), "target")

    # FormPanelImpl.getTextContents
    def getTextContents(self, iframe):
        JS("""
        try {
            if (!iframe.contentWindow.document)
                return null;
        
            return iframe.contentWindow.document.body.innerHTML;
        } catch (e) {
            return null;
        }
        """)

    # FormPanelImpl.hookEvents
    def hookEvents(self, iframe, form, listener):
        JS("""
        if (iframe) {
            iframe.onload = function() {
                if (!iframe.__formAction)
                    return;
        
                listener.onFrameLoad();
            };
        }

        form.onsubmit = function() {
            if (iframe)
                iframe.__formAction = form.action;
            return listener.onFormSubmit();
        };
        """)

    def onFormSubmit(self):
        event = FormSubmitEvent(self)
        for handler in self.formHandlers:
            handler.onSubmit(event)

        return not event.isCancelled()

    def onFrameLoad(self):
        event = FormSubmitCompleteEvent(self, self.getTextContents(self.iframe))
        for handler in self.formHandlers:
            handler.onSubmitComplete(event)

    def removeFormHandler(self, handler):
        self.formHandlers.remove(handler)

    def setAction(self, url):
        DOM.setAttribute(self.getElement(), "action", url)

    # FormPanelImpl.setEncoding
    def setEncoding(self, encodingType):
        JS("""
        var form = this.getElement();
        form.enctype = encodingType;
        form.encoding = encodingType;
        """)

    def setMethod(self, method):
        DOM.setAttribute(self.getElement(), "method", method)

    def submit(self):
        event = FormSubmitEvent(self)
        for handler in self.formHandlers:
            handler.onSubmit(event)

        if event.isCancelled():
            return

        self.submitImpl(self.getElement(), self.iframe)

    # FormPanelImpl.submit
    def submitImpl(self, form, iframe):
        JS("""
        if (iframe)
            iframe.__formAction = form.action;
        form.submit();
        """)

    def onAttach(self):
        SimplePanel.onAttach(self)
        self.hookEvents(self.iframe, self.getElement(), self)

    def onDetach(self):
        SimplePanel.onDetach(self)
        self.unhookEvents(self.iframe, self.getElement())

    def setTarget(self, target):
        DOM.setAttribute(self.getElement(), "target", target)

    # FormPanelImpl.unhookEvents
    def unhookEvents(self, iframe, form):
        JS("""
        if (iframe)
            iframe.onload = null;
        form.onsubmit = null;
        """)






