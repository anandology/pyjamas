from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ListBox import ListBox
from pyjamas.JSONService import JSONProxy

class JSONRPCExample:
    def onModuleLoad(self):
        self.TEXT_WAITING = "Waiting for response..."
        self.TEXT_ERROR = "Server Error"
        self.METHOD_ECHO = "Echo"
        self.METHOD_REVERSE = "Reverse"
        self.METHOD_UPPERCASE = "UPPERCASE"
        self.METHOD_LOWERCASE = "lowercase"
        self.methods = [self.METHOD_ECHO, self.METHOD_REVERSE, self.METHOD_UPPERCASE, self.METHOD_LOWERCASE]

        self.remote_php = EchoServicePHP()
        self.remote_py = EchoServicePython()

        self.status=Label()
        self.text_area = TextArea()
        self.text_area.setText(r"{'Test'} [\"String\"]")
        self.text_area.setCharacterWidth(80)
        self.text_area.setVisibleLines(8)
        
        self.method_list = ListBox()
        self.method_list.setName("hello")
        self.method_list.setVisibleItemCount(1)
        for method in self.methods:
            self.method_list.addItem(method)
        self.method_list.setSelectedIndex(0)

        method_panel = HorizontalPanel()
        method_panel.add(HTML("Remote string method to call: "))
        method_panel.add(self.method_list)
        method_panel.setSpacing(8)

        self.button_php = Button("Send to PHP Service", self)
        self.button_py = Button("Send to Python Service", self)

        buttons = HorizontalPanel()
        buttons.add(self.button_php)
        buttons.add(self.button_py)
        buttons.setSpacing(8)
        
        info = r"<h2>JSON-RPC Example</h2><p>This example demonstrates the calling of server services with <a href=\"http://json-rpc.org/\">JSON-RPC</a>."
        info += "<p>Enter some text below, and press a button to send the text to an Echo service on your server. An echo service simply sends the exact same text back that it receives."
        
        panel = VerticalPanel()
        panel.add(HTML(info))
        panel.add(self.text_area)
        panel.add(method_panel)
        panel.add(buttons)
        panel.add(self.status)
        
        RootPanel().add(panel)

    def onClick(self, sender):
        self.status.setText(self.TEXT_WAITING)
        method = self.methods[self.method_list.getSelectedIndex()]
        text = self.text_area.getText()

        # demonstrate proxy & callMethod()
        if sender == self.button_php:
            if method == self.METHOD_ECHO:
                id = self.remote_php.echo(text, self)
            elif method == self.METHOD_REVERSE:
                id = self.remote_php.callMethod("reverse", [text], self)
            elif method == self.METHOD_UPPERCASE:
                id = self.remote_php.uppercase(text, self)
            elif method == self.METHOD_LOWERCASE:
                id = self.remote_php.lowercase(text, self)
        else:
            if method == self.METHOD_ECHO:
                id = self.remote_py.echo(text, self)
            elif method == self.METHOD_REVERSE:
                id = self.remote_py.reverse(text, self)
            elif method == self.METHOD_UPPERCASE:
                id = self.remote_py.uppercase(text, self)
            elif method == self.METHOD_LOWERCASE:
                id = self.remote_py.lowercase(text, self)
        if id<0:
            self.status.setText(self.TEXT_ERROR)

    def onRemoteResponse(self, response, request_info):
        self.status.setText(response)

    def onRemoteError(self, code, message, request_info):
        self.status.setText("Server Error or Invalid Response: ERROR " + code + " - " + message)


class EchoServicePHP(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "services/EchoService.php", ["echo", "reverse", "uppercase", "lowercase"])


class EchoServicePython(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/services/EchoService.py", ["echo", "reverse", "uppercase", "lowercase"])
