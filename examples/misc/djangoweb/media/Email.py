from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.Composite import Composite
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.TextBox import TextBox
from pyjamas.JSONService import JSONProxy

from pyjamas import Factory

class Email(Composite):
    def __init__(self, **kwargs):

        element = None
        if kwargs.has_key('Element'):
            element = kwargs.pop('Element')

        panel = VerticalPanel(Element=element)
        Composite.__init__(self, panel, **kwargs)

        self.TEXT_WAITING = "Please wait..."
        self.TEXT_ERROR = "Server Error"

        self.remote_py = EchoServicePython()

        self.status=Label()
        self.subject = TextBox()
        self.subject.setVisibleLength(60)
        self.sender = TextBox()
        self.sender.setVisibleLength(40)
        self.message = TextArea()
        self.message.setCharacterWidth(60)
        self.message.setVisibleLines(15)
        
        self.button_py = Button("Send", self)

        buttons = HorizontalPanel()
        buttons.add(self.button_py)
        buttons.setSpacing(8)
        
        panel.add(HTML("Subject:"))
        panel.add(self.subject)
        panel.add(HTML("From:"))
        panel.add(self.sender)
        panel.add(HTML("Your Message - please keep it to under 1,000 characters"))
        panel.add(self.message)
        panel.add(buttons)
        panel.add(self.status)
        
    def onClick(self, sender):
        self.status.setText(self.TEXT_WAITING)
        text = self.message.getText()
        msg_sender = self.sender.getText()
        msg_subject = self.subject.getText()

        # demonstrate proxy & callMethod()
        if sender == self.button_py:
            id = self.remote_py.send(msg_sender, msg_subject, text, self)
        if id<0:
            self.status.setText(self.TEXT_ERROR)

    def onRemoteResponse(self, response, request_info):
        self.status.setText(response)

    def onRemoteError(self, code, message, request_info):
        self.status.setText("Server Error or Invalid Response: ERROR " + \
                str(code) + " - " + str(message))

Factory.registerClass('pyjamas.apps.Email', Email)

class EchoServicePython(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/services/email.py", ["send"])
