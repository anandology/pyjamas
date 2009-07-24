from UnitTest import UnitTest
from pyjamas import Window

class WindowListener(object):

    def __init__(self):
        self.called = []

    def onWindowClosed(self):
        self.called.append('onWindowClosed')

    def onWindowClosing(self):
        self.called.append('onWindowClosing')

    def onWindowResized(self, w, h):
        self.called.append('onWindowResized')

class WindowTest(UnitTest):

    """tests for javascript object conversion"""

    def __init__(self):
        UnitTest.__init__(self)

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

    def testListeners(self):
        l = WindowListener()
        Window.addWindowCloseListener(l)
        Window.addWindowResizeListener(l)
        Window.onClosed()
        Window.onClosing()
        Window.onResize()
        self.assertEquals(l.called,
                          ['onWindowClosed', 'onWindowClosing', 'onWindowResized'])
