from UnitTest import UnitTest
from write import write, writebr

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
        def f():
            try:
                yield 1
                raise ZeroDivisionError('')
            except:
                yield 2
        self.assertEqual(list(f()), [1, 2])

        def f():
            try:
                yield 1
                try:
                    yield 3
                    raise ZeroDivisionError('')
                except:
                    yield 4
                raise ZeroDivisionError('')
            except:
                yield 2
        self.assertEqual(list(f()), [1, 3, 4, 2])


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

    def testThrow(self):
        def fn():
            yield 1
            yield 2

        g = fn()
        try:
            r = g.throw(TypeError, 'test1')
            self.fail("Exception expected (1)")
        except TypeError, e:
            self.assertTrue(e, 'test1')
        try:
            r = g.next()
            self.fail("StopIteration expected (1)")
        except StopIteration:
            self.assertTrue(True)

        g = fn()
        self.assertEqual(g.next(), 1)
        try:
            r = g.throw(TypeError, 'test2')
            self.fail("Exception expected (2)")
        except TypeError, e:
            self.assertTrue(e, 'test2')
        try:
            r = g.next()
            self.fail("StopIteration expected (2)")
        except StopIteration:
            self.assertTrue(True)


        def fn():
            try:
                yield 1
                yield 2
            except:
                yield 3

        g = fn()
        try:
            r = g.throw(TypeError, 'test3')
            self.fail("Exception expected (3)")
        except TypeError, e:
            self.assertTrue(e, 'test3')

        g = fn()
        self.assertEqual(g.next(), 1)
        try:
            r = g.throw(TypeError, 'test4')
            self.assertEqual(r, 3)
        except TypeError, e:
            self.fail("No exception expected (4)")
        try:
            r = g.next()
            self.fail("StopIteration expected (4)")
        except StopIteration:
            self.assertTrue(True)

    def testClose(self):
        def fn():
            yield 1
            yield 2

        g = fn()
        try:
            r = g.close()
            self.assertEqual(r, None)
        except:
            self.fail("No exception expected (1)")
        try:
            r = g.next()
            self.fail("StopIteration expected (1)")
        except StopIteration:
            self.assertTrue(True)
        try:
            r = g.close()
            self.assertEqual(r, None)
        except StopIteration:
            self.fail("No exception expected (1)")

        g = fn()
        self.assertEqual(g.next(), 1)
        try:
            r = g.close()
            self.assertEqual(r, None)
        except TypeError, e:
            self.fail("No exception expected (2)")
        try:
            r = g.next()
            self.fail("StopIteration expected (2)")
        except StopIteration:
            self.assertTrue(True)

        def fn():
            try:
                yield 1
            except:
                yield 2

        g = fn()
        try:
            r = g.close()
            self.assertEqual(r, None)
        except TypeError, e:
            self.fail("No exception expected (3)")

        g = fn()
        self.assertEqual(g.next(), 1)
        try:
            r = g.close()
            self.fail("RuntimeError expected (4)")
        except RuntimeError, e:
            self.assertEqual(e[0], 'generator ignored GeneratorExit')


    def testPEP255_fib(self):
        # http://www.python.org/dev/peps/pep-0255/

        def fib():
            a, b = 0, 1
            while 1:
                yield b
                a, b = b, a+b

        g = fib()
        r = []
        for i in range(6):
            r.append(g.next())
        self.assertEqual(r, [1, 1, 2, 3, 5, 8])

    def testPEP255_recursion(self):
        me = None
        def g():
            i = me.next()
            yield i
        me = g()
        try:
            me.next()
            self.fail("ValueError expected")
        except ValueError, e:
            self.assertEqual(e[0], 'generator already executing')

    def testPEP255_return(self):
        def f1():
            try:
                return
            except:
               yield 1
        self.assertEqual(list(f1()), [])

        def f2():
            try:
                raise StopIteration
            except:
                yield 42
        self.assertEqual(list(f2()), [42])


    def testPEP255_exceptionPropagation(self):
        def f():
            v = 1/0 # See issue #265
            return {}['not-there']
        def g():
            yield f()  # the zero division exception propagates
            yield 42   # and we'll never get here
        k = g()
        try:
            k.next()
            self.fail("Exception expected")
        except ZeroDivisionError, e:
            self.assertTrue(True)
        except:
            self.assertTrue(True, "ZeroDivisionError expected")
        try:
            k.next()
            self.fail("StopIteration expected")
        except StopIteration:
            self.assertTrue(True)

    def testPEP255_tryExceptFinally(self):
        def f():
            try:
                yield 1
                try:
                    yield 2
                    raise ZeroDivisionError()
                    #1/0
                    yield 3  # never get here
                except ZeroDivisionError:
                    yield 4
                    yield 5
                    raise
                except:
                    yield 6
                yield 7     # the "raise" above stops this
            except:
                yield 8
            yield 9
            try:
                x = 12
            finally:
                yield 10
            yield 11
        self.assertEqual(list(f()), [1, 2, 4, 5, 8, 9, 10, 11])

    def testPEP255_exampleRecursive(self):
        global inorder

        # A recursive generator that generates Tree labels in in-order.
        def _inorder(t):
            if t:
                for x in inorder(t.left):
                    yield x
                yield t.label
                for x in inorder(t.right):
                    yield x
        inorder = _inorder

        # Show it off: create a tree.
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        t = tree(s)
        # Print the nodes of the tree in in-order.
        res = ''
        for x in t:
            res += x
        self.assertEqual(s, res)

    def testPEP255_exampleNonRecursive(self):
        global inorder

        # A non-recursive generator.
        def _inorder(node):
            stack = []
            while node:
                while node.left:
                    stack.append(node)
                    node = node.left
                yield node.label
                while not node.right:
                    try:
                        node = stack.pop()
                    except IndexError:
                        return
                    yield node.label
                node = node.right
        inorder = _inorder

        # Show it off: create a tree.
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        t = tree(s)
        # Print the nodes of the tree in in-order.
        res = ''
        for x in t:
            res += x
        self.assertEqual(s, res)


    def testMixed(self):
        def fn(value = None):
            for i in [-1,0,1,2,3,4]:
                if i < 0:
                    continue
                elif i == 0:
                    yield 0
                elif i == 1:
                    yield 1
                    i = 0
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

    def testGenExp(self):
        
        g = (child for child in [1,2,3])
        self.assertEqual(g.next(), 1)
        self.assertEqual(g.next(), 2)

        try:
            g.throw(KeyError, 'test')
        except KeyError, e:
            self.assertEqual(e[0], 'test')

        if any(isinstance(child, int) for child in [1,2,3]):
            self.assertTrue(True)
        else:
            self.fail("any(isinstance(child, int) for child in [1,2,3])")
        if any(isinstance(child, int) for child in ['1','2','3']):
            self.fail("any(isinstance(child, int) for child in ['1','2','3'])")
        else:
            self.assertTrue(True)

        # #269 - whoops!  webkit barfs / infinite loop on this one
        a = A()
        g = (child for child in a.fn())
        self.assertEqual(g.next(), 1)
        self.assertEqual(g.next(), 2)


class A(object):
    def fn(self):
        yield 1
        yield 2

inorder = None
# A binary tree class.
class Tree:

    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self, level=0, indent="    "):
        s = level*indent + repr(self.label)
        if self.left:
            s = s + "\n" + self.left.__repr__(level+1, indent)
        if self.right:
            s = s + "\n" + self.right.__repr__(level+1, indent)
        return s

    def __iter__(self):
        return inorder(self)

# Create a Tree from a list.
def tree(list):
    n = len(list)
    if n == 0:
        return []
    i = n / 2
    return Tree(list[i], tree(list[:i]), tree(list[i+1:]))

