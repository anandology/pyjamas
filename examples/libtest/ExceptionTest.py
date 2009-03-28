from UnitTest import UnitTest

class MyException:

    def toString(self):
        return "MyException"

class MyException2:

    def toString(self):
        return "MyException2"

class ExceptionTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Exception"

    def testTypeError(self):
        try:
            raise TypeError("fred")
        except:
            self.assertTrue(True, "the exception should have happened")
            return
        self.assertTrue(False, "the exception should have happened")
            
    def testExceptionOrdTrigger(self):
        try:
            x = ord(5) # shouldn't be a number
        except:
            self.assertTrue(True, "the exception should have happened")
            return
        self.assertTrue(False, "mustn't be able to do ord() on a number")

    def testExceptionOrdNoTrigger(self):
        try:
            x = ord("5")
        except:
            self.assertTrue(False, "the exception shouldn't have happened")
            return
        self.assertTrue(True, "the exception should have happened")


    def testRaiseException(self):
        try:
            raise MyException()
        except:
            return
        self.fail('MyException was not raised')

    def testCatchClassException(self):
        try:
            raise MyException()
        except MyException, e:
            self.assertEqual(e.toString(), 'MyException',
                             "Caught exception does not match")
            return
        self.fail('MyException was not caught or raised')

    def testCatchMultiClassException(self):
        try:
            raise MyException()
        except (MyException, MyException2), e:
            self.assertEqual(e.toString(), 'MyException',
                             "Caught exception does not match")
            return
        self.fail('MyException was not caught or raised')

    def testCatchStringException(self):
        try:
            raise "test"
        except "test":
            return
        self.fail('"test" was not caught or raised')

    def testBuiltInException(self):
        try:
            raise LookupError('hoschi')
        except LookupError, err:
            self.assertEqual(err.__class__.__name__, 'LookupError')
            return
        self.fail("LookupError should be caught")
