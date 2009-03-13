# pyv8_print_fn is actually in pyv8run.py and is added to the Globals
def printFunc(objs):
    JS("""
        var s = "";
        for(var i=0; i < objs.length; i++) {
            if(s != "") s += " ";
                s += objs[i];
        }

        pyv8_print_fn(s);
    """)

# pyv8_import_module is actually in pyv8run.py and has been added to Globals.
def import_module(parent_name, module_name, dynamic_load, async):
    pyv8_import_module(parent_name, module_name)
