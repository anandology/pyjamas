def setStyleAttribute(element, name, value):
    element.setStyleAttribute(name, value)


def insertChild(element, insert_element, beforeIndex):
    element.insertChild(insert_element, beforeIndex)


def getParent(element):
    return element.getParent()


def setAttribute(element, key, value):
    element.setAttribute(key, value)


def getAttribute(element, key):
    return element.getAttribute(key)


def setElemAttribute(element, key, value):
    element.setAttribute(key, value)



def setInnerHTML(element, html):
    element.setInnerHTML(html)


def setInnerText(element, text):
    element.setInnerText(text)

def sinkEvents(element, bits):
    mask = getEventsSunk(element) ^ bits
    eventbitsmap[element] = bits
    if not mask:
        return

    bits = mask
    if not bits:
        return
    events = []
    if bits & ONBLUR:
        events += ["onblur"]
    if bits & ONCHANGE:
        events += ["onchange"]
    if bits & ONCLICK:
        events += ["onclick"]
    if bits & ONCONTEXTMENU:
        events += ["oncontextmenu"]
    if bits & ONDBLCLICK:
        events += ["ondblclick"]
    if bits & ONERROR:
        events += ["onerror"]
    if bits & ONFOCUS:
        events += ["onfocus"]
    if bits & ONKEYDOWN:
        events += ["onkeydown"]
    if bits & ONKEYPRESS:
        events += ["onkeypress"]
    if bits & ONKEYUP:
        events += ["onkeyup"]
    if bits & ONLOAD:
        events += ["onload"]
    if bits & ONLOSECAPTURE:
        events += ["onclosecapture"]
    if bits & ONMOUSEDOWN:
        events += ["onmousedown"]
    if bits & ONMOUSEMOVE:
        events += ["onmousemove"]
    if bits & ONMOUSEOUT:
        events += ["onmouseout"]
    if bits & ONMOUSEOVER:
        events += ["onmouseover"]
    if bits & ONMOUSEUP:
        events += ["onmouseup"]
    if bits & ONSCROLL:
        events += ["onscroll"]

    mf = get_main_frame()
    for e in events:
        dispatch = lambda elem, ev: _dispatchEvent(elem, ev, None)
        mf.addEventListener(element, e, dispatch)


