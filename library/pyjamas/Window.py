from __pyjamas__ import JS
from pyjamas import Location

closingListeners = None
resizeListeners = None

def addWindowCloseListener(listener):
    init_listeners()
    global closingListeners
    closingListeners.append(listener)

def addWindowResizeListener(listener):
    init_listeners()
    global resizeListeners
    resizeListeners.append(listener)

def alert(msg):
    JS("""
    $wnd.alert(msg);
    """)

def confirm(msg):
    JS("""
    return $wnd.confirm(msg);
    """)

def prompt(msg, defaultReply=""):
    JS("""
        return $wnd.prompt(msg, defaultReply);
    """)

def enableScrolling(enable):
   JS("""
   $doc.body.style.overflow = enable ? 'auto' : 'hidden';
   """)

def scrollBy(x, y):
    JS("""
    $wnd.scrollBy(x, y);
    """)

def scroll(x, y):
    JS("""
    $wnd.scroll(x, y);
    """)

def getClientHeight():
    JS("""
    if ($wnd.innerHeight)
        return $wnd.innerHeight;
    return $doc.body.clientHeight;
    """)

def getClientWidth():
    JS("""
    if ($wnd.innerWidth)
        return $wnd.innerWidth;
    return $doc.body.clientWidth;
    """)

def setLocation(url):
    JS("""
    $wnd.location = url;
    """)
 
location = None

def getLocation():
    global location
    JS("""
    if(!Window.location)
       Window.location = Location.Location($wnd.location);
    return Window.location;
    """)
 
 
def getTitle():
    JS("""
    return $doc.title;
    """)

def open(url, name, features):
    JS("""
    $wnd.open(url, name, features);
    """)

def removeWindowCloseListener(listener):
    global closingListeners
    closingListeners.remove(listener)

def removeWindowResizeListener(listener):
    global resizeListeners
    resizeListeners.remove(listener)

def setMargin(size):
    JS("""
    $doc.body.style.margin = size;
    """)

def setTitle(title):
    JS("""
    $doc.title = title;
    """)

def setOnError(onError):
    if (not callable(onError)):
        raise TypeError("object is not callable")
    JS("""\
    $wnd.onerror=function(msg, url, linenumber){
        return onError(msg, url, linenumber);
    }
    """)

def onError(msg, url, linenumber):
    dialog=JS("""$doc.createElement("div")""")
    dialog.className='errordialog'
    # Note: trackstackstr is a global javascript array
    tracestr = sys.trackstackstr(trackstack.slice(0,-1))
    tracestr = tracestr.replace("\n", "<br />\n&nbsp;&nbsp;&nbsp;")
    dialog.innerHTML='&nbsp;<b style="color:red">JavaScript Error: </b>' + \
        msg +' at line number ' + linenumber +'. Please inform webmaster.' + \
        '<br />&nbsp;&nbsp;&nbsp;' + tracestr
    JS("""$doc.body.appendChild(dialog)""")
    return True

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

def init_listeners():
    global closingListeners
    global resizeListeners
    if not closingListeners:
        closingListeners = []
    if not resizeListeners:
        resizeListeners = []

def init():
    global onError
    init_listeners()
    JS("""
    $wnd.__pygwt_initHandlers(
        function() {
            Window.onResize();
        },
        function() {
            return Window.onClosing();
        },
        function() {
            Window.onClosed();
            /*$wnd.onresize = null;
            $wnd.onbeforeclose = null;
            $wnd.onclose = null;*/
        }
    );
    """)
    setOnError(onError)

init()

