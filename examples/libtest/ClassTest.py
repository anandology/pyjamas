import sys
from UnitTest import UnitTest, IN_BROWSER

# syntax check
# import a, b, c
if True:
    import imports.circ1
from imports import exec_order, imports as IMPORTS
from imports import exec_order as EXEC_ORDER
import I18N

from imports.classes import WithAttribute

import imports.decors # must be in this form

global names
names = {}

class SubAssignBase(object):
    names['SubAssign'] = 'SubAssign'
    def __init__(self):
        pass

class SubAssign(SubAssignBase):
    def __init__(self):
        SubAssignBase.__init__(self)
    names['SubAssignBase'] = 'SubAssignBase'

class GetAttribute():
    # This class definition fails at startup
    getIt = WithAttribute.ATTR

class Sink:
    def __init__(self):
        self.sink = "Sink"
    
class SinkInfo:
    def __init__(self, object_type):
        self.object_type=object_type
        self.instance=None

    def createInstance(self):
        return self.object_type()

    def getInstance(self):
        if self.instance==None:
            self.instance=self.createInstance()
        return self.instance
    
class Trees(Sink):
    def __init__(self):
        Sink.__init__(self)
        self.test = "Trees"

class TestClass1Bug339(object):
    def __init__(self):
        self.test = TestClass2()
        # The following method call causes the problem:
        self.test.test_method(test_arg=0)
        # The problem happens when a method is called with keyword
        # arguments on an object that is referenced as an attribute of
        # another object. In other words, this method could be called
        # in either of the following ways with no problem:
        test = TestClass2()
        test.test_method(test_arg=0)
        # or
        self.test = TestClass2()
        self.test.test_method(0)

class TestClass2(object):
    def test_method(self, test_arg):
        # Because of the way this method is called, self will be undefined
        # and the following line will cause an exception
        self.value = 0

class UserListPanel():
   def setUsers(self, title, screennames=None):
       pass

class TestClassBug342(object):
   def __init__(self):
       self.u = UserListPanel()
       self.u.setUsers('title', screennames=33)


