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
"""
    DOM implements the core of Pjamas-Desktop, providing access to
    and management of the DOM model of the PyWebkitGtk window.
"""

import sys
if sys.platform not in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from pyjamas.Window import onResize, onClosing, onClosed
    from pyjamas.__pyjamas__ import JS, doc, get_main_frame, wnd

    currentEvent = None

sCaptureElem = None
sEventPreviewStack = []
global sCaptureElem

def init():

    mf = get_main_frame()
    mf.connect("browser-event", browser_event_cb) # yuk.  one signal? oh well..
    mf.add_window_event_listener("click")
    mf.add_window_event_listener("change")
    mf.add_window_event_listener("mouseout")
    mf.add_window_event_listener("mousedown")
    mf.add_window_event_listener("mouseup")
    mf.add_window_event_listener("resize")
    mf.add_window_event_listener("keyup")
    mf.add_window_event_listener("keydown")
    mf.add_window_event_listener("keypress")

def _dispatchEvent(evt):
    
    listener = None
    curElem =  evt.props.target
    
    print "_dispatchEvent"
    cap = getCaptureElement()
    if cap and cap._listener:
        print "_dispatchEvent", cap, cap._listener
        dispatchEvent(evt, cap, cap._listener)
        evt.stop_propagation()
        return

    while curElem and not (hasattr(curElem, "_listener") and curElem._listener):
        print "no parent listener", curElem, getParent(curElem)
        curElem = getParent(curElem)
    if curElem and getNodeType(curElem) != 1:
        curElem = None

    if curElem and hasattr(curElem, "_listener") and curElem._listener:
        dispatchEvent(evt, curElem, curElem._listener)
    
def _dispatchCapturedMouseEvent(evt):

    if (_dispatchCapturedEvent(evt)):
        cap = getCaptureElement()
        print "dcme", cap, cap and cap._listener
        if cap and cap._listener:
            dispatchEvent(evt, cap, cap._listener)
            print "dcmsev, stop propagation"
            evt.stop_propagation()

def _dispatchCapturedMouseoutEvent(evt):
    cap = getCaptureElement()
    if cap:
        print "cap", dir(evt), cap
        if not eventGetToElement(evt):
            print "synthesise", cap
            #When the mouse leaves the window during capture, release capture
            #and synthesize an 'onlosecapture' event.
            setCapture(None)
            if cap._listener:
                # this should be interesting...
                lcEvent = doc().create_event('UIEvent')
                lcEvent.init_ui_event('losecapture', False, False, wnd(), 0)
                dispatchEvent(lcEvent, cap, cap._listener);

def browser_event_cb(view, event, from_window):

    et = eventGetType(event)
    print "browser_event_cb", event, et
    if et == "resize":
        onResize()
        return
    elif et == 'mouseout':
        print "mouse out", event
        return _dispatchCapturedMouseoutEvent(event)
    elif et == 'keyup' or et == 'keydown' or et == 'keypress' or et == 'change':
        return _dispatchCapturedEvent(event)
    else:
        return _dispatchCapturedMouseEvent(event)

def _dispatchCapturedEvent(event):

    if not previewEvent(event):
        print "dce, stop propagation"
        event.stop_propagation()
        event.prevent_default()
        return False
    return True


def addEventPreview(preview):
    global sEventPreviewStack
    sEventPreviewStack.append(preview)

def appendChild(parent, child):
    print "appendChild", parent, child
    parent.append_child(child)

def compare(elem1, elem2):
    return elem1.is_same_node(elem2)

def createAnchor():
    return createElement("A")

def createButton():
    return createElement("button")

def createCol():
    return createElement("col")

def createDiv():
    return createElement("div")

def createElement(tag):
    return doc().create_element(tag)

def createFieldSet():
    return createElement("fieldset")

def createForm():
    return createElement("form")

def createIFrame():
    return createElement("iframe")

def createImg():
    return createElement("img")

def createInputCheck():
    return createInputElement("checkbox")

def createInputElement(elementType):
    e = createElement("INPUT")
    e.props.type = elementType;
    return e

