""" testint our demo slider
"""

from pyjamas.ui.Label      import Label
from pyjamas.ui.Button     import Button
from pyjamas.ui.ButtonBase import ButtonBase
from pyjamas.ui.RootPanel  import RootPanel
from pyjamas.ui.CustomButton import CustomButtom
from pyjamas.ui.ToggleButton import ToggleButton
from pyjamas               import DOM


class Toggle:
    def onModuleLoad(self):
        
        self.label = Label("Not set yet")
        
        self.button = Button("Probe button", self)
        self.toggle = ToggleButton("up","down")
        RootPanel().add(self.label)
        RootPanel().add(self.button)
        RootPanel().add(self.toggle)
        self.i = 0
        
    def onClick(self, sender):
        if sender == self.button:
            if self.i: 
                self.i = 0
                self.toggle.setCurrentFace(self.toggle.getUpFace())
            else:
                self.i = 1
                self.toggle.setCurrentFace(self.toggle.getDownFace())
            self.label.setText("self.toggle.style_name: "+
                                self.toggle.style_name+", self.toggle.getStyleName():"+
                                self.toggle.getStyleName()+" ")


if __name__ == "__main__":
    app = Toggle()
    app.onModuleLoad()



