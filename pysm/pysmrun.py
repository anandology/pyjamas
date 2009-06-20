#!/usr/bin/env python

import spidermonkey

import sys

from os.path import join, dirname, basename, abspath
from optparse import OptionParser

currentdir = abspath(dirname(dirname(__file__)))
builddir = abspath("..")
sys.path.append(join(builddir, "pyjs"))

import pyjs

file_name = None

app_library_dirs = [
    currentdir,
    join(builddir, "library/builtins"),
    join(builddir, "library"),
    join(builddir, "addons")]

cx = None

def pysm_print_fn(arg):
    print arg

def pysm_import_module(parent_name, module_name):
    if module_name == 'sys' or module_name == 'pyjslib':
        return
    if module_name == file_name: # HACK!  imported already
        return
    exec "import %s as _module" % module_name
    cx.add_global(module_name, _module)

def main():

    global file_name

    file_name = sys.argv[1]
    if len(sys.argv) > 2:
        module_name = sys.argv[2]
    else:
        module_name = None

    debug = 0

    parser = pyjs.PlatformParser("platform", verbose=False)
    parser.setPlatform("pysm")

    if file_name.endswith(".py"):
        file_name = file_name[:-3]

    app_translator = pyjs.AppTranslator(app_library_dirs, parser,
                        verbose=False)
    app_libs, txt = app_translator.translate(file_name, debug=debug,
                                  library_modules=['_pyjs.js', 'sys', 'pyjslib'])

    #txt = pyjs.translate(file_name, module_name)

    rt = spidermonkey.Runtime()
    global cx
    cx = rt.new_context()
    cx.add_global("pysm_print_fn", pysm_print_fn)
    cx.add_global("pysm_import_module", pysm_import_module)

    template = """
var modules = {};
var pyjs_options = new Object();
pyjs_options.set_all = function (v) {
pyjs_options.arg_ignore = v;
pyjs_options.arg_count = v;
pyjs_options.arg_is_instance = v;
pyjs_options.arg_instance_type = v;
pyjs_options.arg_kwarg_dup = v;
pyjs_options.arg_kwarg_unexpected_keyword = v;
pyjs_options.arg_kwarg_multiple_values = v;
}
pyjs_options.set_all(true);
var trackstack = [];
var track = {module:'__main__', lineno: 1};
trackstack.push(track);
%(app_libs)s


%(module)s

"""

    txt = template % {'app_libs': app_libs, 'module_name': file_name,
                      'module': txt}

    txt += "sys();\n" 
    txt += "pyjslib();\n" 
    txt += "%s();\n" % file_name

    print txt

    cx.execute(txt)

if __name__ == '__main__':
    main()
