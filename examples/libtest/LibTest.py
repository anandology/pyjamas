from StringTest import StringTest
from ListTest import ListTest
from ClassTest import ClassTest
from SetTest import SetTest
from ArgsTest import ArgsTest
from VarsTest import VarsTest

class LibTest:	
	def onModuleLoad(self):
		ClassTest().run()
		StringTest().run()
		ListTest().run()
		SetTest().run()
		ArgsTest().run()
		VarsTest().run()




