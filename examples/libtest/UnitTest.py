from write import write, writebr
import sys

class UnitTest:
    def __init__(self):
        self.tests_completed=0
        self.tests_failed=0
        self.tests_passed=0
        self.test_methods=[]

        # define alternate names for methods
        self.assertEqual = self.failUnlessEqual
        self.assertEquals = self.failUnlessEqual

        self.assertNotEqual = self.failIfEqual
        self.assertFalse = self.failIf
        self.assertTrue = self.failUnless

    def run(self):
        self.getTestMethods()
        for test_method_name in self.test_methods:
            test_method=getattr(self, test_method_name)
            self.current_test_name = test_method_name
            self.setUp()
            test_method()
            self.tearDown()
            self.current_test_name = None

        self.displayStats()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def getName(self):
        return self.__class__.__name__

    def getNameFmt(self, msg=""):
        if self.getName():
            if msg:
                msg=" " + msg
            if self.current_test_name:
                msg += " (%s) " % self.current_test_name
            return self.getName() + msg + ": "
        return ""

    def getTestMethods(self):
        self.test_methods=[]
        for m in dir(self):
            if self.isTestMethod(m):
                self.test_methods.append(m)

    def isTestMethod(self, method):
        if callable(getattr(self, method)):
            if method.find("test") == 0:
                return True
        return False

    def fail(self, msg=None):
        self.startTest()
        self.tests_failed+=1

        if not msg:
            msg="assertion failed"

        title="<b>" + self.getNameFmt("Test failed") + "</b>"
        writebr(title + msg)
        if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
            from __pyjamas__ import JS
            JS("""if (typeof console != 'undefined') {
                console.error(msg)
                console.trace()
            }""")
        return False

    def startTest(self):
        self.tests_completed+=1

    def failIf(self, expr, msg=None):
        self.startTest()
        if expr:
            return self.fail(msg)

    def failUnless(self, expr, msg=None):
        self.startTest()
        if not expr:
            return self.fail(msg)

    def failUnlessEqual(self, first, second, msg=None):
        self.startTest()
        if not first == second:
            if not msg:
                msg=repr(first) + " != " + repr(second)
            return self.fail(msg)

    def failIfEqual(self, first, second, msg=None):
        self.startTest()
        if first == second:
            if not msg:
                msg=repr(first) + " == " + repr(second)
            return self.fail(msg)

    def failUnlessAlmostEqual(self, first, second, places=7, msg=None):
        self.startTest()
        if round(second-first, places) != 0:
            if not msg:
                msg=repr(first) + " != " + repr(second) + " within " + repr(places) + " places"
            return self.fail(msg)

    def failIfAlmostEqual(self, first, second, places=7, msg=None):
        self.startTest()
        if round(second-first, places)  is  0:
            if not msg:
                msg=repr(first) + " == " + repr(second) + " within " + repr(places) + " places"
            return self.fail(msg)

    # based on the Python standard library
    def assertRaises(self, excClass, callableObj, *args, **kwargs):
        """
        Fail unless an exception of class excClass is thrown
        by callableObj when invoked with arguments args and keyword
        arguments kwargs. If a different type of exception is
        thrown, it will not be caught, and the test case will be
        deemed to have suffered an error, exactly as for an
        unexpected exception.
        """
        self.startTest()
        try:
            callableObj(*args, **kwargs)
        except excClass, exc:
            return
        else:
            if hasattr(excClass, '__name__'):
                excName = excClass.__name__
            else:
                excName = str(excClass)
            self.fail("%s not raised" % excName)

    def displayStats(self):
        if self.tests_failed:
            bg_colour="#ff0000"
            fg_colour="#ffffff"
        else:
            bg_colour="#00ff00"
            fg_colour="#000000"

        tests_passed=self.tests_completed - self.tests_failed
        if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
            output="<table cellpadding=4 width=100%><tr><td bgcolor='" + bg_colour + "'><font face='arial' size=4 color='" + fg_colour + "'><b>"
        else:
            output = ""
        output+=self.getNameFmt() + "Passed %d " % tests_passed + "/ %d" % self.tests_completed + " tests"

        if self.tests_failed:
            output+=" (%d failed)" % self.tests_failed

        if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
            output+="</b></font></td></tr></table>"
        else:
            output+= "\n"

        write(output)

