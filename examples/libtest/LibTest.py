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
from LongTest import LongTest
if 1L << 31 > 0:
    has_long_type = True
    from LongTypeTest import LongTypeTest
else:
    has_long_type = True

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
if sys.platform != 'spidermonkey' and sys.platform != 'pyv8':
    from WindowTest import WindowTest
from MD5Test import MD5Test
from TimeModuleTest import TimeModuleTest
from TypeCompatibilityTest import TypeCompatibilityTest
from UrllibModuleTest import UrllibModuleTest
from Base64ModuleTest import Base64ModuleTest
from ReModuleTest import ReModuleTest

from write import writebr

class RunTests:
    def __init__(self):
        self.testlist = {}
        self.test_idx = 0

    def add(self, test):
        self.testlist[len(self.testlist)] = test

    def start_test(self):
        if self.test_idx >= len(self.testlist):
            return

        idx = self.test_idx
        self.test_idx += 1

        test_kls = self.testlist[idx]
        t = test_kls()
        t.start_next_test = getattr(self, "start_test")
        t.run()

def main():

    t = RunTests()
    t.add(LoopTest)
    t.add(BoolTest)
    t.add(ListTest)
    t.add(TupleTest)
    t.add(FunctionTest)
    t.add(ExceptionTest)
    t.add(ClassTest)
    t.add(StringTest)
    t.add(SetTest)
    t.add(ArgsTest)
    t.add(VarsTest)
    t.add(AttributeTest)
    t.add(NameTest)
    t.add(DictTest)
    t.add(BuiltinTest)
    t.add(GeneratorTest)
    t.add(LongTest)
    if has_long_type:
        t.add(LongTypeTest)
    t.add(TypeCompatibilityTest)
    t.add(MD5Test)
    t.add(TimeModuleTest)
    t.add(UrllibModuleTest)
    t.add(Base64ModuleTest)
    t.add(ReModuleTest)

    if IN_BROWSER:
        t.add(JSOTest)
        t.add(WindowTest)

    t.start_test()

if __name__ == '__main__':
    main()

