import sys
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
if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from JSOTest import JSOTest
    from WindowTest import WindowTest
from BuiltinTest import BuiltinTest
from MD5Test import MD5Test
from TimeModuleTest import TimeModuleTest
from TypeCompatibilityTest import TypeCompatibilityTest

def main():
    LoopTest().run()
    BoolTest().run()
    ListTest().run()
    TupleTest().run()
    FunctionTest().run()
    ExceptionTest().run()
    ClassTest().run()
    StringTest().run()
    SetTest().run()
    ArgsTest().run()
    VarsTest().run()
    AttributeTest().run()
    NameTest().run()
    DictTest().run()
    if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
        JSOTest().run()
        WindowTest().run()
    BuiltinTest().run()
    MD5Test().run()
    TimeModuleTest().run()
    TypeCompatibilityTest().run()

if __name__ == '__main__':
    main()

