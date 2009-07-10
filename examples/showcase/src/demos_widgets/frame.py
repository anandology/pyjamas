"""
The ``ui.Frame`` class is used to embed a separate HTML page within your
application.

If you pass a URL when the Frame is created, that URL will be used immediately.
Alternatively, you can call the ``Frame.setUrl()`` method to change the URL at
any time.  You can also call ``Frame.getUrl()`` to retrieve the current URL for
this frame.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Frame import Frame

class FrameDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        frame = Frame("http://google.com",
                      Width="100%",
                      Height="200px")
        self.add(frame)