def createInputPassword():
    return createInputElement("password")

def createInputRadio(group):
    e = createInputElement('radio')
    e.props.name = group
    return e

def createInputText():
    return createInputElement("text")

def createLabel():
    return createElement("label")

def createLegend():
    return createElement("legend")

def createOptions():
    return createElement("options")

def createSelect():
    return createElement("select")

def createSpan():
    return createElement("span")

def createTable():
    return createElement("table")

def createTBody():
    return createElement("tbody")

def createTD():
    return createElement("td")

def createTextArea():
    return createElement("textarea")

def createTH():
    return createElement("th")

def createTR():
    return createElement("tr")

def eventCancelBubble(evt, cancel):
    evt.cancelBubble = cancel

def eventGetAltKey(evt):
    return evt.props.alt_key

def eventGetButton(evt):
    return evt.props.button

def eventGetClientX(evt):
    return evt.props.client_x

def eventGetClientY(evt):
    return evt.props.client_y

def eventGetCtrlKey(evt):
    return evt.props.ctrl_key

def eventGetFromElement(evt):
    return evt.props.from_element

def eventGetKeyCode(evt):
    return evt.props.which and evt.props.key_code

def eventGetRepeat(evt):
    return evt.props.repeat

def eventGetScreenX(evt):
    return evt.props.screen_x

def eventGetScreenY(evt):
    return evt.props.screen_y

def eventGetShiftKey(evt):
    return evt.props.shift_key

def eventGetTarget(event):
    return event.props.target

def eventGetToElement(evt):
    type = eventGetType(evt)
    if type == 'mouseout':
        return evt.props.related_target
    elif type == 'mouseover':
        return evt.props.target
    return None

def eventGetType(event):
    return event.props.type

def eventGetTypeInt(event):
    JS("""
    switch (event.type) {
      case "blur": return 0x01000;
      case "change": return 0x00400;
      case "click": return 0x00001;
      case "dblclick": return 0x00002;
      case "focus": return 0x00800;
      case "keydown": return 0x00080;
      case "keypress": return 0x00100;
      case "keyup": return 0x00200;
      case "load": return 0x08000;
      case "losecapture": return 0x02000;
      case "mousedown": return 0x00004;
      case "mousemove": return 0x00040;
      case "mouseout": return 0x00020;
      case "mouseover": return 0x00010;
      case "mouseup": return 0x00008;
      case "scroll": return 0x04000;
      case "error": return 0x10000;
    }
    """)

def eventGetTypeString(event):
    return eventGetType(event)

def eventPreventDefault(evt):
    evt.prevent_default()

def eventSetKeyCode(evt, key):
    evt.props.key_code = key

def eventToString(evt):
    return evt.to_strign

def iframeGetSrc(elem):
    return elem.props.src

def getAbsoluteLeft(elem):
    left = 0
    while elem:
        left += elem.props.offset_left - elem.props.scroll_left;
        parent = elem.props.offset_parent;
        if parent and parent.props.tag_name == 'BODY' and \
            hasattr(elem, 'style') and \
            getStyleAttribute(elem, 'position') == 'absolute':
            break
        elem = parent
    
    return left + doc().props.body.props.scroll_left;

def getAbsoluteTop(elem):
    top = 0
    while elem:
        top += elem.props.offset_top - elem.props.scroll_top;
        parent = elem.props.offset_parent;
        if parent and parent.props.tag_name == 'BODY' and \
            hasattr(elem, 'style') and \
            getStyleAttribute(elem, 'position') == 'absolute':
            break
        elem = parent
    
    return top + doc().props.body.props.scroll_top;

def getAttribute(elem, attr):
    return str(elem.get_property(mash_name_for_glib(attr)))

def getElemAttribute(elem, attr):
    if not elem.has_attribute(attr):
        return str(elem.get_property(mash_name_for_glib(attr)))
    return str(elem.get_attribute(attr))

def getBooleanAttribute(elem, attr):
    return bool(elem.get_property(mash_name_for_glib(attr)))

