#!/usr/bin/env python

import spidermonkey

import sys

from os.path import join, dirname, basename, abspath
from optparse import OptionParser

currentdir = abspath(dirname(dirname(__file__)))
builddir = abspath("..")
sys.path.append(join(builddir, "pyjs"))

import pyjs


app_library_dirs = [
    currentdir,
    join(builddir, "library/builtins"),
    join(builddir, "library"),
    join(builddir, "addons")]
 

def pysm_print_fn(arg):
    print arg
def pysm_import_module(parent_name, module_name):
    pass

def main():

    file_name = sys.argv[1]
    if len(sys.argv) > 2:
        module_name = sys.argv[2]
    else:
        module_name = None

    debug = 0

    parser = pyjs.PlatformParser("platform", verbose=False)
    parser.setPlatform("pysm")

    if file_name[-3:] == ".py":
            file_name = file_name[:-3]

    app_translator = pyjs.AppTranslator(app_library_dirs, parser, verbose=False)
    app_libs, txt = app_translator.translate(file_name, debug=debug,
                                  library_modules=['_pyjs.js', 'sys', 'pyjslib'])

    #txt = pyjs.translate(file_name, module_name)

    rt = spidermonkey.Runtime()
    cx = rt.new_context()
    cx.add_global("pysm_print_fn", pysm_print_fn)
    cx.add_global("pysm_import_module", pysm_import_module)

    template = """
%(app_libs)s


%(module)s

"""

    txt = template % {'app_libs': app_libs, 'module_name': file_name,
                      'module': txt}

    for mod_name in app_translator.library_modules:
        txt += "%s();\n" % mod_name

    cx.execute(txt)

if __name__ == '__main__':
    main()
