#!/usr/bin/env python

import PyV8

import sys

from os.path import join, dirname, basename, abspath
from optparse import OptionParser

usage = """
  usage: %prog [options] <application module name or path>
"""

currentdir = abspath(dirname(dirname(__file__)))
builddir = abspath("..")
sys.path.append(join(builddir, "pyjs"))

import pyjs


app_library_dirs = [
    currentdir,
    join(builddir, "library/builtins"),
    join(builddir, "library"),
    join(builddir, "addons")]
 

# Create a python class to be used in the context
class Global(PyV8.JSClass):
    def pyv8_print_fn(self, arg):
        print arg
    def pyv8_import_module(self, parent_name, module_name):
        exec "import " + module_name
        return locals()[module_name]

def main():

    parser = OptionParser(usage = usage)
    pyjs.add_compile_options(parser)
    parser.add_option("-o", "--output",
        dest="output",
        help="File to which the generated javascript should be written")

    parser.add_option("-i", "--input",
        dest="input",
        help="File from which the generated javascript should be read")

    parser.set_defaults(\
        output = None,
        input = None,
    )
    (options, args) = parser.parse_args()

    file_name = args[0]
    if len(args) > 1:
        module_name = args[1]
    else:
        module_name = None

    debug = 0

    if options.input:
        txt = open(options.input, 'r').read()
    else:
        parser = pyjs.PlatformParser("platform", verbose=False)
        parser.setPlatform("PyV8")

        if file_name[-3:] == ".py":
                file_name = file_name[:-3]

        app_translator = pyjs.AppTranslator(
                app_library_dirs, parser,
                verbose = False,
                debug = options.debug,
                print_statements = options.print_statements,
                function_argument_checking = options.function_argument_checking,
                attribute_checking = options.attribute_checking,
                source_tracking = options.source_tracking,
                line_tracking = options.line_tracking,
                store_source = options.store_source,
        )
        app_libs, txt = app_translator.translate(file_name, debug=debug,
                              library_modules=['_pyjs.js', 'sys', 'pyjslib'])

        template = """
var $pyjs = new Object();
$pyjs.modules = {};
$pyjs.modules_hash = {};
$pyjs.options = new Object();
$pyjs.options.set_all = function (v) {
    $pyjs.options.arg_ignore = v;
    $pyjs.options.arg_count = v;
    $pyjs.options.arg_is_instance = v;
    $pyjs.options.arg_instance_type = v;
    $pyjs.options.arg_kwarg_dup = v;
    $pyjs.options.arg_kwarg_unexpected_keyword = v;
    $pyjs.options.arg_kwarg_multiple_values = v;
}
$pyjs.options.set_all(true);
$pyjs.trackstack = [];
$pyjs.track = {module:'__main__', lineno: 1};
$pyjs.trackstack.push($pyjs.track);
%(app_libs)s


%(module)s

"""

        txt = template % {'app_libs': app_libs, 'module_name': file_name,
                          'module': txt}

        #for mod_name in app_translator.library_modules:
        for mod_name in ['sys', 'pyjslib', file_name]:
            txt += "%s();\n" % mod_name

    if options.output:
        fp = open(options.output, 'w')
        fp.write(txt)
        fp.close()

    PyV8.debugger.enabled = True
    # create a context with an explicit global
    ctxt = PyV8.JSContext(Global())
    # enter the context
    ctxt.enter()
    
    x = ctxt.eval(txt)

if __name__ == '__main__':
    main()
