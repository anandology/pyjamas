from UnitTest import UnitTest

# XXX fails with a JavaScript error: "In application LibTest -
# undefined: set is not defined
# pyjslib.py, line 1484
# pyjslib.py, line 206
# SetTest.py, line 5
# try:
#     # try to use the built-in set type
#     Set = set
# except NameError:
#     # fall back to sets module
#     from sets import Set
from sets import Set


class SetTest(UnitTest):
	def __init__(self):
		UnitTest.__init__(self)

	def getName(self):
		return "Set"

	def testInit(self):
		value = Set(['a', 'b', 'c'])
		
		self.assertTrue('b' in value)
		self.assertTrue('d' not in value)

	def testAdd(self):
		value = Set()
		value.add("a")
		value.add("b")
		value.add("a")		
		
		self.assertTrue('a' in value)
		self.assertTrue('c' not in value)
		self.assertTrue(len(value) is 2)

	def testRemove(self):
		value = Set(['a', 'b', 'c'])
		value.remove('a')
		
		self.assertTrue('a' not in value)
		self.assertTrue('b' in value)

	def testIter(self):
		items = ['a', 'b', 'c']
		value = Set(items)
		
		for i in value:
			items.remove(i)			

		self.assertTrue(len(items) is 0)

	def testAddObject(self):
		v1 = DummyClass('a')
		v2 = DummyClass('b')
		v3 = DummyClass('b')
		v4 = DummyClass('c')
		items = [v1, v2, v3]

		value = Set()
		value.add(v1)
		value.add(v2)
		value.add(v1)
		value.add(v3)
		
		self.assertTrue(v1 in value)
		self.assertTrue(v2 in value)
		self.assertTrue(v3 in value)
		self.assertTrue(v4 not in value)
		self.assertTrue(len(value) is 3)
		
		i = 0
		for v in value:
			if v.getValue() != items[i].value:
				self.assertTrue(False)
			i += 1


class DummyClass:
	def __init__(self, value):
		self.value = value
	
	def getValue(self):
		return self.value

