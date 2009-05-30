"""
The ``ui.DialogBox`` class implements a panel that behaves like a dialog box.

A dialog box has an optional caption, and a widget which is displayed as the
main part of the dialog box.  The user can drag the dialog box around by
clicking on the caption.

The DialogBox class makes use of stylesheet definitions; if these are not
supplied, the dialog box will look very strange.  The following stylesheet
definitions are used by the example shown below:

    .gwt-DialogBox {
      border: 2px outset;
      background-color: white;
    }

    .gwt-DialogBox .Caption {
      background-color: #C3D9FF;
      padding: 3px;
      margin: 2px;
      font-weight: bold;
      cursor: default;
    }

    .gwt-DialogBox .Contents {
        padding: 10px;
    }

Because the ``DialogBox`` class is derived from ``PopupPanel``, the user should
be able to click outside the dialog box to close it.  However, because of a
problem with Firefox 3, this does not work.  To get around this, the example
shown below implements a "Close" button the user can click on.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Button import Button
from pyjamas import Window

class DialogBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.add(Button("Show Dialog", getattr(self, "showDialog")))


    def showDialog(self, event):
        contents = VerticalPanel()
        contents.setSpacing(4)
        contents.add(HTML('You can place any contents you like in a dialog box.'))
        contents.add(Button("Close", getattr(self, "onClose")))
        contents.setStyleName("Contents")

        self._dialog = DialogBox()
        self._dialog.setHTML('<b>Welcome to the dialog box</b>')
        self._dialog.setWidget(contents)

        left = (Window.getClientWidth() - 200) / 2
        top = (Window.getClientHeight() - 100) / 2
        self._dialog.setPopupPosition(left, top)
        self._dialog.show()


    def onClose(self, event):
        self._dialog.hide()

