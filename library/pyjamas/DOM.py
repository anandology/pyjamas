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

listeners = {}

def get_listener(item):
    if item is None:
        return None
    global listeners
    ret = listeners.get(item.__instance__)
    #print "get listener", item, ret
    return ret

def set_listener(item, listener):
    #print "set listener", item, listener
    global listeners
    listeners[item.__instance__] = listener

def init():

    mf = get_main_frame()
    mf.connect("browser-event", browser_event_cb) # yuk.  one signal? oh well..
    mf.addWindowEventListener("click")
    mf.addWindowEventListener("change")
    mf.addWindowEventListener("mouseout")
    mf.addWindowEventListener("mousedown")
    mf.addWindowEventListener("mouseup")
    mf.addWindowEventListener("resize")
    mf.addWindowEventListener("keyup")
    mf.addWindowEventListener("keydown")
    mf.addWindowEventListener("keypress")

def _dispatchEvent(evt):
    
    evt = get_main_frame().gobject_wrap(evt) # HACK!
    listener = None
    curElem =  evt.target
    
    #print "_dispatchEvent"
    cap = getCaptureElement()
    listener = get_listener(cap)
    if cap and listener:
        #print "_dispatchEvent", cap, listener
        dispatchEvent(evt, cap, listener)
        evt.stopPropagation()
        return

    while curElem and not get_listener(curElem):
        #print "no parent listener", curElem, getParent(curElem)
        curElem = getParent(curElem)
    if curElem and getNodeType(curElem) != 1:
        curElem = None

    listener = get_listener(curElem)
    if listener:
        dispatchEvent(evt, curElem, listener)
    
def _dispatchCapturedMouseEvent(evt):

    if (_dispatchCapturedEvent(evt)):
        cap = getCaptureElement()
        listener = get_listener(cap)
        if cap and listener:
            dispatchEvent(evt, cap, listener)
            print "dcmsev, stop propagation"
            evt.stopPropagation()

def _dispatchCapturedMouseoutEvent(evt):
    cap = getCaptureElement()
    if cap:
        print "cap", dir(evt), cap
        if not eventGetToElement(evt):
            print "synthesise", cap
            #When the mouse leaves the window during capture, release capture
            #and synthesize an 'onlosecapture' event.
            setCapture(None)
            listener = get_listener(cap)
            if listener:
                # this should be interesting...
                lcEvent = doc().createEvent('UIEvent')
                lcEvent.initUiEvent('losecapture', False, False, wnd(), 0)
                dispatchEvent(lcEvent, cap, listener);

def browser_event_cb(view, event, from_window):

    event = get_main_frame().gobject_wrap(event) # HACK!
    et = eventGetType(event)
    #print "browser_event_cb", event, et
    if et == "resize":
        onResize()
        return
    elif et == 'mouseout':
        #print "mouse out", event
        return _dispatchCapturedMouseoutEvent(event)
    elif et == 'keyup' or et == 'keydown' or et == 'keypress' or et == 'change':
        return _dispatchCapturedEvent(event)
    else:
        return _dispatchCapturedMouseEvent(event)

def _dispatchCapturedEvent(event):

    if not previewEvent(event):
        print "dce, stop propagation"
        event.stopPropagation()
        event.preventDefault()
        return False
    return True


def addEventPreview(preview):
    global sEventPreviewStack
    sEventPreviewStack.append(preview)

def appendChild(parent, child):
    #print "appendChild", parent, child
    parent.appendChild(child)

def compare(elem1, elem2):
    return elem1.isSameNode(elem2)

def createAnchor():
    return createElement("A")

def createButton():
    return createElement("button")

def createCol():
    return createElement("col")

def createDiv():
    return createElement("div")

def createElement(tag):
    return doc().createElement(tag)

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
    e.type = elementType;
    return e

def createInputPassword():
    return createInputElement("password")

def createInputRadio(group):
    e = createInputElement('radio')
    e.name = group
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
    return evt.altKey

def eventGetButton(evt):
    return evt.button

def eventGetClientX(evt):
    return evt.clientX

def eventGetClientY(evt):
    return evt.clientY

def eventGetCtrlKey(evt):
    return evt.ctrlKey

def eventGetFromElement(evt):
    return evt.fromElement

def eventGetKeyCode(evt):
    return evt.which and evt.keyCode

def eventGetRepeat(evt):
    return evt.repeat

def eventGetScreenX(evt):
    return evt.screenX

def eventGetScreenY(evt):
    return evt.screenY

