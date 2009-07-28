from UnitTest import UnitTest, IN_BROWSER
from pyjamas import Window

class WindowTest(UnitTest):

    """tests for javascript object conversion"""

    def onWindowResized(self, width, height):

        if not self.resize_test:
            self.fail("onWindowResized called after WindowListener removed")
            return

        nh = Window.getClientHeight()
        nw = Window.getClientWidth()
        # TODO: we cannot assert the exact size, because, we have toolbars
        self.assertTrue(nw!=self.w)
        self.assertTrue(nh!=self.h)
        self.assertTrue(isinstance(nw, int))
        self.assertTrue(isinstance(nh, int))

        # put the window back to its original size
        # but make sure to switch off resize notify!
        self.resize_test = False
        Window.removeWindowResizeListener(self)
        Window.resize(self.w, self.h)

    def testResize(self):
        # TODO: window resizing does not work accuratly in browser
        # because getClientWidth etc does not really match GWT. We
        # need to copy the GWT implementation
        if IN_BROWSER:
            return
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
