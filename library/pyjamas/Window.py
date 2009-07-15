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
    closingListeners.append(listener)

def addWindowResizeListener(listener):
    resizeListeners.append(listener)

def alert(txt):
    #get_main_frame()._alert(txt)

    def close(w):
        dialog.destroy()
    dialog = gtk.Dialog("Alert", None, gtk.DIALOG_DESTROY_WITH_PARENT)
    label = gtk.Label(txt)
    dialog.vbox.add(label)
    label.show()
    button = gtk.Button("OK")
    dialog.action_area.pack_start (button, True, True, 0)
    button.connect("clicked", close)
    button.show()
    dialog.run ()

def confirm(msg):
    return wnd().confirm(msg)

def prompt(msg, defaultReply=""):
    return wnd().prompt(msg, defaultReply)

def enableScrolling(enable):
    doc().body.style.overflow = enable and 'auto' or 'hidden'

def scrollBy(x, y):
    wnd().scrollBy(x, y)

def scroll(x, y):
    wnd().scroll(x, y)

def getClientHeight():
    height = wnd().innerHeight
    if height:
        return height
    return doc().body.clientHeight;

def getClientWidth():
    width = wnd().innerWidth
    if width:
        return width
    return doc().body.clientWidth;

def setLocation(url):
    w = wnd()
    w.location = url

location = None

def getLocation():
    global location
    if not location:
        location = Location.Location(wnd().location)
    return location
 
def getTitle():
    return doc.title

def open(url, name, features):
    document.parent.open(url, name, features)

def removeWindowCloseListener(listener):
    closingListeners.remove(listener)

def removeWindowResizeListener(listener):
    resizeListeners.remove(listener)

def setMargin(size):
    doc().body.style.margin = size;

def setTitle(title):
    d = doc()
    d.title = title

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
    ret = None
    for listener in closingListeners:
        msg = listener.onWindowClosing()
        if ret is None:
            ret = msg
    return ret

def fireResizedAndCatch(handler):
    # FIXME - need implementation
    pass

def fireResizedImpl():
    for listener in resizeListeners:
        listener.onWindowResized(getClientWidth(), getClientHeight())

def init():
    pass

init()

import gtk