def getBooleanElemAttribute(elem, attr):
    if not elem.has_attribute(attr):
        return None
    return bool(elem.get_attribute(attr))

def getCaptureElement():
    global sCaptureElem
    return sCaptureElem

def getChild(elem, index):
    """
    Get a child of the DOM element by specifying an index.
    """
    count = 0
    child = elem.props.first_child
    while child:
        next = child.props.next_sibling;
        if child.props.node_type == 1:
            if index == count:
              return child;
            count += 1
        child = next
    return None

def getChildCount(elem):
    """
    Calculate the number of children the given element has.  This loops
    over all the children of that element and counts them.
    """
    count = 0
    child = elem.props.first_child;
    while child:
      if child.props.node_type == 1:
          count += 1
      child = child.props.next_sibling;
    return count;

def getChildIndex(parent, toFind):
    """
    Return the index of the given child in the given parent.
    
    This performs a linear search.
    """
    count = 0
    child = parent.props.first_child;
    while child:
        if child == toFind:
            return count
        if child.props.node_type == 1:
            count += 1
        child = child.props.next_sibling

    return -1;

def getElementById(id):
    """
    Return the element in the document's DOM tree with the given id.
    """
    return doc().get_element_by_id(id)

def getEventListener(element):
    """
    See setEventListener() for more information.
    """
    return element._listener

def getEventsSunk(element):
    """
    Return which events are currently "sunk" for a given DOM node.  See
    sinkEvents() for more information.
    """
    if hasattr(element, "__eventBits"):
        return element.__eventBits
    return 0

def getFirstChild(elem):
    child = elem and elem.props.first_child
    while child and child.props.node_type != 1:
        child = child.props.next_sibling
    return child

def getInnerHTML(element):
    return element and element.props.inner_html

def getInnerText(element):
    # To mimic IE's 'innerText' property in the W3C DOM, we need to recursively
    # concatenate all child text nodes (depth first).
    text = ''
    child = element.props.first_child;
    while child:
      if child.props.node_type == 1:
        text += child.get_inner_text()
      elif child.props.node_value:
        text += child.props.node_value
      child = child.props.next_sibling
    return text

def getIntAttribute(elem, attr):
    return int(elem.get_property(mash_name_for_glib(attr)))

def getIntElemAttribute(elem, attr):
    if not elem.has_attribute(attr):
        return None
    return int(elem.get_attribute(attr))

def getIntStyleAttribute(elem, attr):
    return int(elem.style.get_property(mash_name_for_glib(attr)))

def getNextSibling(elem):
    sib = elem.props.next_sibling
    while sib and sib.props.node_type != 1:
        sib = sib.props.next_sibling
    return sib

def getNodeType(elem):
    return elem.props.node_type 

def getParent(elem):
    parent = elem.props.parent_node 
    if parent is None:
        return None
    if getNodeType(parent) != 1:
        return None
    return parent 

def getStyleAttribute(elem, attr):
    return elem.style.get_property(mash_name_for_glib(attr))

def insertChild(parent, toAdd, index):
    count = 0
    child = parent.props.first_child
    before = None;
    while child:
        if child.props.node_type == 1:
            if (count == index):
                before = child;
                break
            
            count += 1
        child = child.props.next_sibling

    if before is None:
        parent.append_child(toAdd)
    else:
        parent.insert_before(toAdd, before)

class IterChildrenClass:
    def __init__(self, elem):
        self.parent = elem
        self.child = elem.props.first_child
        self.lastChild = None
    def next (self):
        if not self.child:
            raise StopIteration
        self.lastChild = self.child;
        self.child = getNextSibling(self.child)
        return self.lastChild
    def remove(self):
        self.parent.removeChild(self.lastChild);
    def __iter__(self):
        return self

def iterChildren(elem):
    """
    Returns an iterator over all the children of the given
    DOM node.
    """
    return IterChildrenClass(elem)

