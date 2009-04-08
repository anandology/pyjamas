from UnitTest import UnitTest

class ClassTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Class"

    # test Class.x
    def testClassVars(self):
        expected_result1="test"
        expected_result2=1

        # check class var value without instance
        self.assertEquals(ExampleClass.x, expected_result1)
        self.assertEquals(ExampleClass.x.upper(), expected_result1.upper())

        # verify class var value for instances
        y = ExampleClass()
        self.assertEquals(y.x, expected_result1)

        # modify class var
        ExampleClass.x = expected_result2
        self.assertEquals(ExampleClass.x, expected_result2)

        # verify that class var changed for NEW instances
        z = ExampleClass()
        self.assertEquals(z.x, expected_result2)

        # verify that class var changed for EXISTING instances
        self.assertEquals(y.x, expected_result2)

    # test Class().x
    def testInheritedProperties(self):
        expected_result1="test"
        expected_result2=1
        expected_result3="other"

        # check parent property
        obj1 = ExampleParentClass()
        self.assertEquals(obj1.x, expected_result1)

        # check default inherited property
        obj1.x = expected_result2
        obj2 = ExampleChildClass()
        self.assertEquals(obj2.x, expected_result1)

        # change inherited property
        obj2.x = expected_result3
        self.assertEquals(obj2.x, expected_result3)

        # verify that parent class properties were NOT changed
        self.assertEquals(obj1.x, expected_result2)

    # test Class().anObject
    def testInheritedPropertyObjects(self):
        expected_result1 = "another"
        expected_result2 = "other"

        # check parent property
        obj1 = ExampleParentObject()
        self.assertEquals(len(obj1.x), 0)

        # check default inherited property
        obj1.x.append(expected_result2)

        obj2 = ExampleChildObject()
        self.assertEquals(len(obj2.x), 1)

        # change inherited property
        obj2.x.append(expected_result1)
        self.assertEquals(obj2.x[1], expected_result1)

        # verify that parent class properties were NOT changed
        self.assertEquals(obj1.x[0], expected_result2)

    # test Class().__init__
    def testInheritedConstructors(self):
        expected_result1 = "test"
        expected_result2 = "parent"
        expected_result3 = "grandparent"
        expected_result4 = "older"

        # verify that parent.__init__ is called if there is no child.__init__()
        obj1 = ExampleChildNoConstructor()
        self.assertEquals(obj1.x, expected_result1, "ExampleParentConstructor.__init__() was NOT called for ExampleChildNoConstructor")

        # verify that parent.__init__ is NOT called (child.__init__() is defined)
        obj2 = ExampleChildConstructor()
        self.assertNotEqual(getattr(obj2, "x", None), expected_result1, "ExampleParentConstructor.__init__() was called for ExampleChildConstructor")

        # verify that parent.__init__ is explicitly called
        obj3 = ExampleChildExplicitConstructor()
        self.assertEquals(obj3.x, expected_result1, "ExampleParentConstructor.__init__() was NOT called for ExampleChildExplicitConstructor")

        # verify inherited values
        self.assertEquals(obj1.y, expected_result2, "Did not inherit property from parent")
        self.assertEquals(obj2.y, expected_result2, "Did not inherit property from parent")
        self.assertEquals(obj1.z, expected_result3, "Did not inherit property from grandparent")
        self.assertEquals(obj2.z, expected_result3, "Did not inherit property from grandparent")

        res = getattr(obj1, "r", None)
        self.assertNotEqual(res, expected_result4, "ExampleGrandParentConstructor.__init__() was called (%s)" % res)
        self.assertNotEqual(getattr(obj2, "r", None), expected_result4, "ExampleGrandParentConstructor.__init__() was called")

        # check inherited class vars (from parent)
        self.assertEqual(ExampleChildConstructor.y, expected_result2, "Did not inherit class var from parent")
        self.assertEqual(ExampleChildNoConstructor.y, expected_result2, "Did not inherit class var from parent")
        self.assertEqual(ExampleChildExplicitConstructor.y, expected_result2, "Did not inherit class var from parent")

        # check inherited class vars (from grandparent)
        self.assertEqual(ExampleChildConstructor.z, expected_result3, "Did not inherit class var from grandparent")
        self.assertEqual(ExampleChildNoConstructor.z, expected_result3, "Did not inherit class var from grandparent")
        self.assertEqual(ExampleChildExplicitConstructor.z, expected_result3, "Did not inherit class var from grandparent")

    def testClassMethods(self):
        results = ExampleClass.sampleClassMethod("a")
        self.assertEqual(results[0], ExampleClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1], "a")

        results = ExampleParentClass.sampleClassMethod("a")
        self.assertEqual(results[0], ExampleParentClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1], "a")

        results = ExampleChildClass.sampleClassMethod("a")
        self.assertEqual(results[0], ExampleChildClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1], "a")

        results = ExampleClass.sampleClassMethodVarargs("a", "b", "c")
        self.assertEqual(results[0], ExampleClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1][0], "a")
        self.assertEqual(results[1][1], "b")
        self.assertEqual(results[1][2], "c")

        results = ExampleClass.sampleClassMethodKwargs(c=9, b=8, a=7)
        self.assertEqual(results[0], ExampleClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1], 7)
        self.assertEqual(results[2], 8)
        self.assertEqual(results[3], 9)

        #
        # Repeat the test using class instances; the effect should be the same
        #

        results = ExampleClass().sampleClassMethod("a")
        self.assertEqual(results[0], ExampleClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1], "a")

        results = ExampleParentClass().sampleClassMethod("a")
        self.assertEqual(results[0], ExampleParentClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1], "a")

        results = ExampleChildClass().sampleClassMethod("a")
        self.assertEqual(results[0], ExampleChildClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1], "a")

        results = ExampleClass().sampleClassMethodVarargs("a", "b", "c")
        self.assertEqual(results[0], ExampleClass, "Expected first parameter to be the class instance")
        self.assertEqual(results[1][0], "a")
        self.assertEqual(results[1][1], "b")
        self.assertEqual(results[1][2], "c")

    def testStaticMethod(self):
        self.assertEqual(ExampleClass.sampleStaticMethod("a"), "a", "Expected static method to take the parameter I give as its first parameter")

    #def testClassDefinitionOrder(self):
    #    x = ExampleSubclassDefinedBeforeSuperclass()
    #    self.assertEqual(x.someMethod(), "abc", "Expected someMethod to return 'abc'")

    def testIsInstance(self):
        c = ExampleChildClass()
        self.failIf(isinstance(c, ExampleClass))
        self.failUnless(isinstance(c, ExampleChildClass))
        self.failUnless(isinstance(c, ExampleParentClass))

    def testIsInstanceNested(self):
        c = ExampleChildClass()
        self.failUnless(isinstance(c, (ExampleClass, ExampleChildClass)))
        self.failIf(isinstance(c, (ExampleClass, ExampleParentObject)))
        self.failUnless(isinstance(c, (ExampleClass, (ExampleChildClass,))))

    def testMetaClass(self):
        Klass = type('MyClass', (object,), {'method': method, 'x': 5})
        instance = Klass()
        self.assertEqual(instance.method(), 1)
        self.assertEqual(instance.x, 5)

