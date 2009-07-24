from UnitTest import UnitTest
from pyjamas import Window

class WindowTest(UnitTest):

    """tests for javascript object conversion"""

    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Window"

    def onWindowResized(self, width, height):

        if not self.resize_test:
            self.fail("onWindowResized called after WindowListener removed")
            return

        nh = Window.getClientHeight()
        nw = Window.getClientWidth()
        self.assertEquals(nw, 800)
        self.assertEquals(nh, 600)

        # put the window back to its original size
        # but make sure to switch off resize notify!
        self.resize_test = False
        Window.removeWindowResizeListener(self)
        Window.resize(self.w, self.h)

    def testResize(self):
       
        self.resize_test = True
        Window.addWindowResizeListener(self)

        self.h = Window.getClientHeight()
        self.w = Window.getClientWidth()
        Window.resize(800, 600)

    def testClientDimensions(self):
        h = Window.getClientHeight()
        w = Window.getClientWidth()
        self.assertTrue(isinstance(w, int))
        self.assertTrue(isinstance(h, int))

    def testLocation(self):
        self.assertTrue(Window.getLocation().getHref().endswith(
            'LibTest.html'))

    def testTitle(self):
        self.assertEquals(Window.getTitle(),
                          'PyJamas Auto-Generated HTML file LibTest')
