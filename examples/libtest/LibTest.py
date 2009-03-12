from StringTest import StringTest
from ListTest import ListTest
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
from JSOTest import JSOTest

def main(self):

    BoolTest().run()
    FunctionTest().run()
    ExceptionTest().run()
    ClassTest().run()
    StringTest().run()
    ListTest().run()
    SetTest().run()
    ArgsTest().run()
    VarsTest().run()
    AttributeTest().run()
    NameTest().run()
    DictTest().run()
    JSOTest().run()

if __name__ == '__main__':
    main()


