from UnitTest import UnitTest
import sys


class MyException:

    def __str__(self):
        return "MyException"


class MyException2:

    def __str__(self):
        return "MyException2"


class ExceptionTest(UnitTest):

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
            self.assertEqual(e.__str__(), 'MyException',
                             "Caught exception does not match")
            return
        self.fail('MyException was not caught or raised')

    def testCatchMultiClassException(self):
        try:
            raise MyException()
        except (MyException, MyException2), e:
            self.assertEqual(e.__str__(), 'MyException',
                             "Caught exception does not match")
            return
        self.fail('MyException was not caught or raised')

    def testCatchStringException(self):
        try:
            raise "test"
        except "test":
            return
        except TypeError, e:
            self.fail(e)
        self.fail('"test" was not caught or raised')

    def testBuiltInException(self):
        try:
            raise LookupError('hoschi')
        except LookupError, err:
            self.assertEqual(err.__class__.__name__, 'LookupError')
            return
        self.fail("LookupError should be caught")

    def testZeroDivisionError(self):
        try:
            v = 1/0
        except ZeroDivisionError, err:
            self.assertEqual(err.__class__.__name__, 'ZeroDivisionError')
            return
        self.fail("ZeroDivisionError should be caught bug #265")

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
        try:
            pass
        except KeyError, e:
            pass
        except (TypeError, LookupError), e:
            pass
        except:
            pass
        finally:
            pass

        try:
            a = 1
        except:
            a = 2
        else:
            a = 3
        finally:
            self.assertEqual(a, 3)
            a = 4
        self.assertEqual(a, 4)

        try:
            a = 11
            raise KeyError('test')
        except:
            a = 12
        else:
            a = 13
        finally:
            self.assertEqual(a, 12)
            a = 14
        self.assertEqual(a, 14)

        try:
            a = 1
        finally:
            a = 2
        self.assertEqual(a, 2)
        try:
            a = 1
            try:
                b = 1
            except:
                b = 2
            else:
                b = 3
            finally:
                self.assertEqual(b, 3)
                b = 4
        except:
            a = 2
        else:
            a = 3
        finally:
            self.assertEqual(a, 3)
            a = 4
        self.assertEqual(a, 4)
        self.assertEqual(b, 4)

        sys.exc_clear()
        try:
            raise
            self.fail("No error raised on 'raise' after 'sys.exc_clear()'")
        except TypeError, e:
            # use message which works for both Python 2.5 and 2.6
            self.failUnless(e.args[0].startswith('exceptions must be classes'))
        except:
            e = sys.exc_info()
            self.fail('TypeError expected, got %s' % e[0])

        try:
            raise KeyError, 'test'
            self.fail('No error raised')
        except KeyError, e:
            self.assertEqual(e.args[0], 'test')
        except:
            e = sys.exc_info()
            self.fail('KeyError expected, got %s' % e[0])
            e = e[1]

        try:
            raise
        except:
            err = sys.exc_info()
            self.assertEqual(e.args[0], err[1].args[0])

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
                self.assertTrue(e1.args[0] == 'KeyError' or e1.args[0] == 'TypeError')
            except AttributeError, e2:
                raised_errors.append(e2)
                self.assertTrue(e2.args[0] == 'AttributeError')
            except:
                e3 = sys.exc_info()[1]
                raised_errors.append(e3)
                self.assertTrue(e3.args[0] == 'LookupError')
        self.assertEqual(len(raised_errors), len(raise_errors))

        try:
            try:
                raise TypeError('TypeError')
            except KeyError, e:
                self.fail("Got KeyError")
            self.fail("TypeError should not be ignored")
        except TypeError, e:
            self.assertEqual(e.args[0], 'TypeError')

    def testCatchSuperException(self):
        try:
            raise TypeError('test')
        except Exception, e:
            self.assertTrue(True)
        except:
            self.fail("Failed to catch exception: bug #254")

    def testAssertionError(self):
        try:
            assert True
            self.assertTrue(True)
        except AssertionError, e:
            self.fail("Got an unexpected assertion error: %r" % e)
        try:
            assert False
            self.fail("AssertionError expected")
        except AssertionError, e:
            self.assertTrue(True)
        try:
            assert False, 'reason'
            self.fail("AssertionError expected")
        except AssertionError, e:
            self.assertEqual(e.args[0], 'reason')
