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
import re
import urllib2
import csv
import collections

test_msg_re = re.compile("""\s*([\w]+) (Known issue|Test failed) \(([\w\/]+)\) \: (.+)$""")
issue_no_re = re.compile("""\#(\d+)""")
test_passed_re = re.compile("""\s*(\w+)\: Passed (\d+) \/ (\d+) tests( \((\d+) failed\))?""")
currentdir = path.abspath(path.dirname(__file__))

class PyjamasTester(object):
    parser = OptionParser()
    parser.add_option(
        "--verbose", "-v",
        dest="verbose",
        action="store_true",
        default=False,
        help="Show detailed information")
    parser.add_option(
        "--notracker",
        dest="tracker",
        action="store_false",
        default=True,
        help="Do not load data from issue tracker")
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
    parser.add_option(
        "--trackerreport",
        dest="tracker_report",
        action="store_true",
        default=False,
        help="Provide report on tracker issues lacking failing tests"
        )
        
    def __init__(self):
        self.options, args = self.parser.parse_args()
        
        self.tracker_url = "http://code.google.com/p/pyjamas/issues/csv"
        if not path.isabs(self.options.pyv8):
            self.options.pyv8 = path.join(currentdir, self.options.pyv8)
        
        if not path.isabs(self.options.examples_path):
            self.options.examples_path = path.join(currentdir, self.options.examples_path)
            
        self.testsresults = []
        self.testsknown = []
        
        if self.options.libtest_run:
            self._test(self.test_libtest_cpython)
        
        if self.options.utils_run:
            self._test(self.test_utilities)
        
        if self.options.libtest_run:
            if self.options.pyv8_run:
                self._test(self.test_libtest_pyv8)
        
        self.issues = {}
        if self.options.tracker:
            self.get_tracker_issues()
        
        self.print_results()
        


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
        return stdout_value, stderr_value

    def test_libtest_cpython(self):
        return self.parse_cmd_output(
            *self.run_cmd(opts="LibTest.py", cwd=path.join(self.options.examples_path, 'libtest'))
            )

    def test_utilities(self):
        return []

    def test_libtest_pyv8(self):
        return self.parse_cmd_output(
            *self.run_cmd(cmd=self.options.pyv8,
                          opts=["--strict", "--dynamic '^I18N[.].*.._..'", "LibTest", 
                                "`find I18N -name ??_??.py`"],
                          cwd=path.join(self.options.examples_path, 'libtest'))
            )

    def test_libtest_browsers(self):
        pass

    def test_examples_compile(self):
        pass

    def test_examples_browsers(self):
        pass

    def test_examples_pyjd(self):
        pass
    
    def parse_cmd_output(self, stdout_value, stderr_value=None):
        """
        Parse stdout/stderr into list of dicts
        
        .. TODO:: handle stderr (exceptions)
        """
        res = []
        for line in stdout_value.split('\n'):
            m = test_msg_re.match(line)
            if m:
                groups = m.groups()
                test = dict(
                    cls = groups[0],
                    status = (groups[1] == 'Known issue') and 'known' or 'failed',
                    name = groups[2],
                    message = groups[3]
                    )
                if test['status'] == 'known':
                    test['issues'] = issue_no_re.findall(test['message'])
                res.append(test)
            else:
                m = test_passed_re.match(line)
                if m:
                    groups = m.groups()
                    test = dict(
                        cls = groups[0],
                        status = "passed",
                        name = groups[0],
                        count = int(groups[1])
                        )
                    res.append(test)
        return res
                    
        
        
    def _test(self, method):
        name = method.im_func.func_name
        d = dict(name=name, 
                 tests=[], failed_list=[], known_list=[],
                 total=0, passed=0,
                 failed=0, known=0, err=None)
        self.testsresults.append(d)
        try:
            d['tests'] = method()
        except Exception, e:
            print e
            d['err'] = e
            return False
        
        for test in d['tests']:
            if test['status'] == 'passed':
                d['passed'] += test['count']
            elif test['status'] == 'failed':
                d['failed'] += 1
                d['failed_list'].append(test)
            elif test['status'] == 'known':
                d['known'] += 1
                d['known_list'].append(test)
                self.testsknown.append((d, test))
        d['total'] = d['passed'] + d['failed'] + d['known']
        
    def get_tracker_issues(self):
        print "Fetching issues csv from %s" % self.tracker_url
        csv_data = urllib2.urlopen(self.tracker_url)
        reader = csv.reader(csv_data)
        issue_cls = None
        for row in reader:
            if not issue_cls:
                issue_cls = collections.namedtuple("Issue", " ".join(row))
            elif row:
                issue = issue_cls(*row)
                self.issues[issue.ID] = issue
        print "    received %s issues from tracker" % len(self.issues)
        
    def print_results(self):
        """
        .. TODO:: handle test_pack['err']
        """
        print "="*30
        print " Test results "
        print "="*30
        is_failed = False
        is_bad_issue = False
        if self.options.verbose:
            for test_pack in self.testsresults:
                print "-"*30
                print ("%(name)s: total %(total)s, passed %(passed)s,"
                " known %(known)s, failed %(failed)s" % test_pack)                
                print "-"*30
                if test_pack['failed'] > 0:
                    is_failed = True
                for test in test_pack['known_list']:
                    print "    Known issue: %(cls).%(name)s: %(message)s" % test
                for test in test_pack['failed_list']:
                    print "[!] Failed test: %(cls).%(name)s: %(message)s" % test
        else:
            for test_pack in self.testsresults:
                print ("%(name)s: total %(total)s, passed %(passed)s,"
                " known %(known)s, failed %(failed)s" % test_pack)
                if test_pack['failed'] > 0:
                    is_failed = True
            for test_pack in self.testsresults:
                if test_pack['failed_list']:
                    print "-"*30
                    print test_pack['name'], "failed tests:"
                    for test in test_pack['failed_list']:
                        print "[!] %(cls)s.%(name)s: %(message)s" % test
        
        if self.issues:
            referenced = []
            for test_pack, test in self.testsknown:
                for issue_id in test['issues']:
                    referenced.append(issue_id)
                    if not issue_id in self.issues:
                        if not is_bad_issue:
                            print "-"*30
                            print "Some issues referenced as known are not open on tracker:"
                            is_bad_issue = True
                        print "[!] Issue #%s is not open, referenced by %s:%s.%s: %s" % (
                            issue_id,
                            test_pack['name'],
                            test['cls'], test['name'], test['message'])

            
            if self.options.tracker_report:
                print "="*30
                print " Issues test coverage report"
                print "="*30
                for issue_id, issue in self.issues.iteritems():
                    if not issue_id in referenced:
                        print "    No test for issue #%(ID)s '%(Summary)s'" % issue._asdict()
            
                        


        

if __name__ == '__main__':
    PyjamasTester()
