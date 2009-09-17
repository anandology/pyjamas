from UnitTest import UnitTest

#from __pyjamas__ import debugger

class GeneratorTest(UnitTest):

    def testSimpleStatement(self):
        def fn():
            yield 1
            yield 2

        g = fn()
        self.assertEqual(g.next(), 1)
        self.assertEqual(g.next(), 2)

        for i, g in enumerate(fn()):
            self.assertEqual(i, g-1)

        def fn(n):
            i = 0
            yield i
            i += 1
            j = i
            yield i
            yield j
            j *= 100
            i += j
            yield j
            yield i
            yield n + i

        r = []
        for i in fn(8):
            r.append(i)
        self.assertEqual(r, [0, 1, 1, 100, 101, 109])

        a = A()
        r = []
        for i in a.fn():
            r.append(i)
        self.assertEqual(r, [1,2])

    def testSimpleFor(self):
        def fn():
            for i in [1,2]:
                yield i

        g = fn()
        self.assertEqual(g.next(), 1)
        self.assertEqual(g.next(), 2)

        for i, g in enumerate(fn()):
            self.assertEqual(i, g-1)

    def testSimpleWhile(self):
        def fn(n):
            i = 0
            while i < n:
                yield i
                yield i * 10
                i += 1

        r = []
        for i in fn(4):
            r.append(i)
        self.assertEqual(r, [0, 0, 1, 10, 2, 20, 3, 30])

        def fn(n):
            i = 0
            while i < n:
                yield i
                i = 100
                yield i
                i += 1

        r = []
        for i in fn(50):
            r.append(i)
        self.assertEqual(r, [0, 100])

        def fn():
            y = 0
            while y == 0:
                y += 1
                yield y
                y += 1
                yield y

        r = []
        for y in fn():
            r.append(y)
        self.assertEqual(r, [1, 2])

    def testSimpleIfThenElse(self):
        def fn(n):
            while n < 3:
                if n < 0:
                    yield "less than zero"
                elif n == 0:
                    yield "zero"
                elif n == 1:
                    yield "one"
                else:
                    yield "more than one"
                n += 1

        r = []
        for i in fn(-1):
            r.append(i)
        self.assertEqual(r, ['less than zero', 'zero', 'one', 'more than one'])

    def testSimpleTryBody(self):
        def fn():
            i = 1
            try:
                yield i+1
                yield i+2
            except:
                pass

        r = []
        for i in fn():
            r.append(i)
        self.assertEqual(r, [2,3])

        def fn():
            y = 0
            while y == 0:
                try:
                    y += 1
                    yield y
                    y += 1
                    yield y
                finally:
                    y += 2
            yield y

        r = []
        for i in fn():
            r.append(i)
        self.assertEqual(r, [1,2,4])

    def testSimpleTryExceptElseFinally(self):
        def fn(n):
            for i in range(n):
                try:
                    if i == 0:
                        yield "try %d" % i
                    elif i < 3:
                        raise TypeError(i)
                    elif i == 3:
                        raise KeyError(i)
                except TypeError, e:
                    yield "TypeError %d (1)" % i
                    yield "TypeError %d (2)" % i
                except:
                    yield "Exception %d (1)" % i
                    yield "Exception %d (2)" % i
                else:
                    yield "else %d (1)" % i
                    yield "else %d (2)" % i
                finally:
                    yield "finally %d (1)" % i
                    yield "finally %d (2)" % i

        r = []
        for i in fn(5):
            r.append(i)
        self.assertEqual(r, ['try 0',
                             'else 0 (1)',
                             'else 0 (2)',
                             'finally 0 (1)',
                             'finally 0 (2)',
                             'TypeError 1 (1)',
                             'TypeError 1 (2)',
                             'finally 1 (1)',
                             'finally 1 (2)',
                             'TypeError 2 (1)',
                             'TypeError 2 (2)',
                             'finally 2 (1)',
                             'finally 2 (2)',
                             'Exception 3 (1)',
                             'Exception 3 (2)',
                             'finally 3 (1)',
                             'finally 3 (2)',
                             'else 4 (1)',
                             'else 4 (2)', 
                             'finally 4 (1)',
                             'finally 4 (2)'])

        def fn(n):
            for i in range(n):
                try:
                    if i == 0:
                        yield "try %d" % i
                    elif i < 3:
                        raise TypeError(i)
                    elif i == 3:
                        raise KeyError(i)
                    else:
                        break
                except TypeError, e:
                    yield "TypeError %d (1)" % i
                    yield "TypeError %d (2)" % i
                except:
                    yield "Exception %d (1)" % i
                    yield "Exception %d (2)" % i
                else:
                    yield "else %d (1)" % i
                    yield "else %d (2)" % i
                finally:
                    yield "finally %d (1)" % i
                    yield "finally %d (2)" % i

        r = []
        for i in fn(5):
            r.append(i)
        self.assertEqual(r, ['try 0',
                             'else 0 (1)',
                             'else 0 (2)',
                             'finally 0 (1)',
                             'finally 0 (2)',
                             'TypeError 1 (1)',
                             'TypeError 1 (2)',
                             'finally 1 (1)',
                             'finally 1 (2)',
                             'TypeError 2 (1)',
                             'TypeError 2 (2)',
                             'finally 2 (1)',
                             'finally 2 (2)',
                             'Exception 3 (1)',
                             'Exception 3 (2)',
                             'finally 3 (1)',
                             'finally 3 (2)',
                             'finally 4 (1)',
                             'finally 4 (2)'])


    def testSend(self):
        def fn(value=None):
            while True:
                value = (yield value)

        g = fn(1)
        self.assertEqual(g.next(), 1)
        self.assertEqual(g.next(), None)
        self.assertEqual(g.send(2), 2)

    def testMixed(self):
        def fn(value = None):
            for i in [-1,0,1,2,3,4]:
                if i < 0:
                    continue
                elif i == 0:
                    yield 0
                elif i == 1:
                    yield 1
                    yield value
                    yield 2
                else:
                    try:
                        v = i/value
                    except:
                        v = i
                    yield v

        r = []
        for i in fn():
            r.append(i)
        self.assertEqual(r, [0, 1, None, 2, 2, 3, 4])


class A(object):
    def fn(self):
        yield 1
        yield 2

