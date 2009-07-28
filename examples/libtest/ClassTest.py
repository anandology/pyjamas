import sys
from UnitTest import UnitTest, IN_BROWSER

# syntax check
# import a, b, c
if True:
    import imports.child, imports.circ1
from imports import exec_order
from imports import exec_order as EXEC_ORDER


from imports.classes import WithAttribute


class GetAttribute():
    # This class definition fails at startup
    getIt = WithAttribute.ATTR


class ClassTest(UnitTest):

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

        # verify that the initiation of ExampleClass.c is correct
        self.assertEquals(ExampleClass.c, 1|2)

        # verify that class properties can only be reached via instance
        #
        # this test no longer fails as expected because the compiler now
        # correctly assumes that a used in fail_a is on module level.
        # This has the consequence that a is undefined in javascript. This
        # could be solved by adding a lot of code.
        #try:
        #    ExampleClass().fail_a()
        #    self.fail("Failed to raise error on ExampleClass().fail_a()")
        #except (NameError, AttributeError), e:
        #    self.assertTrue(True)
        #except:
        #    self.fail("Failed to raise NameError or AttributeError on ExampleClass().fail_a()")

        # for we just make sure the result is undefined and not the value of
        # ExampleClass.a
        if IN_BROWSER:
            x = ExampleClass().fail_a()
            self.assertTrue(JS('pyjslib.isUndefined(x)'))

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

        obj = ExampleChildClass(b = 222)
        self.assertEquals(obj.prop_a, 1)
        self.assertEquals(obj.prop_b, 222)

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

        # Test argument passing
        self.assertEqual(ExampleParentClass().inert('inert'), 'inert')
        self.assertEqual(ExampleParentClass().global_x1(), 'global test')
        self.assertEqual(ExampleParentClass().global_x2(), 'global test')

        # Test reqursive class definition
        instance = RecurseMe()
        self.assertEqual(instance.chain[0], 0)
        self.assertEqual(instance.chain[1], 1)

    def testStaticMethod(self):
        self.assertEqual(ExampleClass.sampleStaticMethod("a"), "a", "Expected static method to take the parameter I give as its first parameter")

    def test__new__Method(self):
        c = OtherClass1()
        self.assertEqual(c.__class__.__name__, 'ObjectClass')
        self.assertEqual(c.prop, 1)
        c = OtherClass2()
        self.assertEqual(c.__class__.__name__, 'OtherClass2')
        try:
            prop = c.prop
            self.fail("failed to raise an error on c.prop")
        except:
            self.assertTrue(True)

        instance = MultiBase.__new__(MultiInherit1)
        self.assertEqual(instance.name, 'MultiInherit1')
        instance = MultiInherit1.__new__(MultiBase)
        self.assertEqual(instance.name, 'MultiBase')
        instance = object.__new__(MultiInherit1, **{})
        self.assertEqual(instance.name, 'MultiInherit1')

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

    def testInstanceChecking(self):
        try:
            ExampleChildClass.get_x(ExampleChildClass())
            self.assertTrue(True)
        except TypeError, e:
            self.fail(e)
        try:
            ExampleChildClass.get_x(ExampleClass())
            self.fail('Failed to raise error for invalid instance')
        except TypeError, e:
            self.assertTrue(e.args[0].find('get_x() must be called') >= 0, e.args[0])

    def testMetaClass(self):
        Klass = type('MyClass', (object,), {'method': method, 'x': 5})
        instance = Klass()
        self.assertEqual(instance.method(), 1)
        self.assertEqual(instance.x, 5)

    def testMultiSuperclass(self):
        new_value = 'New value'
        c = ExampleMultiSuperclassNoConstructor(new_value)
        # Verify that the __init__ of ExampleMultiSuperclassParent1 is used
        self.assertEqual(c.x, new_value)
        # Verify that the ExampleMultiSuperclassParent2.y is there
        self.assertEqual(c.y, ExampleMultiSuperclassParent2.y)
        # Verify that the get_value() of ExampleMultiSuperclassParent1 is used
        self.assertEqual(c.get_value(), new_value)

        c = ExampleMultiSuperclassExplicitConstructor(new_value)
        # Verify that the ExampleMultiSuperclassParent1.x is there
        self.assertEqual(c.x, ExampleMultiSuperclassParent1.x)
        # Verify that the ExampleMultiSuperclassParent2.y is there
        self.assertEqual(c.y, ExampleMultiSuperclassParent2.y)
        # Verify that the __init__ of ExampleMultiSuperclassExplicitConstructor is used
        self.assertEqual(c.z, new_value)
        # Verify that the get_value() of ExampleMultiSuperclassExplicitConstructor is used
        self.assertEqual(c.get_value(), new_value)
        # Verify that the combination of the variables is correct
        self.assertEqual(c.get_values(), ':'.join([ExampleMultiSuperclassParent1.x, ExampleMultiSuperclassParent2.y, new_value]))

    def testMultiDoubleInherit(self):
        i = DoubleInherit(1,2,3)
        self.assertEqual(i.get_x(), 1)
        self.assertEqual(i.get_y(), 2)
        self.assertEqual(i.get_z(), 3)

        MultiInherit2.set_x(i, 5)
        self.assertEqual(MultiInherit1.get_x(i), 5)

    def testClassArguments(self):
        c = ClassArguments()
        try:
            # FIXME: This should raise:
            # TypeError: no_args() takes no arguments (1 given)
            c.no_args()
            self.fail("Exception should be raised on 'c.no_args()'")
        except TypeError, e:
            self.assertEqual(e.args[0], "no_args() takes no arguments (1 given)")

        self.assertEqual(c.self_arg(), True)
        self.assertEqual(c.two_args(1), 1)
        try:
            # FIXME: This should raise:
            # 'TypeError: two_args() takes exactly 2 arguments (1 given)
            c.two_args()
            self.fail("Exception should be raised on 'c.two_args()'")
        except TypeError, e:
            self.assertEqual(e.args[0], "two_args() takes exactly 2 arguments (1 given)")

    def testSuperTest(self):
        c = DoubleInherit(1,2,3)
        self.assertEqual(super(DoubleInherit, c).get_y(), 2)
        c.y = 4
        self.assertEqual(super(DoubleInherit, c).get_y(), 4)

        instance = super(MultiBase, MultiInherit1).__new__(MultiInherit1)
        self.assertEqual(instance.name, 'MultiInherit1')
        instance = super(MultiBase, MultiInherit1).__new__(MultiBase)
        self.assertEqual(instance.name, 'MultiBase')

        instance = super(MultiBase, MultiInherit1).__new__(MultiInherit1)
        instance.__init__(1,2)
        self.assertEqual(instance.x, 1)
        self.assertEqual(instance.y, 2)
        try:
            z = instance.z
            self.fail("failed to raise error for instance.z")
        except AttributeError, e:
            self.assertTrue(True)

    def testImportTest(self):
        self.assertEqual(imports.exec_order[0], 'circ1-1')
        self.assertEqual(exec_order[1], 'circ2-1')
        self.assertEqual(EXEC_ORDER[2], 'circ2-2')
        self.assertEqual(imports.exec_order[3], 'circ1-2')

        # import imports.child # FIXME: if the import statement is here in stead of at the top, this fails on compiling
        teststring = 'import test'
        try:
            c = imports.child.Child()
            self.assertEqual(c.value(teststring), teststring)
        except AttributeError, e:
            self.fail(e.message)

    def testPassMeAClass(self):
        res = PassMeAClassFunction(PassMeAClass)
        self.assertEqual(res, "foo in PassMeAClass")

    def testClassAttributeAccess(self):
        self.assertEqual(GetAttribute.getIt, WithAttribute.ATTR)

    def testNameMapping(self):
        instance = MultiBase('a')
        r = instance.prototype(1, 2, 3)
        self.assertEqual(r[0], 'MultiBase')
        self.assertEqual(r[1], 1)
        self.assertEqual(r[2], 2)
        self.assertEqual(r[3], 3)

        instance = MultiInherit1('a', 'b')
        r = instance.call(1, 2, 3)
        self.assertEqual(r[0], 'MultiInherit1')
        self.assertEqual(r[1], 1)
        self.assertEqual(r[2], 2)
        self.assertEqual(r[3], 3)

    def testGlobalClassFactory(self):

        gregister("passme", PassMeAClass)
        gregister("exchild", ExampleChildClass)
        gregister("mscp1", ExampleMultiSuperclassParent1)

        pmc = ggetObject("passme")
        self.assertEqual(pmc.foo(), "foo in PassMeAClass")

        try:
            pmc = ggetObject("mscp1", 5) 
        except:
            self.assertEqual(False, True, "Exception indicates bug in compiler: 'Error: uncaught exception: ExampleMultiSuperclassParent1() arguments after ** must be a dictionary 5'")
        else:
            self.assertEqual(pmc.x, 5)
        try:
            pmc = ggetObject("exchild", 5, 7) # 5 is ignored
        except:
            self.assertEqual(False, True, "Exception indicates bug in compiler: 'Error: uncaught exception: ExampleChildClass() arguments after ** must be a dictionary 7'")
        else:
            self.assertEqual(pmc.prop_a, 1)
            self.assertEqual(pmc.prop_b, 7)

    def testClassFactory(self):

        f = Factory()
        f.register("passme", PassMeAClass)
        f.register("exchild", ExampleChildClass)

        try:
            pmc = f.getObjectCompilerBug("passme")
        except:
            self.assertEqual(False, True, "Compiler bug in class factory test")
        else:
            self.assertEqual(pmc.foo(), "foo in PassMeAClass")

        pmc = f.getObject("passme")
        self.assertEqual(pmc.foo(), "foo in PassMeAClass")

        try:
            pmc = f.getObject("exchild", 5, 7) # 5 is ignored
        except:
            self.assertEqual(False, True, "Exception indicates bug in compiler: 'Error: uncaught exception: ExampleChildClass() arguments after ** must be a dictionary 7'")
        else:
            self.assertEqual(pmc.prop_a, 1)
            self.assertEqual(pmc.prop_b, 7)

    def testClassFactory(self):

        f = Factory()
        f.register("passme", PassMeAClass)
        f.register("exchild", ExampleChildClass)

        try:
            pmc = f.getObjectCompilerBug("passme")
        except:
            self.assertEqual(False, True, "Compiler bug in class factory test")
        else:
            self.assertEqual(pmc.foo(), "foo in PassMeAClass")

        pmc = f.getObject("passme")
        self.assertEqual(pmc.foo(), "foo in PassMeAClass")

        try:
            pmc = f.getObject("exchild", 5, 7) # 5 is ignored
        except:
            self.assertEqual(False, True, "Exception indicates bug in compiler: 'Error: uncaught exception: ExampleChildClass() arguments after ** must be a dictionary 7'")
        else:
            self.assertEqual(pmc.prop_a, 1)
            self.assertEqual(pmc.prop_b, 7)

