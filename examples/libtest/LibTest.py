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

class LibTest:

    def onModuleLoad(self):

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

from pyjamas import Window

if __name__ == '__main__':
    Window.alert("fred")