class ClassTest(UnitTest):

    def testInstancePassing(self):
        s = SinkInfo(Trees)
        i = s.getInstance()
        self.assertEquals(i.test, "Trees")
        self.assertEquals(i.sink, "Sink")

    def testBug342(self):
        try:
            t = TestClassBug342()
        except:
            self.fail("Bug #342 encountered")
        finally:
            self.assertTrue(True)

    def testBug339(self):
        try:
            TestClass1Bug339()
        except:
            self.fail("Bug #339 encountered")
        finally:
            self.assertTrue(True)

    def testSubAssign(self):
        self.assertEquals(names['SubAssignBase'], 'SubAssignBase')
        self.assertEquals(names['SubAssign'], 'SubAssign')

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
        # Test is enabled, to remind us of the differences with CPython
        try:
            ExampleClass().fail_a()
            self.fail("Failed to raise error on ExampleClass().fail_a() bug #217")
        except (NameError, AttributeError), e:
            self.assertTrue(True)
        except:
            self.fail("Failed to raise NameError or AttributeError on ExampleClass().fail_a()")

        # for we just make sure the result is undefined and not the value of
        # ExampleClass.a
        if IN_BROWSER:
            from __pyjamas__ import JS
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
        try:
            m = ExampleClass.oldIdiomStaticMethod("middle")
            self.assertEqual(m,"beforemiddleafter")
        except TypeError:
            self.fail("Issue 415 - Old idiom for static methods improperly checks first argument type")

    def test__new__Method(self):
        c = OtherClass1()
        self.assertEqual(c.__class__.__name__, 'ObjectClass')
        self.assertEqual(c.prop, 1)
        c = OtherSubclass1()
        self.assertEqual(c.__class__.__name__, 'ObjectClass', "Issue 414: __new__ method on superclass not called")
        c = OtherClass2()
        self.assertEqual(c.__class__.__name__, 'OtherClass2')
        try:
            prop = c.prop
            self.fail("failed to raise an error on c.prop (improperly follows explicit __new__ with implicit __init__)")
        except:
            self.assertTrue(True)
        c = OtherClass3(41, 42)
        self.assertEqual(c.y if hasattr(c,"y") else 0, 42, "Issue 417: __new__ method not passed constructor arguments.")

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
    
    def testIsSubclass(self):
        class A: pass
        class B(A): pass
        class C(B): pass
        class D: pass
        class E(D, C): pass
        
        self.assertTrue(issubclass(A, A))
        self.assertTrue(issubclass(C, A))
        self.assertTrue(issubclass(E, A))
        self.assertTrue(issubclass(E, (PassMeAClass, A)))
        self.assertFalse(issubclass(A, PassMeAClass))
        
        self.assertRaises(TypeError, issubclass, PassMeAClass(), PassMeAClass)
        self.assertRaises(TypeError, issubclass, PassMeAClass, PassMeAClass())
        self.assertRaises(TypeError, issubclass, None, PassMeAClass)
    
    def testMetaClass(self):
        Klass = type('MyClass', (object,), {'method': method, 'x': 5})
        instance = Klass()
        self.assertEqual(instance.method(), 1)
        self.assertEqual(instance.x, 5)

    def testMetaClassInheritFromType(self):
        class Metaklass(type):
            def metamethod(cls):
                return 2
        class Klass(object):
            __metaclass__ = Metaklass
            def method(cls):
                return 1
            x = 5
        try:
            self.assertEqual(Klass.metamethod(), 2)
            instance = Klass()
            self.assertEqual(instance.method(), 1)
            self.assertEqual(instance.x, 5)
        except:
            self.fail('bug #298 - missing metaclass features')

    def testMetaClassDct(self):
        class MetaklassDctSaver(type):
            def __init__(cls, name, bases, dct):
                super(MetaklassDctSaver, cls).__init__(name, bases, dct)
                cls.saved_dct = dct
        class MyClass(object):
            __metaclass__ = MetaklassDctSaver
            a = 1
            b = 2
        try:
            self.assertTrue(isinstance(MyClass.saved_dct, dict))
            self.assertTrue("a" in MyClass.saved_dct)
            self.assertTrue("b" in MyClass.saved_dct)
        except:
            self.fail('bug #298 - missing metaclass features')

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
        except:
            self.fail("failed to raise Attribute error for instance.z")

    def testSuperArgTest(self):
        a2 = SuperArg2(a=1,b=2,c=3)
        a3 = SuperArg3(a=1,b=2,c=3)
        self.assertEqual(["SuperArg2",a2.a1_args], ['SuperArg2', [('a', 1), ('b', 2), ('c', 3)]])
        self.assertEqual(["SuperArg3",a3.a1_args], ['SuperArg3', [('a', 1), ('b', 2), ('c', 3)]])

    def testImportTest(self):
        import imports
        self.assertEqual(imports.exec_order[0], 'circ1-1')
        self.assertEqual(exec_order[1], 'circ2-1')
        self.assertEqual(EXEC_ORDER[2], 'circ2-2')
        self.assertEqual(imports.exec_order[3], 'circ1-2')
        self.assertEqual(imports.exec_order[3], IMPORTS.exec_order[3])

        import imports.child
        teststring = 'import test'
        try:
            c = imports.child.Child()
            self.assertEqual(c.value(teststring), teststring)
        except AttributeError, e:
            self.fail(e.message)

        class C(imports.child.Child): pass
        c = C()
        self.assertEqual(c.value(teststring), teststring)

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
        self.assertEqual(pmc.foo(), "foo in PassMeAClass", "foo !in PassMeAClass")

        try:
            pmc = ggetObject("mscp1", 5) 
        except:
            self.assertEqual(False, True, "Exception indicates bug in compiler: 'Error: uncaught exception: ExampleMultiSuperclassParent1() arguments after ** must be a dictionary 5'")
        else:
            self.assertEqual(pmc.x, 5, "pass me class x != 5")
        try:
            pmc = ggetObject("exchild", 5, 7) # 5 is ignored
        except:
            self.assertEqual(False, True, "Exception indicates bug in compiler: 'Error: uncaught exception: ExampleChildClass() arguments after ** must be a dictionary 7'")
        else:
            self.assertEqual(pmc.prop_a, 1, "pass me class prop_a != 1")
            self.assertEqual(pmc.prop_b, 7, "pass me class prop_b != 7")

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

    def testImportKeywords(self):
        import imports.enum.super
        self.assertEqual(imports.enum.super.var, 1)
        self.assertEqual(imports.enum.super.function(), 2)

        from imports import enumerate
        self.assertEqual(enumerate.list, 1)

        from imports.enumerate import dict
        self.assertEqual(dict(), (1,2))

    def testDescriptors(self):
        global revealAccessLog
        decorated = Decorated()
        revealAccessLog = None

        self.assertEqual(decorated.x, 10)
        self.assertEqual(revealAccessLog, "Retrieving var 'x'")

        decorated.x = 5
        self.assertEqual(revealAccessLog, "Updating var 'x': 5")
        self.assertEqual(decorated.x, 5)

        del decorated.x
        self.assertEqual(revealAccessLog, "Deleting var 'x'")
        try:
            x = decorated.x
            self.fail("Failed to raise error for 'del decorated.x'")
        except AttributeError, e:
            self.assertTrue(True)
            #self.assertEqual(e[0], "'RevealAccess' object has no attribute 'val'")
        except:
            self.fail("Failed to raise Attribute error for 'del decorated.x'")

    def testProperty(self):
        p = OldStylePropertyDecorating()

        p.x = 1
        self.assertEqual(p._x, 1)
        self.assertEqual(p.x, 1)
        del p.x
        try:
            x = p._x
            self.fail("Failed to raise error for 'x = p._x'")
        except AttributeError, e:
            self.assertTrue(True)
        except:
            self.fail("Failed to raise Attribute error for 'x = p._x'")

        p = NewStylePropertyDecorating()

        p.x = 1
        self.assertEqual(p._x, 1)
        self.assertEqual(p.x, 1)
        del p.x
        try:
            x = p._x
            self.fail("Failed to raise error for 'x = p._x'")
        except AttributeError, e:
            self.assertTrue(True)
        except:
            self.fail("Failed to raise Attribute error for 'x = p._x'")

    def testDynamicLoading(self):
        self.assertEqual(I18N.i18n.example(),
                         'This is an example')
        self.assertEqual(I18N.domain.i18n.example(),
                         'This is a domain example')
        self.assertEqual(I18N.domain.subdomain.i18n.example(),
                         'This is a subdomain example')
        self.assertEqual(I18N.i18n.another_example(),
                         'This is another example')
        self.assertEqual(I18N.domain.i18n.another_example(),
                         'This is another example')
        I18N.set_locale('en_US')
        self.assertEqual(I18N.i18n.example(),
                         'This is an en_US example')
        self.assertEqual(I18N.domain.i18n.example(),
                         'This is a domain en_US example')
        self.assertEqual(I18N.domain.subdomain.i18n.example(),
                         'This is a subdomain en_US example')
        self.assertEqual(I18N.i18n.another_example(),
                         'This is en_US another example')
        self.assertEqual(I18N.domain.i18n.another_example(),
                         'This is en_US another example')

    def testClassesAnywhere(self):
        class A(object):
            def __init__(self, what):
                if not what:
                    class B(object):
                        def __init__(self):
                            self.v = 0
                else:
                    class B(object):
                        def __init__(self):
                            self.v = 1
                self.b = B()
 
        a = A(0)
        self.assertEqual(a.b.v, 0)
        a = A(1)
        self.assertEqual(a.b.v, 1)

    def testClassDefinitionCode(self):
        class A(object):
            def __init__(self, what):
                class B(object):
                    if not what:
                        def __init__(self):
                            self.v = 0
                    else:
                        def __init__(self):
                            self.v = 1
                self.b = B()

        a = A(0)
        self.assertEqual(a.b.v, 0)
        a = A(1)
        self.assertEqual(a.b.v, 1)

        class A(object):
            l = [1,2,3]
            l[1] = 22
            d = {}
            d['a'] = 1
            l1 = []
            l2 = []
            for i in range(4):
                l1.append(i)
            i = 0
            while i < 4:
                l2.append(i)
                i += 1

        a = A()
        v = [1,22,3]
        self.assertTrue(a.l == v, "%r == %r" % (a.l, v))
        v = {'a': 1}
        self.assertTrue(a.d == v, "%r == %r" % (a.d, v))
        v = [0,1,2,3]
        self.assertTrue(a.l1 == v, "%r == %r" % (a.l1, v))
        self.assertTrue(a.l2 == v, "%r == %r" % (a.l2, v))

    def testGenericMethodDecorators(self):
        """
        issues #309, #318
        """
        obj = DecoratedMethods()
        self.assertEqual(obj.mtd1("b"), "1b2")
        self.assertEqual(obj.mtd2("b"), "31b24")
        self.assertEqual(obj.mtd3("b"), "abc")
        self.assertEqual(obj.mtd4("b"), "a3b4c")

        exc_raised = False
        try:
            res = obj.mtd5("b")
        except TypeError, t:
            exc_raised = True
        self.assertTrue(exc_raised, "TypeError wrong arguments count not raised")

        self.assertEqual(obj.mtd_static("b"), "5b6")
        self.assertEqual(DecoratedMethods.mtd_static(*["b"], **{}), "5b6")
        self.assertEqual(obj.mtd_static2("b"), "55b66")
        self.assertEqual(DecoratedMethods.mtd_static("b"), "5b6")
        self.assertEqual(DecoratedMethods.mtd_static2("b"), "55b66")

        try:
            self.assertEqual(obj.mtd_class("b"), "7b8")
            self.assertEqual(obj.mtd_class2("b"), "77b88")
            self.assertEqual(DecoratedMethods.mtd_class("b"), "7b8")
            self.assertEqual(DecoratedMethods.mtd_class2("b"), "77b88")
        except TypeError, e:
            msg = str(e)
            if "fnc() takes exactly 2 arguments (1 given)" in msg:
                msg = "bug #318 - " + msg
            self.fail(msg)

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
    
    def shouldntWork(arg):
        return "before" + arg + "after"
        
    oldIdiomStaticMethod = staticmethod(shouldntWork)

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
        