def eventGetShiftKey(evt):
    return evt.shiftKey

def eventGetTarget(event):
    return event.target

def eventGetToElement(evt):
    type = eventGetType(evt)
    if type == 'mouseout':
        return evt.relatedTarget
    elif type == 'mouseover':
        return evt.target
    return None

def eventGetType(event):
    return event.type

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
    evt.preventDefault()

def eventSetKeyCode(evt, key):
    evt.keyCode = key

def eventToString(evt):
    return evt.toString

def iframeGetSrc(elem):
    return elem.src

def getAbsoluteLeft(elem):
    left = 0
    while elem:
        left += elem.offsetLeft - elem.scrollLeft;
        parent = elem.offsetParent;
        if parent and parent.tagName == 'BODY' and \
            hasattr(elem, 'style') and \
            getStyleAttribute(elem, 'position') == 'absolute':
            break
        elem = parent
    
    return left + doc().body.scrollLeft;

def getAbsoluteTop(elem):
    top = 0
    while elem:
        top += elem.offsetTop - elem.scrollTop;
        parent = elem.offsetParent;
        if parent and parent.tagName == 'BODY' and \
            hasattr(elem, 'style') and \
            getStyleAttribute(elem, 'position') == 'absolute':
            break
        elem = parent
    
    return top + doc().body.scrollTop;

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
    child = elem.firstChild
    while child:
        next = child.nextSibling;
        if child.nodeType == 1:
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
    child = elem.firstChild;
    while child:
      if child.nodeType == 1:
          count += 1
      child = child.nextSibling;
    return count;

def getChildIndex(parent, toFind):
    """
    Return the index of the given child in the given parent.
    
    This performs a linear search.
    """
    count = 0
    child = parent.firstChild;
    while child:
        if child == toFind:
            return count
        if child.nodeType == 1:
            count += 1
        child = child.nextSibling

    return -1;

def getElementById(id):
    """
    Return the element in the document's DOM tree with the given id.
    """
    return doc().getElementById(id)

def getEventListener(element):
    """
    See setEventListener() for more information.
    """
    return get_listener(element)

def getEventsSunk(element):
    """
    Return which events are currently "sunk" for a given DOM node.  See
    sinkEvents() for more information.
    """
    if hasattr(element, "__eventBits"):
        return element.__eventBits
    return 0

def getFirstChild(elem):
    child = elem and elem.firstChild
    while child and child.nodeType != 1:
        child = child.nextSibling
    return child

def getInnerHTML(element):
    return element and element.innerHtml

def getInnerText(element):
    # To mimic IE's 'innerText' property in the W3C DOM, we need to recursively
    # concatenate all child text nodes (depth first).
    text = ''
    child = element.firstChild;
    while child:
      if child.nodeType == 1:
        text += child.getInnerText()
      elif child.nodeValue:
        text += child.nodeValue
      child = child.nextSibling
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
    sib = elem.nextSibling
    while sib and sib.nodeType != 1:
        sib = sib.nextSibling
    return sib

def getNodeType(elem):
    return elem.nodeType 

def getParent(elem):
    parent = elem.parentNode 
    if parent is None:
        return None
    if getNodeType(parent) != 1:
        return None
    return parent 

def getStyleAttribute(elem, attr):
    try:
        return elem.style.get_property(mash_name_for_glib(attr))
    except:
        return None

def insertChild(parent, toAdd, index):
    count = 0
    child = parent.firstChild
    before = None;
    while child:
        if child.nodeType == 1:
            if (count == index):
                before = child;
                break
            
            count += 1
        child = child.nextSibling

    if before is None:
        parent.appendChild(toAdd)
    else:
        parent.insertBefore(toAdd, before)

class IterChildrenClass:
    def __init__(self, elem):
        self.parent = elem
        self.child = elem.firstChild
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
        firstChild = getFirstChild(self.child)
        nextSibling = getNextSibling(self.child)
        if firstChild is not None:
            if nextSibling is not None:
               self.stack.append((nextSibling, self.parent))
            self.parent = self.child
            self.child = firstChild
        elif nextSibling is not None:
            self.child = nextSibling
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
        child = child.parentNode;
        if not child:
            return False
        if child.nodeType != 1:
            child = None
    return False

def releaseCapture(elem):
    global sCaptureElem
    if sCaptureElem and compare(elem, sCaptureElem):
        sCaptureElem = None
    return

def removeChild(parent, child):
    parent.removeChild(child)

def replaceChild(parent, newChild, oldChild):
    parent.replaceChild(newChild, oldChild)

