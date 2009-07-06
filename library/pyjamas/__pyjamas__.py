# This is the gtk-dependent __pyjamas__ module.
# For the pyjamas/javascript version, see platform/__pyjamas__PyJS.py

""" This module interfaces between PyWebkitGTK and the Pyjamas API,
    to get applications kick-started.
"""
import sys
if not sys.platform in  ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from traceback import print_stack

main_frame = None

def noSourceTracking(*args):
    pass

def unescape(str):
    s = s.replace("&amp;", "&")
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&quot;", '"')
    return s

def set_main_frame(frame):
    global main_frame
    main_frame = frame
    from pyjamas import DOM
    # ok - now the main frame has been set we can initialise the
    # signal handlers etc.
    DOM.init()

def get_main_frame():
    return main_frame

def doc():
    try:
        return main_frame.getGdomDocument() # webkit
    except:
        return main_frame.get_dom_window().document # hulahop

def wnd():
    """ try to avoid using this function until a bug in pywebkitgtk
        has been tracked down
    """
    try:
        return main_frame.getDomWindow() # webkit
    except:
        return main_frame.get_dom_window() # hulahop

def JS(code):
    """ try to avoid using this function, it will only give you grief
        right now...
    """
    ctx = main_frame.gjs_get_global_context()
    try:
        return ctx.eval(code)
    except:
        print "code", code
        print_stack()

pygwt_moduleNames = []

def pygwt_processMetas():
    from pyjamas import DOM
    metas = doc().getElementsByTagName("meta")
    for i in range(metas.length):
        meta = metas.item(i)
        name = DOM.getAttribute(meta, "name")
        if name == "pygwt:module":
            content = DOM.getAttribute(meta, "content")
            if content:
                pygwt_moduleNames.append(content)
    return pygwt_moduleNames

class console:

    @staticmethod
    def error(msg):
        print "TODO CONSOLE:", msg

