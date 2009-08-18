def getAbsoluteLeft(elem):
    left = elem.getBoundingClientRect().left
    return left + elem.ownerDocument.body.scrollLeft

def getAbsoluteTop(elem):
    top = elem.getBoundingClientRect().top
    return top + elem.ownerDocument.body.scrollTop