def removeEventPreview(preview):
    global sEventPreviewStack
    sEventPreviewStack.remove(preview)

def scrollIntoView(elem):
    left = elem.offsetLeft
    top = elem.offsetTop
    width = elem.offsetWidth
    height = elem.offsetHeight
    
    if elem.parentNode != elem.offsetParent:
        left -= elem.parentNode.offsetLeft
        top -= elem.parentNode.offsetTop

    cur = elem.parentNode
    while cur and cur.nodeType == 1:
        if hasattr(cur, 'style') and hasattr(cur.style, 'overflow') and \
           (cur.style.overflow == 'auto' or cur.style.overflow == 'scroll'):
            if left < cur.scrollLeft:
                cur.scrollLeft = left
            if left + width > cur.scrollLeft + cur.clientWidth:
                cur.scrollLeft = (left + width) - cur.clientWidth
            if top < cur.scrollTop:
                cur.scrollTop = top
            if top + height > cur.scrollTop + cur.clientHeight:
                cur.scrollTop = (top + height) - cur.clientHeight

        offsetLeft = cur.offsetLeft
        offsetTop = cur.offsetTop
        if cur.parentNode != cur.offsetParent :
            if hasattr(cur.parentNode, "offsetLeft"):
                offsetLeft -= cur.parentNode.offsetLeft
            if hasattr(cur.parentNode, "offsetTop"):
                offsetTop -= cur.parentNode.offsetTop

        left += offsetLeft - cur.scrollLeft
        top += offsetTop - cur.scrollTop
        cur = cur.parentNode

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
    element.setAttribute(attribute, value)

def setBooleanAttribute(elem, attr, value):
    elem.set_property(mash_name_for_glib(attr), value)

def setCapture(elem):
    global sCaptureElem
    sCaptureElem = elem
    #print "setCapture", sCaptureElem

def setEventListener(element, listener):
    """
    Register an object to receive event notifications for the given
    element.  The listener's onBrowserEvent() method will be called
    when a captured event occurs.  To set which events are captured,
    use sinkEvents().
    """
    set_listener(element, listener)

def setInnerHTML(element, html):
    element.innerHtml = html

def setInnerText(elem, text):
    #Remove all children first.
    while elem.firstChild:
        elem.removeChild(elem.firstChild)
    elem.appendChild(doc().createTextNode(text or ''))

def setIntElemAttribute(elem, attr, value):
    elem.set_attribute(attr, str(value))

def setIntAttribute(elem, attr, value):
    elem.set_property(mash_name_for_glib(attr), value)

def setIntStyleAttribute(elem, attr, value):
    sty = elem.style
    sty.setCssProperty(mash_name_for_glib(attr), str(value), "")

def setOptionText(select, text, index):
    print "TODO - setOptionText"
    JS("""
    var option = select.options[index];
    option.text = text;
    """)

def setStyleAttribute(element, name, value):
    sty = element.style
    sty.setCssProperty(mash_name_for_glib(name), value, "")

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
        element.addEventListener("click", True)
    if (bits & 0x00002):
        element.addEventListener("dblclick", True)
    if (bits & 0x00004):
        element.addEventListener("mousedown", True)
    if (bits & 0x00008):
        element.addEventListener("mouseup", True)
    if (bits & 0x00010):
        element.addEventListener("mouseover", True)
    if (bits & 0x00020):
        element.addEventListener("mouseout", True)
    if (bits & 0x00040):
        element.addEventListener("mousemove", True)
    if (bits & 0x00080):
        element.addEventListener("keydown", True)
    if (bits & 0x00100):
        element.addEventListener("keypress", True)
    if (bits & 0x00200):
        element.addEventListener("keyup", True)
    if (bits & 0x00400):
        element.addEventListener("change", True)
    if (bits & 0x00800):
        element.addEventListener("focus", True)
    if (bits & 0x01000):
        element.addEventListener("blur", True)
    if (bits & 0x02000):
        element.addEventListener("losecapture", True)
    if (bits & 0x04000):
        element.addEventListener("scroll", True)
    if (bits & 0x08000):
        element.addEventListener("load", True)
    if (bits & 0x10000):
        element.addEventListener("error", True)

def toString(elem):
    temp = elem.clone_node(True)
    tempDiv = createDiv()
    tempDiv.appendChild(temp)
    outer = tempDiv.innerHtml
    temp.innerHtml = ""
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
    #print "dispatchEventImpl", listener, eventGetType(event)
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

