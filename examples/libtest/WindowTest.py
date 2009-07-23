from UnitTest import UnitTest
from pyjamas import Window

class WindowTest(UnitTest):

    """tests for javascript object conversion"""

    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Window"

    def testClientDimensions(self):
        h = Window.getClientHeight()
        w = Window.getClientWidth()
        self.assertTrue(isinstance(w, int))
        self.assertTrue(isinstance(h, int))

    def testLocation(self):
        self.assertTrue(Window.getLocation().getHref().endswith(
            'LibTest.html'))
        self.assertEquals(Window.getTitle(),
                          'PyJamas Auto-Generated HTML file LibTest')
