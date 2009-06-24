# pyv8_print_fn is actually in pyv8run.py and is added to the Globals
def printFunc(objs, newline):
    JS("""
        var s = "";
        for(var i=0; i < objs.length; i++) {
            if(s != "") s += " ";
                s += objs[i];
        }

        pyv8_print_fn(s);
    """)

# pyv8_import_module is actually in pyv8run.py and has been added to Globals.
def import_module(syspath, parent_name, module_name, dynamic_load, async, init):
    JS("""
    module = $pyjs.modules_hash[module_name];
    if (typeof module == 'function' && module.__was_initialized__ == true) {
        return null;
    }
    if (module_name == 'sys' || module_name == 'pyjslib') {
        module();
        return null;
    }
    """)
    names = module_name.split(".")
    importName = ''
    # Import all modules in the chain (import a.b.c)
    for name in names:
        importName += name
        JS("""module = $pyjs.modules_hash[importName];""")
        if not isUndefined(module):
            # Not initialized, but present. Must be pyjs module.
            if JS("module.__was_initialized__ != true"):
                # Module wasn't initialized
                module()
        else:
            # Get a pytjon module from PyV8
            initialized = False
            try:
                JS("initialized = (module.__was_initialized__ != true)")
            except:
                pass
            if not initialized:
                # Module wasn't initialized
                module = pyv8_import_module(parent_name, module_name)
                module.__was_initialized__ = True
                JS("""$pyjs.modules_hash[importName] = module""")
        importName += '.'
    name = names[0]
    JS("""$pyjs.modules[name] = $pyjs.modules_hash[module];""")
    return None