class PassMeAClass(object):
    def __init__(self):
        pass
    def foo(self):
        return "foo in PassMeAClass"

def PassMeAClassFunction(klass):
    c = klass()
    return c.foo() 

# testMetaClass
def method(self):
    return 1


# testClassVars
class ExampleClass:
    x = "test"
    a = 1
    b = 2
    c = a|b

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

    def fail_a(self):
        return a

# Global variable to test variable selection order
x = 'global test'
# testInheritedProperties
class ExampleParentClass:
    x = "test"

    def __init__(self, a=1, b=2):
        self.prop_a = a
        self.prop_b = b

    @classmethod
    def sampleClassMethod(cls, arg):
        return cls, arg

    def get_x(self):
        return self.x

    def inert(self, x):
        return x

    def global_x1(self):
        return x

    def global_x2(self):
        return x

class ExampleChildClass(ExampleParentClass):
    def __init__(self, a = 11, b = 22):
        ExampleParentClass.__init__(self, b = b)

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

class ObjectClass(object):
    def __init__(self):
        self.prop = 1

class OtherClass1(object):
    def __new__(cls):
        return ObjectClass()

class OtherClass2(object):
    def __new__(cls):
        return ObjectClass.__new__(cls)

class ExampleMultiSuperclassParent1:
    x = 'Initial X'

    def __init__(self, x):
        self.x = x
    def get_value(self):
        return self.x

