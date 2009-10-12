from UnitTest import UnitTest
import time
from write import write, writebr

class A(object):

    def __init__(self, x):
        self.x = x

    def getX(self):
        return self.x

def fib(n):
    if n<3.0:
        return 1.0
    return fib(n-2.0)+fib(n-1.0)

def int_fib(n):
    if n<3:
        return 1
    return int_fib(n-2)+int_fib(n-1)

def long_fib(n):
    if n<3L:
        return 1L
    return long_fib(n-2L)+long_fib(n-1L)

class LoopTest(UnitTest):

    def testLoop1(self):
        t1 = t0 = time.time()
        n = 1000
        a = A(1)
        m = 0;
        while t1 - t0 == 0:
            m += 1
            for i in range(n):
                x = a.getX()
            t1 = time.time()
        dt = t1 - t0
        writebr("Loop1: %.2f/sec" % (n*m/dt))

    def testLoop2(self):
        t1 = t0 = time.time()
        n = 100
        m = 0.0
        while t1 - t0 == 0:
            m += 1.0
            for i in range(n):
                fib(10.0)
            t1 = time.time()
        dt = t1 - t0
        writebr("Loop2 (float): %.2f/sec" % (n*m/dt))

    def testLoop3(self):
        t1 = t0 = time.time()
        n = 100
        m = 0.0
        while t1 - t0 == 0:
            m += 1.0
            for i in range(n):
                int_fib(10)
            t1 = time.time()
        dt = t1 - t0
        writebr("Loop3 (int): %.2f/sec" % (n*m/dt))

    def testLoop4(self):
        t1 = t0 = time.time()
        n = 100
        m = 0.0
        while t1 - t0 == 0:
            m += 1.0
            for i in range(n):
                long_fib(10L)
            t1 = time.time()
        dt = t1 - t0
        writebr("Loop4 (long): %.2f/sec" % (n*m/dt))

if __name__ == '__main__':
    l = LoopTest()
    l.run()
