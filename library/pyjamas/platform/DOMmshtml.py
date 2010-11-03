
def get_listener(item):
    if item is None:
        return None
    return listeners.get(item.uniqueID)

def set_listener(item, listener):
    listeners[item.uniqueID] = listener


def _dispatchEvent(sender, event, useCap):
    if event is None:
        evt = wnd().event
    else:
        evt = event
    #print "_dispatchEvent", sender, evt, evt.type, evt.returnValue

    if evt.returnValue is None:
        evt.returnValue = True
        if not previewEvent(evt):
            return

    cap = getCaptureElement()
    listener = get_listener(cap)
    if cap and (listener is not None):
        #print "_dispatchEvent capture", cap, listener
        dispatchEvent(evt, cap, listener)
        return

    curElem = sender
    while curElem and (get_listener(curElem) is None):
        curElem = curElem.parentElement
    
    listener = get_listener(curElem)
    if listener is not None:
        dispatchEvent(evt, curElem, listener)


def buttonClick(elem):
    newEvent = doc().createEventObject()
    elem.fireEvent('onclick', newEvent)


def init():
    
    mf = get_main_frame()
    mf._addWindowEventListener("click", browser_event_cb)
    mf._addWindowEventListener("change", browser_event_cb)
    mf._addWindowEventListener("mouseout", browser_event_cb)
    mf._addWindowEventListener("mousedown", browser_event_cb)
    mf._addWindowEventListener("mouseup", browser_event_cb)
    mf._addWindowEventListener("resize", browser_event_cb)
    mf._addWindowEventListener("keyup", browser_event_cb)
    mf._addWindowEventListener("keydown", browser_event_cb)
    mf._addWindowEventListener("keypress", browser_event_cb)

    # this is somewhat cheating, but hey.  if someone
    # ever tries to wrap body with a Widget, and attaches
    # events to it, whoops...
    body = doc().body

    mf.addEventListener(body, "click", _dispatchEvent)
    mf.addEventListener(body, "mousedown", _dispatchEvent)
    mf.addEventListener(body, "mouseup", _dispatchEvent)
    mf.addEventListener(body, "mousemove", _dispatchEvent)
    mf.addEventListener(body, "keydown", _dispatchEvent)
    mf.addEventListener(body, "keyup", _dispatchEvent)
    mf.addEventListener(body, "keypress", _dispatchEvent)
    mf.addEventListener(body, "focus", _dispatchEvent)
    mf.addEventListener(body, "blur", _dispatchEvent)
    mf.addEventListener(body, "dblclick", _dispatchEvent)
    mf.addEventListener(body, "propertychange", _dispatchEvent)

    _init_mousewheel()

def _init_mousewheel():
    mf._addWindowEventListener("mousewheel", browser_event_cb)

    # XXX whoops, see above...
    body = doc().body
    mf.addEventListener(body, "mousewheel", _dispatchEvent)
    
def compare(elem1, elem2):
    e1 = elem1 is not None
    e2 = elem2 is not None
    if not e1 and not r2:
        return True
    elif not e1 or not e2:
        return False
    return elem1.uniqueID == elem2.uniqueID

def createInputRadio(group):
    return doc().createElement("<INPUT type='RADIO' name='" + group + "'>")

def eventGetType(event):
    etype = event.type
    if etype == 'propertychange':
        return 'input'
    return etype

def eventGetTarget(evt):
    return evt.srcElement

def eventGetToElement(evt):
    return getattr(evt, "toElement", None)

def eventPreventDefault(evt):
    evt.returnValue = False

def eventToString(evt):
    if hasattr(evt, "toString"):
        return evt.toString()
    return "[object Event]"

def getAbsoluteLeft(elem):
    scrollLeft = doc().documentElement.scrollLeft
    if scrollLeft == 0:
        scrollLeft = doc().body.scrollLeft
    
    return (elem.getBoundingClientRect().left + scrollLeft) - 2

def getAbsoluteTop(elem):
    scrollTop = doc().documentElement.scrollTop
    if scrollTop == 0:
        scrollTop = doc().body.scrollTop
    
    return (elem.getBoundingClientRect().top +  scrollTop) - 2


def getChild(elem, index):
    return elem.children.item(index)

def getChildCount(elem):
    return elem.children.length

def getChildIndex(parent, child):
    for i in range(parent.children.length):
        if child.uniqueID == parent.children.item(i).uniqueID:
            return i
    return -1

def getFirstChild(elem):
    return elem.firstChild

def getInnerText(elem):
    return elem.innerText

def getNextSibling(elem):
    return elem.nextSibling

def getParent(elem):
    return elem.parentElement

def insertChild(parent, child, index):
    if index == parent.children.length:
        parent.appendChild(child)
    else:
        parent.insertBefore(child, parent.children.item(index))

def insertListItem(select, text, value, index):
    newOption = doc().createElement("Option")
    if index == -1:
        select.add(newOption)
    else:
        select.add(newOption,index)
    newOption.text = text
    newOption.value = value

def isOrHasChild(parent, child):
    if parent is None:
        return False
    while child is not None:
        if parent.uniqueID == child.uniqueID:
            return True
        child = child.parentElement
    return False

def releaseCapture(elem):
    global sCaptureElem
    if sCaptureElem and compare(elem, sCaptureElem):
        sCaptureElem = None
    elem.releaseCapture()

def setCapture(elem):
    global sCaptureElem
    sCaptureElem = elem
    elem.setCapture()

def setInnerText(elem, text):
    if not text:
        text = ''
    elem.innerText = text

def toString(elem):
    return elem.outerHTML

def setOptionText(select, text, index):
    option = select.options.item(index)
    option.text = text

def eventGetKeyCode(evt):
    if hasattr(evt, "which"):
        return evt.which
    if hasattr(evt, "keyCode"):
        return evt.keyCode
    return 0

def eventStopPropagation(evt):
    eventCancelBubble(evt,True)

def eventGetMouseWheelVelocityY(evt):
    return round(-evt.wheelDelta / 40.0) or 0.0

