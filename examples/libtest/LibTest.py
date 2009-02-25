from StringTest import StringTest
from ListTest import ListTest
from ClassTest import ClassTest
from SetTest import SetTest
from ArgsTest import ArgsTest
from VarsTest import VarsTest
from AttributeTest import AttributeTest
from ExceptionTest import ExceptionTest

class LibTest:
	def onModuleLoad(self):
		ExceptionTest().run()
		ClassTest().run()
		StringTest().run()
		ListTest().run()
		SetTest().run()
		ArgsTest().run()
		VarsTest().run()
		AttributeTest().run()

