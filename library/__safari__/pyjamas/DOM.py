
def toString(elem):
    # need to override because safari does not like '' as inner
    # html. just leave it out so far, don't know what this should do
    # anyways
    JS("""
    var temp = elem.cloneNode(true);
    var tempDiv = $doc.createElement("DIV");
    tempDiv.appendChild(temp);
    outer = tempDiv.innerHTML;
    //temp.innerHTML = " ";
    return outer;
    """)

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
