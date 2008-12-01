from UnitTest import UnitTest

class ExceptionTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Exception"
 
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
