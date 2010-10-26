from UnitTest import UnitTest

def aArgs(*args):
    return args

def ftest(a, b):
    return [a, b]

class ArgsTest(UnitTest):

    def testNaming1(self):
        values = ftest(1, 2)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)

    def testNaming2(self):
        values = ftest(a=1, b=2)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)

    def testNaming3(self):
        values = ftest(1, b=2)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)

    def testNaming4(self):
        exc_raised = False
        try:
            values = ftest(1, c=2)
        except TypeError, t:
            exc_raised = True
        self.assertTrue(exc_raised, "TypeError 'c' unexpected arg not raised")

    def testNaming5(self):
        exc_raised = False
        try:
            values = ftest()
        except TypeError, t:
            exc_raised = True
        self.assertTrue(exc_raised, "TypeError 'ftest() takes exactly 2 arguments (0 given)' not raised")

    def testSimpleCall(self):
        values = foo(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = foo2(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

    def testKeywordCall1(self):
        values = foo2(c=3, b=2, a=1)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
    def testKeywordCall2(self):
        values = foo2(b=2, a=1, c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
    def testKeywordCall3(self):
        values = foo2(1, c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], 3)

    def testKeywordCall4(self):
        values = foo2()
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], None)

    def testKeywordCall5(self):
        values = foo2(c=True)
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], True)
        
    def testStarArgs(self):
        args = (1,2)
        res = aArgs(*args)
        self.assertEquals(args, res)

        args = "123"
        try:
            res = aArgs(*args)
            called = True
            exc = None
        except TypeError, e:
            called = False
            exc = e

        # weird one: a string is a sequence, so it gets away with being
        # called on its own as *args! eeugh.
        self.assertTrue(called,
                    "exception not expected but function called:" + repr(res) + repr(exc))
        self.assertEquals(res, ("1", "2", "3"))


        args = 1
        try:
            res = aArgs(*args)
            called = True
        except TypeError:
            called = False

        self.assertFalse(called,
                    "exception expected but not raised - TypeError: aArgs() argument after * must be a sequence")


        args = (1,)
        res = aArgs(*args)
        self.assertEquals(args, res)

        args = (1,)
        res = aArgs(args)
        self.assertEquals((args,), res)

        
    def testDefaultValuesCall(self):
        values = foo3(b=7)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 7)
        self.assertEquals(values[2], 3)
        
        values = foo3(a=9)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = foo3()
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
    
    def testVarargsCall(self):
        values = foo4(9, 8, 7, 2, 3, 4)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 8)
        self.assertEquals(values[2], 7)
        self.assertEquals(values[3][0], 2)
        self.assertEquals(values[3][1], 3)
        self.assertEquals(values[3][2], 4)
        
        values = foo4(9, 8, 7, 3, 2, 1)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 8)
        self.assertEquals(values[2], 7)
        self.assertEquals(values[3][0], 3)
        self.assertEquals(values[3][1], 2)
        self.assertEquals(values[3][2], 1)
    
    def testKwargsCall(self):
        values = foo5(9, 8, 7, x=5, y=7)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 8)
        self.assertEquals(values[2], 7)
        self.assertEquals(values[3]["x"], 5)
        self.assertEquals(values[3]["y"], 7)

    def testComboCall(self):
        values = foo6(9, 8, 7, 1, 2, 3, x=4, y=5)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 8)
        self.assertEquals(values[2], 7)
        self.assertEquals(values[3][0], 1)
        self.assertEquals(values[3][1], 2)
        self.assertEquals(values[3][2], 3)
        self.assertEquals(values[4]["x"], 4)
        self.assertEquals(values[4]["y"], 5)

    def testEdgeCall(self):
        values = foo7(1,2,3,b=2)
        self.assertEqual(values[0], 1)
        self.assertEqual(values[1], (2,3))
        self.assertEqual(values[2], {'b':2})

        values = foo7(1, 2, 3, {'b':2})
        self.assertEqual(values[0], 1)
        self.assertEqual(values[1], (2,3,{'b':2}))
        self.assertEqual(values[2], {})

        vaules = foo8(1, b=2)
        self.assertEqual(vaules[0], 1)
        self.assertEqual(vaules[1], {'b':2})

        vaules = foo8({'b':2})
        self.assertEqual(vaules[0], {'b':2})
        self.assertEqual(vaules[1], {})

    def testSimpleCtorCall(self):
        values = ArgsTestClass_foo(1, 2, 3).x
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass_foo2(1, 2, 3).x
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

    def testKeywordCtorCall(self):
        values = ArgsTestClass_foo2(c=3, b=2, a=1).x
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass_foo2(b=2, a=1, c=3).x
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass_foo2().x
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], None)

        values = ArgsTestClass_foo2(c=True).x
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], True)
        
        
    def testDefaultValuesCtorCall(self):
        values = ArgsTestClass_foo3(b=7).x
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 7)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass_foo3(a=9).x
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass_foo3().x
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
    
    def testVarargsCtorCall(self):
        values = ArgsTestClass_foo4(9, 8, 7, 2, 3, 4).x
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 8)
        self.assertEquals(values[2], 7)
        self.assertEquals(values[3][0], 2)
        self.assertEquals(values[3][1], 3)
        self.assertEquals(values[3][2], 4)
        
        values = ArgsTestClass_foo4(9, 8, 7, 3, 2, 1).x
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 8)
        self.assertEquals(values[2], 7)
        self.assertEquals(values[3][0], 3)
        self.assertEquals(values[3][1], 2)
        self.assertEquals(values[3][2], 1)
    
    def testKwargsCtorCall(self):
        values = ArgsTestClass_foo5(9, 8, 7, x=5, y=7).x
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 8)
        self.assertEquals(values[2], 7)
        self.assertEquals(values[3]["x"], 5)
        self.assertEquals(values[3]["y"], 7)

    def testComboCtorCall(self):
        values = ArgsTestClass_foo6(9, 8, 7, 1, 2, 3, x=4, y=5).x
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 8)
        self.assertEquals(values[2], 7)
        self.assertEquals(values[3][0], 1)
        self.assertEquals(values[3][1], 2)
        self.assertEquals(values[3][2], 3)
        self.assertEquals(values[4]["x"], 4)
        self.assertEquals(values[4]["y"], 5)
        
    def testSimpleMethodCall(self):
        values = ArgsTestClass().foo(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass().foo2(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

    def testKeywordMethodCall(self):
        values = ArgsTestClass().foo2(c=3, b=2, a=1)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass().foo2(b=2, a=1, c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass().foo2()
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], None)

        values = ArgsTestClass().foo2(c=True)
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], True)
        
        
    def testDefaultValuesMethodCall(self):
        values = ArgsTestClass().foo3(b=7)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 7)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass().foo3(a=9)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass().foo3()
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
    
    def testVarargsMethodCall(self):
        values = ArgsTestClass().foo4(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass().foo4(3, 2, 1)
        self.assertEquals(values[0], 3)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 1)
    
    def testKwargsMethodCall(self):
        values = ArgsTestClass().foo5(x=5, y=7)
        self.assertEquals(values["x"], 5)
        self.assertEquals(values["y"], 7)

    def testComboMethodCall(self):
        values = ArgsTestClass().foo6(1, 2, 3, x=4, y=5)
        self.assertEquals(values[0][0], 1)
        self.assertEquals(values[0][1], 2)
        self.assertEquals(values[0][2], 3)
        self.assertEquals(values[1]["x"], 4)
        self.assertEquals(values[1]["y"], 5)
        
    def testEdgeMethodCall(self):
        values = ArgsTestClass().foo7(1,2,3,b=2)
        self.assertEqual(values[0], 1)
        self.assertEqual(values[1], (2,3))
        self.assertEqual(values[2], {'b':2})

        values = ArgsTestClass().foo7(1, 2, 3, {'b':2})
        self.assertEqual(values[0], 1)
        self.assertEqual(values[1], (2,3,{'b':2}))
        self.assertEqual(values[2], {})

        vaules = ArgsTestClass().foo8(1, b=2)
        self.assertEqual(vaules[0], 1)
        self.assertEqual(vaules[1], {'b':2})

        vaules = ArgsTestClass().foo8({'b':2})
        self.assertEqual(vaules[0], {'b':2})
        self.assertEqual(vaules[1], {})

    def testSimpleStaticMethodCall(self):
        values = ArgsTestClass2.foo(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass2.foo2(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

    def testKeywordStaticMethodCall(self):
        values = ArgsTestClass2.foo2(c=3, b=2, a=1)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass2.foo2(b=2, a=1, c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass2.foo2()
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], None)

        values = ArgsTestClass2.foo2(c=True)
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], True)
        
    def testDefaultValuesStaticMethodCall(self):
        values = ArgsTestClass2.foo3(b=7)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 7)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass2.foo3(a=9)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass2.foo3()
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
    
    def testVarargsStaticMethodCall(self):
        values = ArgsTestClass2.foo4(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass2.foo4(3, 2, 1)
        self.assertEquals(values[0], 3)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 1)
    
    def testKwargsStaticMethodCall(self):
        values = ArgsTestClass2.foo5(x=5, y=7)
        self.assertEquals(values["x"], 5)
        self.assertEquals(values["y"], 7)

    def testComboStaticMethodCall(self):
        values = ArgsTestClass2.foo6(1, 2, 3, x=4, y=5)
        self.assertEquals(values[0][0], 1)
        self.assertEquals(values[0][1], 2)
        self.assertEquals(values[0][2], 3)
        self.assertEquals(values[1]["x"], 4)
        self.assertEquals(values[1]["y"], 5)

    def testEdgeStaticMethodCall(self):
        values = ArgsTestClass2.foo7(1,2,3,b=2)
        self.assertEqual(values[0], 1)
        self.assertEqual(values[1], (2,3))
        self.assertEqual(values[2], {'b':2})

        values = ArgsTestClass2.foo7(1, 2, 3, {'b':2})
        self.assertEqual(values[0], 1)
        self.assertEqual(values[1], (2,3,{'b':2}))
        self.assertEqual(values[2], {})

        vaules = ArgsTestClass2.foo8(1, b=2)
        self.assertEqual(vaules[0], 1)
        self.assertEqual(vaules[1], {'b':2})

        vaules = ArgsTestClass2.foo8({'b':2})
        self.assertEqual(vaules[0], {'b':2})
        self.assertEqual(vaules[1], {})

    def testSimpleClassMethodCall(self):
        values = ArgsTestClass3.foo(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3.foo2(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

    def testKeywordClassMethodCall(self):
        values = ArgsTestClass3.foo2(c=3, b=2, a=1)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3.foo2(b=2, a=1, c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3.foo2()
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], None)

        values = ArgsTestClass3.foo2(c=True)
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], True)
        
        
    def testDefaultValuesClassMethodCall(self):
        values = ArgsTestClass3.foo3(b=7)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 7)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3.foo3(a=9)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3.foo3()
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
    
    def testVarargsClassMethodCall(self):
        values = ArgsTestClass3.foo4(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3.foo4(3, 2, 1)
        self.assertEquals(values[0], 3)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 1)
    
    def testKwargsClassMethodCall(self):
        values = ArgsTestClass3.foo5(x=5, y=7)
        self.assertEquals(values["x"], 5)
        self.assertEquals(values["y"], 7)

    def testComboClassMethodCall(self):
        values = ArgsTestClass3.foo6(1, 2, 3, x=4, y=5)
        self.assertEquals(values[0][0], 1)
        self.assertEquals(values[0][1], 2)
        self.assertEquals(values[0][2], 3)
        self.assertEquals(values[1]["x"], 4)
        self.assertEquals(values[1]["y"], 5)
        
    def testEdgeClassMethodCall(self):
        values = ArgsTestClass3.foo7(1,2,3,b=2)
        self.assertEqual(values[0], 1)
        self.assertEqual(values[1], (2,3))
        self.assertEqual(values[2], {'b':2})

        values = ArgsTestClass3.foo7(1, 2, 3, {'b':2})
        self.assertEqual(values[0], 1)
        self.assertEqual(values[1], (2,3,{'b':2}))
        self.assertEqual(values[2], {})

        vaules = ArgsTestClass3.foo8(1, b=2)
        self.assertEqual(vaules[0], 1)
        self.assertEqual(vaules[1], {'b':2})

        vaules = ArgsTestClass3.foo8({'b':2})
        self.assertEqual(vaules[0], {'b':2})
        self.assertEqual(vaules[1], {})

    def testSimpleIndirectClassMethodCall(self):
        values = ArgsTestClass3().foo(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3().foo2(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

    def testKeywordIndirectClassMethodCall(self):
        values = ArgsTestClass3().foo2(c=3, b=2, a=1)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3().foo2(b=2, a=1, c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3().foo2()
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], None)

        values = ArgsTestClass3().foo2(c=True)
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], True)
        
        
    def testDefaultValuesIndirectClassMethodCall(self):
        values = ArgsTestClass3().foo3(b=7)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 7)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3().foo3(a=9)
        self.assertEquals(values[0], 9)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3().foo3()
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
    
    def testVarargsIndirectClassMethodCall(self):
        values = ArgsTestClass3().foo4(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = ArgsTestClass3().foo4(3, 2, 1)
        self.assertEquals(values[0], 3)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 1)
    
    def testKwargsIndirectClassMethodCall(self):
        values = ArgsTestClass3().foo5(x=5, y=7)
        self.assertEquals(values["x"], 5)
        self.assertEquals(values["y"], 7)

    def testComboIndirectClassMethodCall(self):
        values = ArgsTestClass3().foo6(1, 2, 3, x=4, y=5)
        self.assertEquals(values[0][0], 1)
        self.assertEquals(values[0][1], 2)
        self.assertEquals(values[0][2], 3)
        self.assertEquals(values[1]["x"], 4)
        self.assertEquals(values[1]["y"], 5)
       
    def testKwArgsRecurse(self):
        kwa = kw_args(x=5, y=6)
        if kwa:
            self.assertEquals(kwa.get('x'), 5)
            self.assertEquals(kwa.get('y'), 6)

        kwa = kw_args2(x=5, y=6)
        if kwa:
            self.assertEquals(kwa.get('x'), 5)
            self.assertEquals(kwa.get('y'), 6)

        values = varargs_kwargs(1,2,3,4,c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], (3,4))
        self.assertEquals(values[3]['c'], 3)

        values = varargs_kwargs2(1,2,3,4,c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], (3,4))
        self.assertEquals(values[3]['c'], 3)

        values = varargs_kwargs2(1)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 3)

        values = varargs_kwargs2(1, {'a':1}, {})
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1]['a'], 1)

        values = varargs_kwargs2(1, {'a':1})
        self.assertEquals(values[0], 1)
        try:
            self.assertEquals(values[1], {'a':1})
        except TypeError, e:
            self.fail("Last arg in *args,**kwargs is dict problem")

    def testKwArgsInherit(self):

        c = KwArgs(x=5, y=6)
        self.assertTrue(hasattr(c, 'kwargs'))
        kwa = getattr(c, 'kwargs', None)
        if kwa:
            self.assertEquals(kwa.get('x'), 5)
            self.assertEquals(kwa.get('y'), 6)
            self.assertEquals(kwa.get('z'), 7)

        try:
            c = Kwargs2(x=5, y=6)
            self.assertTrue(hasattr(c, 'kwargs'))
            kwa = getattr(c, 'kwargs', None)
            if kwa:
                self.assertEquals(kwa.get('x'), 5)
                self.assertEquals(kwa.get('y'), 6)
                self.assertEquals(kwa.get('z'), 7)
        except:
            self.assertTrue(False, "runtime error in kwargs, needs investigating")

        c.set_kwargs(x=5, y=6)
        self.assertTrue(hasattr(c, 'kwargs'))
        kwa = getattr(c, 'kwargs', None)
        if kwa:
            self.assertEquals(kwa.get('x'), 5)
            self.assertEquals(kwa.get('y'), 6)
            self.assertEquals(kwa.get('z'), 8)


        c.set_kwargs2(x=5, y=6)
        self.assertTrue(hasattr(c, 'kwargs'))
        kwa = getattr(c, 'kwargs', None)
        if kwa:
            self.assertEquals(kwa.get('x'), 5)
            self.assertEquals(kwa.get('y'), 6)
            self.assertEquals(kwa.get('z'), 8)


        c.set_kwargs3(x=5, y=6)
        self.assertTrue(hasattr(c, 'kwargs'))
        kwa = getattr(c, 'kwargs', None)
        if kwa:
            self.assertEquals(kwa.get('x'), 5)
            self.assertEquals(kwa.get('y'), 6)
            self.assertEquals(kwa.get('z'), 8)

    def testLookupOrder(self):
        def fn(fint = int):
            return fint(1.2);
        class A:
            def fn(self, fint = int):
                return fint(1.2);
        self.assertEqual(fn(), 1)
        self.assertEqual(A().fn(), 1)

    def testArgIsModuleName(self):
        def fn(ArgsTest):
            return foo(ArgsTest, 2, 3)
        self.assertEqual(__name__, 'ArgsTest', "Argument to fn must be equal to module name")
        self.assertEqual(fn('foo'), ['foo', 2, 3])

    def testGetattr(self):
        instance = ArgsTestClass()
        foo = instance.foo

        values = foo(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

        values = foo(*(1, 2, 3))
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

        try:
            values = foo(*(1, 2), **dict(c=3))
            self.assertEquals(values[0], 1)
            self.assertEquals(values[1], 2)
            self.assertEquals(values[2], 3)
        except TypeError:
            self.fail('foo() takes exactly 4 arguments (5 given), bug #503')


def foo(a, b, c):
    return [a, b, c]

def foo2(a=None, b=None, c=None):
    return [a, b, c]

def foo3(a=1, b=2, c=3):
    return [a, b, c]

def foo4(a, b, c, *args):
    return a, b, c, args

def foo5(a, b, c, **kwargs):
    return a, b, c, kwargs

def foo6(a, b, c, *args, **kwargs):
    return (a, b, c, args, kwargs)

def foo7(a, *args, **kwargs):
    return (a, args, kwargs)
    
def foo8(a, **kwargs):
    return (a, kwargs)
    
class ArgsTestClass_foo:
    def __init__(self, a, b, c):
        self.x = [a, b, c]

class ArgsTestClass_foo2:
    def __init__(self, a=None, b=None, c=None):
        self.x = [a, b, c]

class ArgsTestClass_foo3:
    def __init__(self, a=1, b=2, c=3):
        self.x = [a, b, c]

class ArgsTestClass_foo4:
    def __init__(self, a, b, c, *args):
        self.x = a, b, c, args

class ArgsTestClass_foo5:
    def __init__(self, a, b, c, **kwargs):
        self.x = a, b, c, kwargs

class ArgsTestClass_foo6:
    def __init__(self, a, b, c, *args, **kwargs):
        self.x = (a, b, c, args, kwargs)

class ArgsTestClass:
    def foo(self, a, b, c):
        return [a, b, c]
    
    def foo2(self, a=None, b=None, c=None):
        return [a, b, c]
    
    def foo3(self, a=1, b=2, c=3):
        return [a, b, c]
    
    def foo4(self, *args):
        return args
    
    def foo5(self, **kwargs):
        return kwargs
    
    def foo6(self, *args, **kwargs):
        return (args, kwargs)
    
    def foo7(self, a, *args, **kwargs):
        return (a, args, kwargs)
    
    def foo8(self, a, **kwargs):
        return (a, kwargs)
    

class ArgsTestClass2:
    @staticmethod
    def foo(a, b, c):
        return [a, b, c]
    
    @staticmethod
    def foo2(a=None, b=None, c=None):
        return [a, b, c]
    
    @staticmethod
    def foo3(a=1, b=2, c=3):
        return [a, b, c]
    
    @staticmethod
    def foo4(*args):
        return args
    
    @staticmethod
    def foo5(**kwargs):
        return kwargs
    
    @staticmethod
    def foo6(*args, **kwargs):
        return (args, kwargs)

    @staticmethod
    def foo7(a, *args, **kwargs):
        return (a, args, kwargs)
    
    @staticmethod
    def foo8(a, **kwargs):
        return (a, kwargs)
    
class ArgsTestClass3:
    @classmethod
    def foo(self, a, b, c):
        return [a, b, c]
    
    @classmethod
    def foo2(self, a=None, b=None, c=None):
        return [a, b, c]
    
    @classmethod
    def foo3(self, a=1, b=2, c=3):
        return [a, b, c]
    
    @classmethod
    def foo4(self, *args):
        return args
    
    @classmethod
    def foo5(self, **kwargs):
        return kwargs
    
    @classmethod
    def foo6(self, *args, **kwargs):
        return (args, kwargs)

    @classmethod
    def foo7(self, a, *args, **kwargs):
        return (a, args, kwargs)
    
    @classmethod
    def foo8(self, a, **kwargs):
        return (a, kwargs)
    

class KwArgs:
    def __init__(self, z=7, zz=77, **kwargs):
        self.kwargs = kwargs
        self.kwargs['z'] = z # XXX this causes problems: kwargs is undefined

    def set_kwargs(self, z=8, **kwargs):
        self.kwargs = kwargs
        self.kwargs['z'] = z

class Kwargs2(KwArgs):

    def __init__(self, **kwargs):
        KwArgs.__init__(self, **kwargs)

    def set_kwargs2(self, **kwargs):
        KwArgs.set_kwargs(self, **kwargs)

    def set_kwargs3(self, **kwargs):
        skw = getattr(self, "set_kwargs")
        skw(**kwargs)

def kw_args(**kwargs):
    return kwargs

def kw_args2(**kwargs):
    return kw_args(**kwargs)

def varargs_kwargs(arg1, arg2=2, *args, **kwargs):
    return (arg1, arg2, args, kwargs)

def varargs_kwargs2(arg1, arg2=3, *args, **kwargs):
    return varargs_kwargs(arg1, arg2, *args, **kwargs)
