from UnitTest import UnitTest
import time
from write import write, writebr

class A(object):

    def __init__(self, x):
        self.x = x

    def getX(self):
        return self.x

class LoopTest(UnitTest):

    def testLoop1(self):
        t = time.time()
        loops = 0
        a = A(1)
        while time.time()<(t+0.4):
            loops+=1
            x = a.getX()
        writebr("Loops in 0.4 seconds: %s"  % loops)
