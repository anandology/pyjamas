"""
The ``ui.FileUpload`` class implements a file uploader widget.

The FileUpload widget must be inside a ``ui.FormPanel`` which is used to submit
the HTML form to the server.  Note that you must set the form encoding and
method like this:

        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
        self.form.setMethod(FormPanel.METHOD_POST)

This will ensure that the form is submitted in a way that allows files to be
uploaded.

The example below doesn't really work, as there is no suitable server at
``nonexistent.com``.  However, it does show how a file upload widget could be
used within a FormPanel.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.FileUpload import FileUpload
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button

class FileUploadDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.form = FormPanel()
        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
        self.form.setMethod(FormPanel.METHOD_POST)
        self.form.setAction("http://nonexistent.com")
        self.form.setTarget("results")

        vPanel = VerticalPanel()

        hPanel = HorizontalPanel()
        hPanel.setSpacing(5)
        hPanel.add(Label("Upload file:"))

        self.field = FileUpload()
        self.field.setName("file")
        hPanel.add(self.field)

        hPanel.add(Button("Submit", getattr(self, "onBtnClick")))

        vPanel.add(hPanel)

        results = NamedFrame("results")
        vPanel.add(results)

        self.form.add(vPanel)
        self.add(self.form)


    def onBtnClick(self, event):
        self.form.submit()

