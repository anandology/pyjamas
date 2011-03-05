
def getComputedStyle(element, style=None):
    """
    Get computed style of an element, like in
    http://efreedom.com/Question/1-1848445/Duplicating-Element-Style-JavaScript
    """
    element_style = element.currentStyle
    if style:
        return element_style[style]
    return element_style

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
        scrollOffsetY = doc().body.scrollTop
        scrollOffsetX = doc().body.scrollLeft
        return scrollOffsetX, scrollOffsetY
    except:
        scrollOffsetY = doc().documentElement.scrollTop
        scrollOffsetX = doc().documentElement.scrollLeft
        return scrollOffsetX, scrollOffsetY

def eventCoordinates(event):
    """ Get the absolute coordinates of a mouse event.
    http://www.quirksmode.org/js/events_properties.html#position
    """
    offsetX, offsetY = getScrollOffsets()
    pageX = event.clientX + offsetX
    pageY = event.clientY + offsetY
    return pageX, pageY
