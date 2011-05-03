from UnitTest import IN_BROWSER, IN_JS, IN_BROWSER
from LoopTest import LoopTest
from NoInlineCodeTest import NoInlineCodeTest
from StringTest import StringTest
from ListTest import ListTest
from TupleTest import TupleTest
from ClassTest import ClassTest
from SetTest import SetTest, FrozenSetTest
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
from CompileTest import CompileTest

if 1L << 31 > 0:
    has_long_type = True
    from LongTypeTest import LongTypeTest
else:
    has_long_type = False

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
from DatetimeModuleTest import DatetimeModuleTest
from TypeCompatibilityTest import TypeCompatibilityTest
from UrllibModuleTest import UrllibModuleTest
from Base64ModuleTest import Base64ModuleTest
from RandomModuleTest import RandomModuleTest
from ReModuleTest import ReModuleTest
from CsvModuleTest import CsvModuleTest
from StringIOModuleTest import StringIOModuleTest

from RunTests import RunTests

def main():

    t = RunTests()
    t.add(CompileTest)
    t.add(LoopTest)
    t.add(NoInlineCodeTest)
    t.add(BoolTest)
    t.add(ListTest)
    t.add(TupleTest)
    t.add(FunctionTest)
    t.add(ExceptionTest)
    t.add(ClassTest)
    t.add(StringTest)
    t.add(SetTest)
    t.add(FrozenSetTest)
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
    t.add(DatetimeModuleTest)
    t.add(StringIOModuleTest)
    t.add(UrllibModuleTest)
    t.add(Base64ModuleTest)
    t.add(ReModuleTest)
    t.add(RandomModuleTest)
    t.add(CsvModuleTest)

    if IN_BROWSER:
        t.add(JSOTest)
        t.add(WindowTest)

    t.start_test()

if __name__ == '__main__':
    main()

