def compare(elem1, elem2):
    JS("""
    if (!elem1 && !elem2) {
        return true;
    } else if (!elem1 || !elem2) {
        return false;
    }
	if (!elem1.isSameNode) {
		return (elem1 == elem2);
	}
    return (elem1.isSameNode(elem2));
    """)

def eventGetButton(evt):
    JS("""
    var button = evt.button;
    if(button == 0) {
        return 1;
    } else if (button == 1) {
        return 4;
    } else {
        return button;
    }
    """)

# This is what is in GWT 1.5 for getAbsoluteLeft.  err...
"""
    // We cannot use DOMImpl here because offsetLeft/Top return erroneous
    // values when overflow is not visible.  We have to difference screenX
    // here due to a change in getBoxObjectFor which causes inconsistencies
    // on whether the calculations are inside or outside of the element's
    // border.
    try {
      return $doc.getBoxObjectFor(elem).screenX
          - $doc.getBoxObjectFor($doc.documentElement).screenX;
    } catch (e) {
      // This works around a bug in the FF3 betas. The bug
      // should be fixed before they release, so this can
      // be removed at a later date.
      // https://bugzilla.mozilla.org/show_bug.cgi?id=409111
      // DOMException.WRONG_DOCUMENT_ERR == 4
      if (e.code == 4) {
        return 0;
      }
      throw e;
    }
"""
def getAbsoluteLeft(elem):
    JS("""
    var left = $doc.getBoxObjectFor(elem).x;
    var parent = elem.parentNode;

    while (parent) {
        if (parent.scrollLeft > 0) {
            left = left -  parent.scrollLeft;
        }
        parent = parent.parentNode;
    }

    return left + $doc.body.scrollLeft + $doc.documentElement.scrollLeft;
    """)

# This is what is in GWT 1.5 for getAbsoluteTop.  err...
"""
    // We cannot use DOMImpl here because offsetLeft/Top return erroneous
    // values when overflow is not visible.  We have to difference screenY
    // here due to a change in getBoxObjectFor which causes inconsistencies
    // on whether the calculations are inside or outside of the element's
    // border.
    try {
      return $doc.getBoxObjectFor(elem).screenY
          - $doc.getBoxObjectFor($doc.documentElement).screenY;
    } catch (e) {
      // This works around a bug in the FF3 betas. The bug
      // should be fixed before they release, so this can
      // be removed at a later date.
      // https://bugzilla.mozilla.org/show_bug.cgi?id=409111
      // DOMException.WRONG_DOCUMENT_ERR == 4
      if (e.code == 4) {
        return 0;
      }
      throw e;
    }
"""
def getAbsoluteTop(elem):
    JS("""
    var top = $doc.getBoxObjectFor(elem).y;
    var parent = elem.parentNode;
    while (parent) {
        if (parent.scrollTop > 0) {
            top -= parent.scrollTop;
        }
        parent = parent.parentNode;
    }

    return top + $doc.body.scrollTop + $doc.documentElement.scrollTop;
    """)

def getChildIndex(parent, child):
    JS("""
    var count = 0, current = parent.firstChild;
    while (current) {
		if (! current.isSameNode) {
			if (current == child) {
			return count;
			}
		}
		else if (current.isSameNode(child)) {
            return count;
        }
        if (current.nodeType == 1) {
            ++count;
        }
        current = current.nextSibling;
    }
    return -1;
    """)

def isOrHasChild(parent, child):
    JS("""
    while (child) {
        if ((!parent.isSameNode)) {
			if (parent == child) {
				return true;
			}
		}
		else if (parent.isSameNode(child)) {
            return true;
        }
        child = child.parentNode;
        if (child.nodeType != 1) {
            child = null;
        }
    }
    return false;
    """)

def releaseCapture(elem):
    JS("""
    if ((DOM_sCaptureElem != null) && DOM_compare(elem, DOM_sCaptureElem))
        DOM_sCaptureElem = null;
    
	if (!elem.isSameNode) {
		if (elem == $wnd.__captureElem) {
			$wnd.__captureElem = null;
		}
	}
	else if (elem.isSameNode($wnd.__captureElem)) {
        $wnd.__captureElem = null;
    }
    """)



