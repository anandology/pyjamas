#!/usr/bin/env python

import PyV8

import os
import sys
import compiler

from os.path import join, dirname, basename, abspath
from optparse import OptionParser

usage = """
  usage: %prog [options] <application module name or path>
"""

currentdir = abspath(dirname(__file__))
pyjspth = abspath(join(dirname(__file__), ".."))
sys.path = [(join(pyjspth, "pyjs", "src"))] + sys.path

import pyjs

pyjs.pyjspth = pyjspth
pyjs.path += [os.path.join(pyjspth, 'library'),
            os.path.join(pyjspth, 'addons'),
]


from pyjs import translator
from linker import PLATFORM, PyV8Linker, add_linker_options
from jsglobal import Global

def main():
    usage = """
    usage: %prog [ options ] [ -c command | module_name | script | - ] [ -- arguments ]
    """
    parser = OptionParser(usage = usage)
    translator.add_compile_options(parser)

    parser.add_option(
        "--dynamic",
        dest="unlinked_modules",
        action="append",
        help="regular expression for modules that will not be linked"
        "and thus loaded dynamically"
        )
    parser.add_option(
        "-c",
        dest="command",
        help="Python command to run")
    
    # override the default because we want print
    parser.set_defaults(print_statements=True)
    add_linker_options(parser)
    options, args = parser.parse_args()
    IS_REPL = False
    if len(args) == 0 or args[0] == '-':
        IS_REPL = True
        modules = ['main']
    else:
        modules = args

    for d in options.library_dirs:
        pyjs.path.append(os.path.abspath(d))

    #print "paths:", pyjs.path
    translator_arguments = translator.get_compile_options(options)
    linker = PyV8Linker(modules, output=options.output,
                        platforms=[PLATFORM],
                        path=pyjs.path,
                        compiler=compiler,
                        translator_arguments=translator_arguments)
    linker()
    
    fp = open(linker.out_file_mod, 'r')
    txt = fp.read()
    fp.close()

    #PyV8.debugger.enabled = True
    
    # create a context with an explicit global
    g = Global()
    ctxt = PyV8.JSContext(g)
    g.__context__ = ctxt
    # enter the context
    ctxt.enter()
    try:
        x = ctxt.eval(txt)
    except Exception, e:
        raise
        #ei = ctxt.locals['$pyjs']['loaded_modules']['sys']['exc_info']()
        #print ei
    
    if IS_REPL:
        from repl import REPL
        REPL(compiler, linker, translator_arguments, g, ctxt)()


if __name__ == '__main__':
    main()

