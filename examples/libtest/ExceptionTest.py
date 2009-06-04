from UnitTest import UnitTest
import sys

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

    def testStrReprSingleArg(self):
        args = ('test',)

        e = BaseException(*args)
        self.assertEqual(e.args[0], args[0])
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "BaseException('test',)")

        e = Exception(*args)
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "Exception('test',)")

        e = TypeError(*args)
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "TypeError('test',)")

        e = StandardError(*args)
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "StandardError('test',)")

        e = LookupError(*args)
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "LookupError('test',)")

        e = KeyError(*args)
        self.assertEqual(str(e), "'%s'" % args[0])
        self.assertEqual(repr(e), "KeyError('test',)")

        e = AttributeError(*args)
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "AttributeError('test',)")

        e = NameError(*args)
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "NameError('test',)")

        e = ValueError(*args)
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "ValueError('test',)")

        e = IndexError(*args)
        self.assertEqual(str(e), args[0])
        self.assertEqual(repr(e), "IndexError('test',)")

    def testSyntax(self):
        raise_errors = [KeyError('KeyError'), TypeError('TypeError'),
                        AttributeError('AttributeError'),
                        LookupError('LookupError')]
        raised_errors = []
        for err in raise_errors:
            try:
                raise err
                self.fail("Failed to raise exception")
            except (KeyError, TypeError), e1:
                raised_errors.append(e1)
                self.assertTrue(e1.message == 'KeyError' or e1.message == 'TypeError')
            except AttributeError, e2:
                raised_errors.append(e2)
                self.assertTrue(e2.message == 'AttributeError')
            except:
                e3 = sys.exc_info()[1]
		raised_errors.append(e3)
                self.assertTrue(e3.message == 'LookupError')
        self.assertEqual(len(raised_errors), len(raise_errors))

