"""
The ``ui.HTMLPanel`` class allows you to include HTML within your application,
and embed other widgets inside the panel's contents by wrapping them inside a
``&lt;span&gt;`` tag.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.Label import Label

class HtmlPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        id1 = HTMLPanel.createUniqueId(self)
        id2 = HTMLPanel.createUniqueId(self)

        panel = HTMLPanel('<b>This is some HTML</b><br>' +
                          'First widget:<span id="' + id1 + '"></span><br>' +
                          'Second widget:<span id="' + id2 + '"></span><br>' +
                          'More <i>HTML</i>')

        panel.add(Button("Hi there"), id1)
        panel.add(Label("This label intentionally left blank"), id2)

        self.add(panel)

