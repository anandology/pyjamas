import pyjd

from pyjamas.ui.Label import Label
from pyjamas.ui.RootPanel import RootPanel

class BrowserDetect:
    def i_am(self):
        return None

    def onModuleLoad(self):
        self.l = Label()
        RootPanel().add(self.l)
        self.display()

    def display(self):
        i_am = self.i_am()
        if i_am is None:
            self.l.setText("Browser not detected/supported")
        else:
            self.l.setText(
                "%s detected. This is the %s version of the application." % (
                    i_am, i_am,
                ),
            )


if __name__ == '__main__':
    pyjd.setup("./BrowserDetect.html")
    app = BrowserDetect()
    app.onModuleLoad()
    pyjd.run()