class OtherSubclass1(OtherClass1):
    pass

class OtherClass2(object):
    def __new__(cls):
        return ObjectClass.__new__(cls)
        
class OtherClass3(object):
    def __new__(cls, x, y):
        val = object.__new__(cls)
        val.x, val.y = x,y
        return val

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

revealAccessLog = None
class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
    def __get__(self, obj, objtype=None):
        global revealAccessLog
        revealAccessLog = 'Retrieving %s' % self.name
        return self.val
    def __set__(self, obj, val):
        global revealAccessLog
        revealAccessLog = 'Updating %s: %s' % (self.name, val)
        self.val = val
    def __delete__(self, obj):
        global revealAccessLog
        revealAccessLog = 'Deleting %s' % self.name
        del self.val

class Decorated(object):
    x = RevealAccess(10, "var 'x'")

class OldStylePropertyDecorating(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

# Property class that gives python 2.5 a setter and a deleter
class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if not doc is None or not hasattr(fget, '__doc__') :
            self.__doc__ = doc
        else:
            self.__doc__ = fget.__doc__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError, "unreadable attribute"
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError, "can't set attribute"
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError, "can't delete attribute"
        self.fdel(obj)

    def setter(self, fset):
        self.fset = fset
        return self

    def deleter(self, fdel):
        self.fdel = fdel
        return self

    def property_setter(self, fset):
        self.__setattr__('fset', fset)
        return self
    def property_deleter(self, fdel):
        self.__setattr__('fdel', fdel)
        return self

# Bug in pyjs that appears when the next lines are executed
# The 'property = Property' makes property a module variable, which is
# not set if the next line not is executed
property = property
if not hasattr(property, 'setter'):
    # Replace python 2.5 property class
    property = Property

class NewStylePropertyDecorating(object):
    def __init__(self):
        self._x = None
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

class SuperArg1(object) :
    def __init__(self,a=None,b=None,c=None) :
        self.a1_args = [('a', a),('b',b),('c',c)]

class SuperArg2(SuperArg1) :
    def __init__(self,a=None,b=None,c=None) :
        self.a2_args = [('a', a),('b',b),('c',c)]
        super(SuperArg2,self).__init__(a=a,b=b,c=c)

class SuperArg3(SuperArg1) :
    def __init__(self,a=None,b=None,c=None) :
        self.a3_args = [('a', a),('b',b),('c',c)]
        super(SuperArg3,self).__init__(a,b,c)

############################################################################
# generic decoerators for methods
############################################################################

def mdeco1(f):
    def fn1(self, x):
        if not isinstance(self, DecoratedMethods):
            raise TypeError("fn1 - self is not instance of DecoratedMethods")
        return "1" + f(self, x) + "2"
    return fn1

def mdeco2(f):
    def fn2(self, x):
        if not isinstance(self, DecoratedMethods):
            raise TypeError("fn2 - self is not instance of DecoratedMethods")
        return "3" + f(self, x) + "4"
    return fn2

def mdeco_with_wrong_args(f):
    def fn_wwa(x): # correct definition should be fn(self, x), this must raise an exc
        return "5" + f(x) + "6"
    return fn_wwa

def mdeco_static(f):
    def fns(x):
        return "5" + f(x) + "6"
    return fns

def mdeco_class(f):
    def fnc(cls, x):
        if cls is not DecoratedMethods:
            raise TypeError("fnc - cls is not DecoratedMethods")
        return "7" + f(cls, x) + "8"
    return fnc

class DecoratedMethods(object):
    @mdeco1
    def mtd1(self, x):
        return x

    @mdeco2
    @mdeco1
    def mtd2(self, x):
        return x

    @imports.decors.othermoduledeco1
    def mtd3(self, x):
        return x

    @imports.decors.othermoduledeco1
    @mdeco2
    def mtd4(self, x):
        return x

    @mdeco_with_wrong_args
    def mtd5(self, x):
        return x

    @staticmethod
    @mdeco_static
    def mtd_static(x):
        return x

    @staticmethod
    @mdeco_static
    @mdeco_static
    def mtd_static2(x):
        return x

    @classmethod
    @mdeco_class
    def mtd_class(cls, x):
        return x

    @classmethod
    @mdeco_class
    @mdeco_class
    def mtd_class2(cls, x):
        return x

