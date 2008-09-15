from UnitTest import UnitTest

class ArgsTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Args"
 
    def testSimpleCall(self):
        values = foo(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = foo2(1, 2, 3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)

    def testKeywordCall(self):
        values = foo2(c=3, b=2, a=1)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = foo2(b=2, a=1, c=3)
        self.assertEquals(values[0], 1)
        self.assertEquals(values[1], 2)
        self.assertEquals(values[2], 3)
        
        values = foo2()
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], None)

        values = foo2(c=True)
        self.assertEquals(values[0], None)
        self.assertEquals(values[1], None)
        self.assertEquals(values[2], True)
        
        
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


