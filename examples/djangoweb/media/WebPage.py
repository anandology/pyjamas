import pyjd

from pyjamas.ui.Label import Label
from pyjamas.ui.HTML import HTML
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.Hidden import Hidden
from pyjamas.ui.Button import Button
from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.Composite import Composite
from pyjamas.ui import KeyboardListener
from pyjamas.ui import HasAlignment

from pyjamas.JSONService import JSONProxy

from pyjamas.Timer import Timer
from RichTextEditor import RichTextEditor

from pyjamas import Window
from pyjamas import History

class HTMLDialog(DialogBox):
    def __init__(self, name, html):
        DialogBox.__init__(self)
        self.setText(name)

        closeButton = Button("Close", self)

        htp = HTMLPanel(html)
        self.sp = ScrollPanel(htp)

        dock = DockPanel()
        dock.setSpacing(4)

        dock.add(closeButton, DockPanel.SOUTH)
        dock.add(self.sp, DockPanel.CENTER)

        dock.setCellHorizontalAlignment(closeButton, HasAlignment.ALIGN_RIGHT)
        dock.setCellWidth(self.sp, "100%")
        dock.setWidth("100%")
        self.setWidget(dock)

    def setWidth(self, width):
        DialogBox.setWidth(self, "%dpx" % width)
        self.sp.setWidth("%dpx" % (width-20))

    def setHeight(self, height):
        DialogBox.setHeight(self, "%dpx" % height)
        self.sp.setHeight("%dpx" % (height-65))

    def onClick(self, sender):
        self.hide()

class WebPageEdit(Composite):
    def __init__(self):
        Composite.__init__(self)

        self.remote = DataService()
        panel = VerticalPanel(Width="100%")

        self.view = Button("View", self)
        self.new = Button("New", self)
        self.todoId = None
        self.todoTextName = TextBox()
        self.todoTextName.addKeyboardListener(self)

        self.todoTextArea = RichTextEditor()
        self.todoTextArea.setWidth("100%")
        self.todoTextArea.addSaveListener(self)

        self.todoList = ListBox()
        self.todoList.setVisibleItemCount(7)
        self.todoList.setWidth("200px")
        self.todoList.addClickListener(self)

        self.status = HTML()
        panel.add(self.status)
        panel.add(Label("Add New Page:"))
        panel.add(self.todoTextName)
        panel.add(Label("New Page HTML:"))
        panel.add(self.todoTextArea)
        panel.add(Label("Click to Edit:"))
        panel.add(self.todoList)
        panel.add(self.view)
        panel.add(self.new)

        self.setWidget(panel)

        self.remote.getPages(self)

    def onKeyUp(self, sender, keyCode, modifiers):
        pass

    def onKeyDown(self, sender, keyCode, modifiers):
        pass

    def onSave(self, editor):
        self.status.setText("")
        name = self.todoTextName.getText()
        if not name:
            self.status.setText("Please enter a name for the page")
            return
        item = {
            'name': name,
            'text': self.todoTextArea.getHTML()
           }
        if self.todoId is None:
            rid = self.remote.addPage(item, self)
        else:
            item['id'] = self.todoId
            rid = self.remote.updatePage(item, self)

        if rid<0:
            self.status.setHTML("Server Error or Invalid Response")
            return

    def onKeyPress(self, sender, keyCode, modifiers):
        """
        This functon handles the onKeyPress event, and will add the item in the text box to the list when the user presses the enter key.  In the future, this method will also handle the auto complete feature.
        """
        pass


    def onClick(self, sender):
        if sender == self.new:
            self.todoId = None
            self.todoTextName.setText('')
            self.todoTextArea.setHTML('')
            return
        elif sender == self.view:
            name = self.todoTextName.getText()
            html = self.todoTextArea.getHTML()
            if not html:
                return
            p = HTMLDialog(name, html)
            p.setPopupPosition(10, 10)
            p.setWidth(Window.getClientWidth()-40)
            p.setHeight(Window.getClientHeight()-40)
            p.show()
            return

        id = self.remote.getPage(sender.getValue(sender.getSelectedIndex()),self)
        if id<0:
            self.status.setHTML("Server Error or Invalid Response")

    def onRemoteResponse(self, response, request_info):
        self.status.setHTML("response received")
        if request_info.method == 'getPage':
            self.status.setHTML(self.status.getText() + "HERE!")
            item = response[0]
            self.todoId = item['pk']
            self.todoTextName.setText(item['fields']['name'])
            self.todoTextArea.setHTML(item['fields']['text'])

        elif (request_info.method == 'getPages' or 
              request_info.method == 'addPage' or 
              request_info.method == 'deletePage'):
            self.status.setHTML(self.status.getText() + "HERE!")
            self.todoList.clear()
            for task in response:
                self.todoList.addItem(task['fields']['name'])
                self.todoList.setValue(self.todoList.getItemCount()-1,
                                       str(task['pk']))

        else:
            self.status.setHTML(self.status.getText() + "none!")

    def onRemoteError(self, code, message, request_info):
        self.status.setHTML("Server Error or Invalid Response: ERROR " + str(code) + " - " + str(message))

class WebApp:
    def onModuleLoad(self):

        #Show the initial screen.
        initToken = History().getToken()
        if len(initToken):
            if initToken == 'admin':
                RootPanel().add(WebPageEdit())
                return
        else:
            initToken = 'index'

        self.htp = HTMLPanel()
        self.remote = DataService()
        self.onHistoryChanged(initToken)
        RootPanel().add(self.htp)
        self.htp.setWidth("100%")

    def onHistoryChanged(self, token):
        self.remote.getPageByName(token, self)

    def onRemoteResponse(self, response, request_info):
        if (request_info.method == 'getPageByName' or
           request_info.method == 'getPage'):
            item = response[0]
            Window.setTitle(item['fields']['name'])
            self.htp.setHTML(item['fields']['text'])

    def onRemoteError(self, code, message, request_info):
        self.htp.setHTML("Server Error or Invalid Response: ERROR " + str(code) + " - " + str(message))


class DataService(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/services/",
                 ["getPage", "updatePage",
                  "getPages", "addPage",
                  "getPageByName",
                  "deletePage"])

if __name__ == "__main__":
    pyjd.setup("http://127.0.0.1:8000/site_media/WebPage.html")

    app = WebApp()
    app.onModuleLoad()
    pyjd.run()

