# the platform name (PyV8, smjs, Mozilla, IE6, Opera, Safari etc.)
platform = '' # to be updated by app, on compile

# a dictionary of module override names (platform-specific)
overrides = None # to be updated by app, on compile

# the remote path for loading modules
loadpath = None 

stacktrace = None 

appname = None 

def setloadpath(lp):
    global loadpath
    loadpath = lp

def setappname(an):
    global appname
    appname = an

def getloadpath():
    global loadpath
    return loadpath

def addoverride(module_name, path):
    global overrides
    overrides[module_name] = path

__last_exception__ = None
__last_exception_stack__ = None
def exc_info():
    global __last_exception__
    if not __last_exception__:
        return (None, None, None)
    return (__last_exception__.error.__class__, __last_exception__.error, None)

def exc_clear():
    global __last_exception__
    __last_exception__ = None

# save_exception_stack is totally javascript, to prevent trackstack pollution
JS("""sys.save_exception_stack = function () {
    var save_stack = [];
    for (var needle in trackstack) {
        var t = new Object();
        for (var p in trackstack[needle]) {
            t[p] = trackstack[needle][p];
        }
        save_stack.push(t);
        sys.__last_exception_stack__ = save_stack;
    }
return null;
}""")

def trackstackstr(stack=None):
    global __last_exception_stack__
    if stack is None:
        stack = __last_exception_stack__
    if not stack:
        return ''
    stackstrings = []
    for s in list(stack):
        JS("var msg = eval(s.module + '.__track_lines__[' + s.lineno + ']');")
        if msg:
            stackstrings.append(msg)
        else:
            stackstrings.append('%s.py, line %d' % (s.module, s.lineno))
    return '\n'.join(stackstrings)