class ExampleMultiSuperclassParent2:
    y = 'Initial Y'

    def __init__(self, y):
        self.y = y
    def get_value(self):
        return self.y

class ExampleMultiSuperclassNoConstructor(ExampleMultiSuperclassParent1, ExampleMultiSuperclassParent2):
    z = 'Initial Z'

class ExampleMultiSuperclassExplicitConstructor(ExampleMultiSuperclassParent1, ExampleMultiSuperclassParent2):
    z = 'Initial Z'

    def __init__(self, z):
        self.z = z
    def get_value(self):
        return self.z
    def get_values(self):
        return ':'.join([self.x, self.y, self.z])

class ClassArguments:
    def no_args( ):
        return False
    def self_arg(self):
        return True
    def two_args(self, arg1):
        return arg1

class MultiBase(object):
    name = 'MultiBase'
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_x(self,x ):
        self.x = x

    def prototype(self, default, arguments, this):
        return (self.name, default, arguments, this)

class MultiInherit1(MultiBase):
    name = 'MultiInherit1'
    def __init__(self, x, y):
        self.y = y
        MultiBase.__init__(self, x) # yes it gets called twice

    def get_y(self):
        return self.y

    def call(self, default, arguments, this):
        return self.prototype(default, arguments, this)

class MultiInherit2(MultiBase):
    name = 'MultiInherit2'
    def __init__(self, x, z):
        self.z = z
        MultiBase.__init__(self, x) # yes it gets called twice

    def get_z(self):
        return self.z

class DoubleInherit(MultiInherit1, MultiInherit2):
    name = 'DoubleInherit'
    def __init__(self, x, y, z):
        MultiInherit1.__init__(self, x, y) # MultiBase __init__ called once
        MultiInherit2.__init__(self, x, z) # MultiBase __init__ called twice

class RecurseMe(object):
    chain = []
    def __init__(self):
        self.chain.append(0)

class RecurseMe(RecurseMe):
    def __init__(self):
        # Cannot do RecurseMe._init__(self), that would really call myself
        # And we can only do this once...
        super(self.__class__, self).__init__()
        self.chain.append(1)

class Factory:
    _classes = {}
    def __init__(self):
        pass
    def register(self, className, classe):
        Factory._classes[className] = classe

    def getObjectCompilerBug(self, className,*args, **kargs):
        return Factory._classes[className](*args, **kargs)

    def getObject(self, className,*args, **kargs):
        f = Factory._classes[className]
        return f(*args, **kargs)

global gclasses
gclasses = {}

def gregister(className, classe):
    gclasses[className] = classe
def ggetObject(className, *args, **kargs):
    classe = gclasses[className]
    return classe(*args, **kargs)

