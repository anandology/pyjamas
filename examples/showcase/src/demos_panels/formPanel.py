"""
The ``ui.FormPanel`` class implements a traditional HTML form.

Any ``TextBox``, ``PasswordTextBox``, ``TextArea``, ``RadioButton``,
``CheckBox``, ``ListBox``, ``FileUpload`` and ``Hidden`` fields contained
within the form panel will be sent to the server when the form is submitted.

The example below calls Google to perform a search using the query entered by
the user into the text field.  The results are shown in a separate Frame.
Alternatively, you can call ``Form.addFormHandler(handler)`` to manually
process the results of posting the form.  When this is done,
``handler.onSubmit(event)`` will be called when the user is about to submit the
form; call ``event.setCancelled(True)`` to cancel the event within this method.
Also, ``handler.onSubmitComplete(event)`` will be called when the results of
submitting the form are returned back to the browser.  Call
``event.getResults()`` to retrieve the (plain-text) value returned by the
server.

Note that if you use a ``ui.FileUpload`` widget in your form, you must set the
form encoding and method like this:

        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
        self.form.setMethod(FormPanel.METHOD_POST)

This will ensure that the form is submitted in a way that allows files to be
uploaded.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button

class FormPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.form = FormPanel()
        self.form.setAction("http://google.com/search")
        self.form.setTarget("results")

        vPanel = VerticalPanel()
        vPanel.setSpacing(5)

        hPanel = HorizontalPanel()
        hPanel.setSpacing(5)

        hPanel.add(Label("Search for:"))

        self.field = TextBox()
        self.field.setName("q")
        hPanel.add(self.field)

        hPanel.add(Button("Submit", getattr(self, "onBtnClick")))

        vPanel.add(hPanel)

        results = NamedFrame("results")
        vPanel.add(results)

        self.form.add(vPanel)
        self.add(self.form)


    def onBtnClick(self):
        self.form.submit()


