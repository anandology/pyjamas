from pyjamas.ui import RootPanel, TextBox, HTML, Button
from pyjamas import Window

import jsrecttest.js # YUK!!!

class Rect:
    def __init__(self, x, y):
        JS("""
           this.rect = new rectobj();
           this.rect.init(x, y);
           """)

    def add(self, r):
        JS("""
            this.rect.add(r.rect);
           """)
    def area(self):
        JS("""
            return this.rect.area();
           """)

    def get_x(self):
        JS("""
            return this.rect.x;
            """)

    def get_y(self):
        JS("""
            return this.rect.y;
            """)

class TestRect:

    def onModuleLoad(self):

        self.r = Rect(0.0, 0.0)

        self.xbox = TextBox()
        self.ybox = TextBox()
        self.addbutton = Button("Click to add x and y to Rectangle")
        self.addbutton.addClickListener(self)

        self.xbox.setText("2")
        self.ybox.setText("5")

        RootPanel().add(HTML("X Value:"))
        RootPanel().add(self.xbox)
        RootPanel().add(HTML("Y Value:"))
        RootPanel().add(self.ybox)
        RootPanel().add(self.addbutton)

        RootPanel().add(HTML("Current value: %d %d" % ( self.r.get_x(), self.r.get_y())))

    def onClick(self, sender):

        x = int(self.xbox.getText())
        y = int(self.ybox.getText())

        r = Rect(x, y)

        self.r.add(r)

        RootPanel().add(HTML("New value: %d %d" % ( self.r.get_x(), self.r.get_y())))
        RootPanel().add(HTML("New Area: " + self.r.area()))

