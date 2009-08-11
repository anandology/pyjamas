from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Button import Button
from __pyjamas__ import JS

import jsdicttest.js # YUK!!!

class WrapperDict:
    def __init__(self):
        d = {'hello': 'world',
             'goodbye': 2}
        JS("""
           self.dict = new dictobj();
           """)
        self.dict.init(d)

    def python_get_value(self, key):
        return self.dict.d[key]

    def python_dict_length(self):
        return len(self.dict)

    def javascript_get_value(self, key):
        return self.dict.get_value(key)


class TestDict:

    def onModuleLoad(self):

        self.r = WrapperDict()

        self.kbox = TextBox()
        self.addbutton = Button("Click to look up key value (hello or goodbye)")
        self.addbutton.addClickListener(self)

        self.kbox.setText("hello") # default to make life easier

        RootPanel().add(HTML("Key:"))
        RootPanel().add(self.kbox)
        RootPanel().add(self.addbutton)

    def display_value(self):

        key = self.kbox.getText()

        RootPanel().add(HTML("Value using python:" ))
        RootPanel().add(HTML(self.r.python_get_value(key)))
        RootPanel().add(HTML("Value using javascript:" ))
        RootPanel().add(HTML(self.r.javascript_get_value(key)))

    def onClick(self, sender):

        self.display_value()



if __name__ == '__main__':
    app = TestDict()
    app.onModuleLoad()
