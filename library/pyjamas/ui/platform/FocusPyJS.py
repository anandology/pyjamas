
def blur(elem):
    JS("""
    elem.blur();
    """)

def createFocusable():
    JS("""
    var e = $doc.createElement("DIV");
    e.tabIndex = 0;
    return e;
    """)

def focus(elem):
    JS("""
    elem.focus();
    """)

def getTabIndex(elem):
    JS("""
    return elem.tabIndex;
    """)

def setAccessKey(elem, key):
    JS("""
    elem.accessKey = key;
    """)

def setTabIndex(elem, index):
    JS("""
    elem.tabIndex = index;
    """)