class IterWalkChildren:

    def __init__(self, elem):
        self.parent = elem
        self.child = getFirstChild(elem)
        self.lastChild = None
        self.stack = []

    def next(self):
        if not self.child:
            raise StopIteration
        self.lastChild = self.child
        first_child = getFirstChild(self.child)
        next_sibling = getNextSibling(self.child)
        if first_child is not None:
            if next_sibling is not None:
               self.stack.append((next_sibling, self.parent))
            self.parent = self.child
            self.child = first_child
        elif next_sibling is not None:
            self.child = next_sibling
        elif len(self.stack) > 0:
            (self.child, self.parent) = self.stack.pop()
        else:
            self.child = None
        return self.lastChild

    def remove(self):
        self.parent.removeChild(self.lastChild)

    def __iter__(self):
        return self

def walkChildren(elem):
    """
    Walk an entire subtree of the DOM.  This returns an
    iterator/iterable which performs a pre-order traversal
    of all the children of the given element.
    """
    return IterWalkChildren(elem)

def isOrHasChild(parent, child):
    while child:
        if parent == child:
            return True
        child = child.props.parent_node;
        if not child:
            return False
        if child.props.node_type != 1:
            child = None
    return False

def releaseCapture(elem):
    global sCaptureElem
    if sCaptureElem and compare(elem, sCaptureElem):
        sCaptureElem = None
    return

def removeChild(parent, child):
    parent.remove_child(child)

def replaceChild(parent, newChild, oldChild):
    parent.replace_child(newChild, oldChild)

def removeEventPreview(preview):
    global sEventPreviewStack
    sEventPreviewStack.remove(preview)

def scrollIntoView(elem):
    left = elem.props.offset_left
    top = elem.props.offset_top
    width = elem.props.offset_width
    height = elem.props.offset_height
    
    if elem.props.parent_node != elem.props.offset_parent:
        left -= elem.props.parent_node.props.offset_left
        top -= elem.props.parent_node.props.offset_top

    cur = elem.props.parent_node
    while cur and cur.props.node_type == 1:
        if hasattr(cur, 'style') and \
           (cur.style.overflow == 'auto' or cur.style.overflow == 'scroll'):
            if left < cur.props.scroll_left:
                cur.props.scroll_left = left
            if left + width > cur.props.scroll_left + cur.props.client_width:
                cur.props.scroll_left = (left + width) - cur.props.client_width
            if top < cur.props.scroll_top:
                cur.props.scroll_top = top
            if top + height > cur.props.scroll_top + cur.props.client_height:
                cur.props.scroll_top = (top + height) - cur.props.client_height

        offset_left = cur.props.offset_left
        offset_top = cur.props.offset_top
        if cur.props.parent_node != cur.props.offset_parent :
            if hasattr(cur.props.parent_node.props, "offset_left"):
                offset_left -= cur.props.parent_node.props.offset_left
            if hasattr(cur.props.parent_node.props, "offset_top"):
                offset_top -= cur.props.parent_node.props.offset_top

        left += offset_left - cur.props.scroll_left
        top += offset_top - cur.props.scroll_top
        cur = cur.props.parent_node

def mash_name_for_glib(name, joiner='-'):
    res = ''
    for c in name:
        if c.isupper():
            res += joiner + c.lower()
        else:
            res += c
    return res

def removeAttribute(element, attribute):
    elem.remove_attribute(attribute)

def setAttribute(element, attribute, value):
    element.set_property(mash_name_for_glib(attribute), value)

def setElemAttribute(element, attribute, value):
    element.set_attribute(attribute, value)

def setBooleanAttribute(elem, attr, value):
    elem.set_property(mash_name_for_glib(attr), value)

def setCapture(elem):
    global sCaptureElem
    sCaptureElem = elem
    print "setCapture", sCaptureElem

def setEventListener(element, listener):
    """
    Register an object to receive event notifications for the given
    element.  The listener's onBrowserEvent() method will be called
    when a captured event occurs.  To set which events are captured,
    use sinkEvents().
    """
    element._listener = listener

def setInnerHTML(element, html):
    element.props.inner_html = html

def setInnerText(elem, text):
    #Remove all children first.
    while elem.props.first_child:
        elem.remove_child(elem.props.first_child)
    elem.append_child(doc().create_text_node(text or ''))

