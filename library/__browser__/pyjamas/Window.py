
def setOnError(onError):
    if (not callable(onError)):
        raise TypeError("object is not callable")
    JS("""\
    $wnd.onerror=function(msg, url, linenumber){
        return onError(msg, url, linenumber);
    }
    """)

def onError(msg, url, linenumber):
    dialog=doc().createElement("div")
    dialog.className='errordialog'
    # Note: $pyjs.trackstack is a global javascript array
    tracestr = sys.trackstackstr(JS("$pyjs.trackstack.slice(0,-1)"))
    tracestr = tracestr.replace("\n", "<br />\n&nbsp;&nbsp;&nbsp;")
    dialog.innerHTML='&nbsp;<b style="color:red">JavaScript Error: </b>' + \
        msg +' at line number ' + linenumber +'. Please inform webmaster.' + \
        '<br />&nbsp;&nbsp;&nbsp;' + tracestr
    doc().body.appendChild(dialog)
    return True

def alert(msg):
    wnd().alert(msg)

def confirm(msg):
    return wnd().confirm(msg)

def prompt(msg, defaultReply=""):
    return wnd().prompt(msg, defaultReply)

def init_listeners():
    global closingListeners
    global resizeListeners
    if not closingListeners:
        closingListeners = []
    if not resizeListeners:
        resizeListeners = []

def init():
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