# testMetaClass
def method(self):
    return 1

# testClassVars
class ExampleClass:
    x = "test"

    @classmethod
    def sampleClassMethod(cls, arg):
        return cls, arg

    @classmethod
    def sampleClassMethodVarargs(cls, *args):
        return cls, args

    @classmethod
    def sampleClassMethodKwargs(cls, a=0, b=1, c=2):
        return cls, a, b, c

    @staticmethod
    def sampleStaticMethod(arg):
        return arg

# testInheritedProperties
class ExampleParentClass:
    x = "test"

    @classmethod
    def sampleClassMethod(cls, arg):
        return cls, arg

class ExampleChildClass(ExampleParentClass):
    pass


# testInheritedPropertyObjects
class ExampleParentObject:
    x = []

class ExampleChildObject(ExampleParentObject):
    pass


# testInheritedConstructors
class ExampleGrandParentConstructor:
    z = "grandparent"

    def __init__(self):
        self.r = "older"

    def older(self):
        self.w = 2

class ExampleParentConstructor(ExampleGrandParentConstructor):
    y = "parent"

    def __init__(self):
        self.x = "test"

    def dosomething(self):
        self.m = 1

class ExampleChildConstructor(ExampleParentConstructor):
    def __init__(self):
        pass

class ExampleChildNoConstructor(ExampleParentConstructor):
    pass

class ExampleChildExplicitConstructor(ExampleParentConstructor):
    def __init__(self):
        ExampleParentConstructor.__init__(self)

# XXX doing this should throw a "Name" exception
#
#class ExampleSubclassDefinedBeforeSuperclass(ExampleSuperclassDefinedAfterSubclass):
#    pass

#class ExampleSuperclassDefinedAfterSubclass:
#    def someMethod(self):
#        return 'abc'



