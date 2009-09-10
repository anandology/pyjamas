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
from BuiltinTest import BuiltinTest
from MD5Test import MD5Test
from TimeModuleTest import TimeModuleTest
from TypeCompatibilityTest import TypeCompatibilityTest
from UrllibModuleTest import UrllibModuleTest
from Base64ModuleTest import Base64ModuleTest
from ReModuleTest import ReModuleTest


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
    if IN_BROWSER:
        JSOTest().run()
        WindowTest().run()
    BuiltinTest().run()
    MD5Test().run()
    TimeModuleTest().run()
    TypeCompatibilityTest().run()
    UrllibModuleTest().run()
    Base64ModuleTest().run()
    ReModuleTest().run()

if __name__ == '__main__':
    main()

