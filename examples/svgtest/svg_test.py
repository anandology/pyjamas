# Copyright (C) 2009 Johan Wouters

import pyjd

from svgWindow import svgWindow
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Button import Button
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas import Window


class mainUI:
  svg = None

  def __init__(self):
    svg = svgWindow(className="svg") # className for CSS
    mainUI.svg = svg

    RootPanel().add(svg)

    panel = HorizontalPanel()
    RootPanel().add(panel)

    buttons = ["zoom in",
               "zoom out",
               "rotate CW",
               "rotate CCW",
               "reload",
               "reset",
                 ]
    for buttonName in buttons:
      newButton = Button(buttonName, listener=self.clickListener)
      panel.add(newButton)

    RootPanel().add(HTML("Hello <b>World</b>"))

  def clickListener(self, e):
    button = e.getText()
    if button=="zoom in":
      mainUI.svg.zoom_in()
    elif button=="zoom out":
      mainUI.svg.zoom_out()
    elif button=="rotate CW":
      mainUI.svg.rot_CW()
    elif button=="rotate CCW":
      mainUI.svg.rot_CCW()
    elif button=="reset":
      mainUI.svg.reset_transforms()
    elif button=="reload":
      mainUI.svg.change_floorplan()

if __name__ == "__main__":
  pyjd.setup("./public/svg_test.html")
  ui = mainUI()
  pyjd.run()

