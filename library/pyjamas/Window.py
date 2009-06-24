# This is the gtk-dependent Window module.
# For the pyjamas/javascript version, see platform/WindowPyJS.py

"""
    Window provides access to the DOM model's global Window.
"""
import sys
if sys.platform not in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:

    import pygtk
    pygtk.require('2.0')
    import gtk

    from pyjamas.__pyjamas__ import JS, doc, get_main_frame, wnd

    closingListeners = []
    resizeListeners = []
else:
    from __pyjamas__ import JS
    from __pyjamas__ import unescape # for Location IE6 and Opera
    closingListeners = None
    resizeListeners = None

from pyjamas import Location

def init_listeners():
    pass

def addWindowCloseListener(listener):
    global closingListeners
    closingListeners.append(listener)

def addWindowResizeListener(listener):
    global resizeListeners
    resizeListeners.append(listener)

def alert(msg):
    wnd().alert(msg)

def confirm(msg):
    print "TODO", msg
    alert("Window.confirm() is still on the TODO list. sorry!")
    return False
    JS("""
    window.confirm("%s");
    """ % msg)

def prompt(msg, defaultReply=""):
    print "TODO", msg
    alert("Window.prompt() is still on the TODO list. sorry!")

def enableScrolling(enable):
    doc().props.body.props.style.overflow = enable and 'auto' or 'hidden'

def scrollBy(x, y):
    print "TODO: scrollBy", x, y
    pass

def scroll(x, y):
    print "TODO: scroll", x, y
    pass

def getClientHeight():
    height = wnd().props.inner_height
    if height:
        return height
    return doc().props.body.props.client_height;

def getClientWidth():
    width = wnd().props.inner_width
    if width:
        return width
    return doc().props.body.props.client_width;

def setLocation(url):
    print "TODO - setLocation", url
    pass

location = None

def getLocation():
    global location
    if not location:
        print dir(wnd())
        location = Location.Location(wnd().props.location)
    return location
    JS("""
    if(!Window_location)
       Window_location = Location_Location($wnd.location);
    return Window_location;
    """)
 
 
def getTitle():
    return doc.props.title

def open(url, name, features):
    JS("""
    document.parent.open('%s', '%s', '%s');
    """ % (url, name, features))

def removeWindowCloseListener(listener):
    global closingListeners
    closingListeners.remove(listener)

def removeWindowResizeListener(listener):
    global resizeListeners
    resizeListeners.remove(listener)

def setMargin(size):
    doc().props.body.props.style.margin = size;

def setTitle(title):
    doc().props.title = title

def setOnError(onError):
    pass

def onError(msg, url, linenumber):
    pass

# TODO: call fireClosedAndCatch
def onClosed():
    fireClosedImpl()

# TODO: call fireClosingAndCatch
def onClosing():
    fireClosingImpl()

# TODO: call fireResizedAndCatch
def onResize():
    fireResizedImpl()

def fireClosedAndCatch(handler):
    # FIXME - need implementation
    pass

def fireClosedImpl():
    global closingListeners
    
    for listener in closingListeners:
        listener.onWindowClosed()

def fireClosingAndCatch(handler):
    # FIXME - need implementation
    pass

def resize(width, height):
    print "resize", width, height
    wnd().resize_to(width, height)
    wnd().resize_by(width, height)

def fireClosingImpl():
    global closingListeners
    
    ret = None
    for listener in closingListeners:
        msg = listener.onWindowClosing()
        if ret == None:
            ret = msg
    return ret

def fireResizedAndCatch(handler):
    # FIXME - need implementation
    pass

def fireResizedImpl():
    global resizeListeners

    for listener in resizeListeners:
        listener.onWindowResized(getClientWidth(), getClientHeight())

def init():
    pass

init()