def setIntElemAttribute(elem, attr, value):
    elem.set_attribute(attr, str(value))

def setIntAttribute(elem, attr, value):
    elem.set_property(mash_name_for_glib(attr), value)

def setIntStyleAttribute(elem, attr, value):
    sty = elem.props.style
    sty.set_css_property(mash_name_for_glib(attr), str(value), "")

def setOptionText(select, text, index):
    print "TODO - setOptionText"
    JS("""
    var option = select.options[index];
    option.text = text;
    """)

def setStyleAttribute(element, name, value):
    sty = element.props.style
    sty.set_css_property(mash_name_for_glib(name), value, "")

def dispatch_event_cb(element, event, capture):
    print "dispatch_event_cb", element, event, capture

def sinkEvents(element, bits):
    """
    Set which events should be captured on a given element and passed to the
    registered listener.  To set the listener, use setEventListener().
    
    @param bits: A combination of bits; see ui.Event for bit values
    """
    mask = getEventsSunk(element) ^ bits
    element.__eventBits = bits
    if not mask:
        return

    bits = mask

    if bits:
        element.connect("browser-event", lambda x,y,z: _dispatchEvent(y))
    if (bits & 0x00001):
        element.add_event_listener("click", True)
    if (bits & 0x00002):
        element.add_event_listener("dblclick", True)
    if (bits & 0x00004):
        element.add_event_listener("mousedown", True)
    if (bits & 0x00008):
        element.add_event_listener("mouseup", True)
    if (bits & 0x00010):
        element.add_event_listener("mouseover", True)
    if (bits & 0x00020):
        element.add_event_listener("mouseout", True)
    if (bits & 0x00040):
        element.add_event_listener("mousemove", True)
    if (bits & 0x00080):
        element.add_event_listener("keydown", True)
    if (bits & 0x00100):
        element.add_event_listener("keypress", True)
    if (bits & 0x00200):
        element.add_event_listener("keyup", True)
    if (bits & 0x00400):
        element.add_event_listener("change", True)
    if (bits & 0x00800):
        element.add_event_listener("focus", True)
    if (bits & 0x01000):
        element.add_event_listener("blur", True)
    if (bits & 0x02000):
        element.add_event_listener("losecapture", True)
    if (bits & 0x04000):
        element.add_event_listener("scroll", True)
    if (bits & 0x08000):
        element.add_event_listener("load", True)
    if (bits & 0x10000):
        element.add_event_listener("error", True)

def toString(elem):
    temp = elem.clone_node(True)
    tempDiv = createDiv()
    tempDiv.append_child(temp)
    outer = tempDiv.props.inner_html
    temp.props.inner_html = ""
    return outer

# TODO: missing dispatchEventAndCatch
def dispatchEvent(event, element, listener):
    dispatchEventImpl(event, element, listener)

def previewEvent(evt):
    global sEventPreviewStack
    ret = True
    if len(sEventPreviewStack) > 0:
        preview = sEventPreviewStack[len(sEventPreviewStack) - 1]
        
        ret = preview.onEventPreview(evt)
        if not ret:
            print "previewEvent, cancel, prevent default"
            eventCancelBubble(evt, True)
            eventPreventDefault(evt)

    return ret

# TODO
def dispatchEventAndCatch(evt, elem, listener, handler):
    pass

currentEvent = None

def dispatchEventImpl(event, element, listener):
    global sCaptureElem
    global currentEvent
    if element == sCaptureElem:
        if eventGetType(event) == "losecapture":
            sCaptureElem = None
    print "dispatchEventImpl", listener, eventGetType(event)
    prevCurrentEvent = currentEvent
    currentEvent = event
    listener.onBrowserEvent(event)
    currentEvent = prevCurrentEvent

def eventGetCurrentEvent():
    global currentEvent
    return currentEvent

def insertListItem(select, item, value, index):
    option = createElement("OPTION")
    setInnerText(option, item)
    if value != None:
        setAttribute(option, "value", value)
    if index == -1:
        appendChild(select, option)
    else:
        insertChild(select, option, index)



if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    init()

