#!/usr/bin/python
"""
Utility to run all possible tests and provide overall results. 

Test plan:

* Test LibTest with CPython
* Test all utilities:

  * pyjsbuild
  * pyjscompile
  * pyv8run
  * pyjampiler

* Test LibTest with PyV8
* Test LibTest in browsers (needs further research)
* Compile all examples
* Test examples in browsers (needs further research)
* Test examples in pyjd

Should be also reflected at http://pyjs.org/wiki/githowto/

"""

from optparse import OptionParser
from os import path
import subprocess
import os

class PyjamasTester(object):
    parser = OptionParser()
    parser.add_option(
        "--cpython",
        dest="cpython",
        action="store",
        default="/usr/bin/python",
        help="Path to CPython executable"
        )
    parser.add_option(
        "--pyv8",
        dest="pyv8",
        action="store",
        default="pyv8/pyv8run.py",
        help="Path to PyV8-based interpreter"
        )
    parser.add_option(
        "--nolibtest",
        dest="libtest_run",
        action="store_false",
        default=True,
        help="Do not run any LibTest tests"
        )
    parser.add_option(
        "--nopyv8",
        dest="pyv8_run",
        action="store_false",
        default=True,
        help="Do not run any PyV8 tests"
        )
    parser.add_option(
        "--nobrowsers",
        dest="browsers_run",
        action="store_false",
        default=True,
        help="Do not run any browsers tests"
        )
    parser.add_option(
        "--nopyjd",
        dest="pyjd_run",
        action="store_false",
        default=True,
        help="Do not run any browsers tests"
        )
    parser.add_option(
        "--noutils",
        dest="utils_run",
        action="store_false",
        default=True,
        help="Do not test utilities"
        )
    parser.add_option(
        "--noexamples",
        dest="examples_run",
        action="store_false",
        default=True,
        help="Do not test examples"
        )
    parser.add_option(
        "--examples",
        dest="examples_path",
        action="store",
        default="examples/",
        help="Path to examples dir"
        )
        
    def __init__(self):
        self.options, args = self.parser.parse_args()
        
        if self.options.libtest_run:
            self.test_libtest_cpython()
        
        if self.options.utils_run:
            self.test_utilities()
        
        if self.options.libtest_run:
            if self.options.pyv8_run:
                self.test_libtest_pyv8()

    def run_cmd(self, cmd=None, opts=None, cwd=None):
        if not cmd:
            cmd = self.options.cpython
        cmd = path.abspath(cmd)
        if not cwd:
            cwd = '.'
        cwd = path.abspath(cwd)
        if opts:
            if not isinstance(opts, list):
                opts = [opts]
            cmd = ' '.join([cmd] + opts)
        print "Running `%s` at \"%s\"" % (cmd, cwd)
        proc = subprocess.Popen(cmd,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True,
                                cwd=cwd,
                                env=os.environ
                                )
        stdout_value, stderr_value = proc.communicate('')
        print stdout_value
        print stderr_value

    def test_libtest_cpython(self):
        self.run_cmd(opts="LibTest.py", cwd=path.join(self.options.examples_path, 'libtest'))

    def test_utilities(self):
        pass

    def test_libtest_pyv8(self):
        self.run_cmd(cmd=self.options.pyv8,
                     opts=["--strict", "--dynamic '^I18N[.].*.._..'", "LibTest", "`find I18N -name ??_??.py`"],
                     cwd=path.join(self.options.examples_path, 'libtest'))

    def test_libtest_browsers(self):
        pass

    def test_examples_compile(self):
        pass

    def test_examples_browsers(self):
        pass

    def test_examples_pyjd(self):
        pass


if __name__ == '__main__':
    PyjamasTester()
