def getAbsoluteLeft(elem):
    JS("""
    var left = 0;
    while (elem) {
        left += elem.offsetLeft - elem.scrollLeft;
    
        var parent = elem.offsetParent;
        if (parent && (parent.tagName == 'BODY') && (elem.style.position == 'absolute'))
            break;
        elem = parent;
    }
    return left + $doc.body.scrollLeft;
    """)

def getAbsoluteTop(elem):
    JS("""
    var top = 0;
    while (elem) {
        top += elem.offsetTop - elem.scrollTop;
    
        var parent = elem.offsetParent;
        if (parent && (parent.tagName == 'BODY') && (elem.style.position == 'absolute'))
            break;
        elem = parent;
    }
    return top + $doc.body.scrollTop;
    """)
