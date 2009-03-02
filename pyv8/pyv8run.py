#!/usr/bin/env python

import PyV8

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
 

class Global:
    def print_fn(self, arg):
        print arg

def main():

    file_name = sys.argv[1]
    if len(sys.argv) > 2:
        module_name = sys.argv[2]
    else:
        module_name = None

    debug = 0

    parser = pyjs.PlatformParser("platform")
    parser.setPlatform("PyV8")

    if file_name[-3:] == ".py":
            file_name = file_name[:-3]

    app_translator = pyjs.AppTranslator(app_library_dirs, parser)
    app_libs = app_translator.translateLibraries(['pyjslib'], debug)
    txt      = app_translator.translate(file_name, debug=debug)

    #txt = pyjs.translate(file_name, module_name)

    PyV8.debugger.enabled = True

    e = PyV8.JSEngine(Global())

    template = """
%(app_libs)s


var __name__ = '__main__';

%(module)s

"""

    txt = template % {'app_libs': app_libs, 'module': txt}

    x = e.eval(txt)

if __name__ == '__main__':
    main()
