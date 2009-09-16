from UnitTest import IN_BROWSER, IN_JS, IN_BROWSER
from LoopTest import LoopTest
from StringTest import StringTest
from ListTest import ListTest
from TupleTest import TupleTest
from ClassTest import ClassTest
from SetTest import SetTest
from ArgsTest import ArgsTest
from VarsTest import VarsTest
from AttributeTest import AttributeTest
from ExceptionTest import ExceptionTest
from BoolTest import BoolTest
from FunctionTest import FunctionTest
from NameTest import NameTest
from DictTest import DictTest
from BuiltinTest import BuiltinTest
from GeneratorTest import GeneratorTest

if IN_JS:
    from JSOTest import JSOTest
else:
    import os, sys
    here = os.path.abspath(os.path.dirname(__file__))
    library = os.path.join(os.path.dirname(os.path.dirname(
        here)), 'library')
    sys.path.append(library)

# spidermonkey has no window implementation, but we like to test the
# import of pyjamas.Window in pure python too
import sys
if sys.platform != 'spidermonkey':
    from WindowTest import WindowTest
from MD5Test import MD5Test
from TimeModuleTest import TimeModuleTest
from TypeCompatibilityTest import TypeCompatibilityTest
from UrllibModuleTest import UrllibModuleTest
from Base64ModuleTest import Base64ModuleTest
from ReModuleTest import ReModuleTest

from pyjamas import log

class RunTests:
    def __init__(self, tests):
        self.tests = tests
        self.test_idx = 0

    def start_test(self):
        if self.test_idx >= len(self.tests):
            return
        idx = self.test_idx
        self.test_idx += 1

        test_kls = self.tests[idx]
        t = test_kls()
        t.start_next_test = self.start_test
        t.run()

def main():

    test_classes = [ LoopTest,
        BoolTest,
        ListTest,
        TupleTest,
        FunctionTest,
        ExceptionTest,
        ClassTest,
        StringTest,
        SetTest,
        ArgsTest,
        VarsTest,
        AttributeTest,
        NameTest,
        DictTest,
        BuiltinTest,
        GeneratorTest,
        TypeCompatibilityTest,
        MD5Test,
        TimeModuleTest,
        UrllibModuleTest,
        Base64ModuleTest,
        ReModuleTest,
    ]
    if IN_BROWSER:
        test_classes.append(JSOTest)
        test_classes.append(WindowTest)

    t = RunTests(test_classes)
    t.start_test()

if __name__ == '__main__':
    main()

