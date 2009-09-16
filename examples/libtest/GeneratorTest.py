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

