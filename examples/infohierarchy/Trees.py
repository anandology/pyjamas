from pyjamas.ui.Tree import Tree
from pyjamas.ui.TreeItem import TreeItem
from pyjamas.ui.Composite import Composite
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas import Window

from pyjamas.JSONService import JSONProxy

class Trees(Composite):
    def __init__(self):
        Composite.__init__(self)

        self.fProto = []
        self.fTree = Tree()
        
        self.fTree.addTreeListener(self)
        self.initWidget(self.fTree)
        self.remote = InfoServicePython()
        self.remote.index("", 1, self)
        
    def protoise_tree(self, data):

        res = []
        for i in range(len(data)):
            d = data[i]
            name = d[0]
            children = d[1]

            res.append(Proto(name, self.protoise_tree(children)))
        return res

    def create_tree(self, data):

        self.fProto = self.protoise_tree(data)
        
        for i in range(len(self.fProto)):
            p = self.fProto[i]
            p.pathify()
            self.createItem(p)
            self.fTree.addItem(p.item)

    def onRemoteResponse(self, response, request_info):
        if request_info.method == "index":
            self.create_tree(response)

    def onRemoteError(self, code, message, request_info):
        RootPanel().add(HTML("Server Error or Invalid Response: ERROR " + code + " - " + message))

    def onTreeItemSelected(self, item):
        pass
    
    def onTreeItemStateChanged(self, item):
        child = item.getChild(0)
        if hasattr(child, "isPendingItem"):
            item.removeItem(child)
        
            proto = item.getUserObject()
            for i in range(len(proto.children)):
                self.createItem(proto.children[i])
                item.addItem(proto.children[i].item)

    def createItem(self, proto):
        proto.item = TreeItem(proto.text)
        proto.item.setUserObject(proto)
        if len(proto.children) > 0:
            proto.item.addItem(PendingItem())


class Proto:
    def __init__(self, text, children=None):
        self.children = []
        self.item = None
        self.text = text
        self.root = '/'
        
        if children is not None:
            self.children = children

    def pathify(self):
        """ cascade setup of full path
        """

        for c in self.children:
            c.root = self.root + self.text + "/"
            c.pathify()


class PendingItem(TreeItem):
    def __init__(self):
        TreeItem.__init__(self, "Please wait...")

    def isPendingItem(self):
        return True


class InfoServicePython(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/infoservice/EchoService.py",
                                    ["index"])


