""" Showcase.py

    A simply Pyjamas application that showcases the various widgets and panels
    defined by the 'ui' module.
"""
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Tree import Tree
from pyjamas.ui.TreeItem import TreeItem
from pyjamas.ui.VerticalPanel import VerticalPanel

from pyjamas import Window
from pyjamas import DOM

import demoInfo

import uiHelpers

#############################################################################

class Showcase:
    """ Our main application object.
    """
    def onModuleLoad(self):
        """ Dynamically build our user interface when the web page is loaded.
        """
        self._root        = RootPanel()
        self._tree        = Tree()
        self._rightPanel  = SimplePanel()
        self._curContents = None

        intro = HTML('<h3>Welcome to the Pyjamas User Interface Showcase</h3>'+
                     '<p/>Please click on an item to start.')

        self._introPanel = VerticalPanel()
        self._introPanel.add(uiHelpers.indent(intro, left=20))

        self._demos = [] # List of all installed demos.  Each item in this list
                         # is a dictionary with the following entries:
                         #
                         #     'name'
                         #
                         #         The name for this demo.
                         #
                         #     'section'
                         #
                         #         The name of the section of the demo tree
                         #         this demo should be part of.
                         #
                         #     'doc'
                         #
                         #         The documentation for this demo.
                         #
                         #     'src'
                         #
                         #         The source code for this demo.
                         #
                         #     'example'
                         #
                         #         The Panel which holds the example output for
                         #         this demo.

        self.loadDemos()
        self.buildTree()

        self._tree.setSize("0%", "100%")

        divider = VerticalPanel()
        divider.setSize("1px", "100%")
        divider.setBorderWidth(1)

        scroller = ScrollPanel(self._rightPanel)
        scroller.setSize("100%", "100%")

        hPanel = HorizontalPanel()
        hPanel.setSpacing(4)

        hPanel.add(self._tree)
        hPanel.add(divider)
        hPanel.add(scroller)

        hPanel.setHeight("100%")
        self._root.add(hPanel)

        self._tree.addTreeListener(self)
        self.showDemo(None)


    def loadDemos(self):
        """ Load our various demos, in preparation for showing them.

            We insert the demos into self._demos.
        """
        self._demos = demoInfo.getDemos()


    def buildTree(self):
        """ Build the contents of our tree.

            Note that, for now, we highlight the demos which haven't been
            written yet.
        """
        sections = {} # Maps section name to TreeItem object.

        for demo in self._demos:
            if demo['section'] not in sections:
                section = TreeItem('<b>' + demo['section'] + '</b>')
                DOM.setStyleAttribute(section.getElement(),
                                      "cursor", "pointer")
                DOM.setAttribute(section.itemTable, "cellPadding", "0")
                DOM.setAttribute(section.itemTable, "cellSpacing", "1")
                self._tree.addItem(section)
                sections[demo['section']] = section

            section = sections[demo['section']]

            if demo['doc'][:26] == "Documentation goes here...":
                item = TreeItem('<font style="color:#808080">' +
                                demo['title'] + '</font>')
            else:
                item = TreeItem(demo['title'])
            DOM.setStyleAttribute(item.getElement(), "cursor", "pointer")
            DOM.setAttribute(item.itemTable, "cellPadding", "0")
            DOM.setAttribute(item.itemTable, "cellSpacing", "1")
            item.setUserObject(demo)
            section.addItem(item)

        # Open the branches of the tree.

        for section in sections.keys():
            sections[section].setState(True, fireEvents=False)


    def onTreeItemSelected(self, item):
        """ Respond to the user selecting an item in our tree.
        """
        demo = item.getUserObject()
        if demo is None:
            self.showDemo(None)
        else:
            self.showDemo(demo['name'])


    def onTreeItemStateChanged(self, item):
        """ Respond to the user opening or closing a branch of the tree.
        """
        pass # Nothing to do.


    def showDemo(self, name):
        """ Show the demonstration with the given name.
        """
        if self._curContents is not None:
            self._rightPanel.remove(self._curContents)
            self._curContents = None

        demo = None
        for d in self._demos:
            if d['name'] == name:
                demo = d
                break

        if demo is not None:
            exampleID = HTMLPanel.createUniqueId()

            html = []
            html.append('<div style="padding:20px">')
            html.append('<b>' + demo['title'] + '</b>')
            html.append('<p/>')
            html.append(self.docToHTML(demo['doc']))
            html.append('<p/>')
            html.append('<hr/>')
            html.append('<b>Working Example</b>')
            html.append('<p/>')
            html.append('<div style="padding-left:20px">')
            html.append('<span id="' + exampleID + '"></span>')
            html.append('</div>')
            html.append('<p/>')
            html.append('<hr/>')
            html.append('<b>Source Code</b>')
            html.append('<p/>')
            html.append(self.srcToHTML(demo['src']))
            html.append('</div>')

            panel = HTMLPanel("\n".join(html))
            panel.add(demo['example'], exampleID)

            self._rightPanel.add(panel)
            self._curContents = panel
        else:
            self._rightPanel.add(self._introPanel)
            self._curContents = self._introPanel


    def docToHTML(self, doc):
        """ Convert the given documentation string to HTML.
        """
        doc = doc.replace('\n\n', '<p/>')

        isBold = False
        while True:
            i = doc.find("``")
            if i == -1: break
            if isBold:
                doc = doc[:i] + '</b></font>' + doc[i+2:]
            else:
                doc = doc[:i] + '<font face="monospace"><b>' + doc[i+2:]
            isBold = not isBold

        return doc


    def srcToHTML(self, src):
        """ Convert the given source code to HTML.

            The source code is already in HTML format, but has extra tags to
            make it a complete HTML file.  We extract and return just the text
            between the <body> tags.
        """
        i = src.find('<body')
        i = src.find('>', i)
        j = src.find('</body>')
        return src[i+1:j]



if __name__ == '__main__':
    app = Showcase()
    app.onModuleLoad()
