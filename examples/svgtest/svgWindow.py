# Copyright (C) 2009 Johan Wouters

from pyjamas import DOM
from pyjamas.ui.FocusWidget import FocusWidget
from pyjamas.ui.HTML import HTML
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Frame import Frame


class svgWindow(FocusWidget):
  def __init__(self, className=None):
    element = DOM.createIFrame()
    FocusWidget.__init__(self,element)

    self.floorplan_file = "floorplan.svg"


    #DOM.setStyleAttribute(element, "position", "relative")
    #DOM.setStyleAttribute(element, "overflow", "hidden")
    #DOM.setStyleAttribute(element, "border", "1px")
    #DOM.setStyleAttribute(element, "width", "100px")
    #DOM.setStyleAttribute(element, "height", "100px")
    #DOM.setStyleAttribute(element, "backgroundColor", "lightblue")

    self.svg_area = element
    self.rot_deg = 0.0
    self.scale = 1.0
    self.x_translate = 0.0
    self.y_translate = 0.0

    self.draw_elements()
    self.svg_area.setAttribute("class", className)

  def apply_transform(self):
    rot_string = "rotate(%f)" % self.rot_deg
    scale_string = "scale(%f)" % self.scale
    translate_string = "translate(%f," % self.x_translate
    translate_string+= "%f)" % self.y_translate

    transform_string = rot_string
    transform_string = transform_string + " " + scale_string
    transform_string = transform_string + " " + translate_string

    svg_g = self.svg_area.contentDocument.getElementById("svg_transform_element")
    RootPanel().add(HTML("transform_string = %s" % transform_string))
    transform = svg_g.getAttribute("transform")
    svg_g.setAttribute("transform", transform_string)

  def scale(self, scale):
    self.scale = scale
    self.apply_transform()

  def rotate(self, degrees):
    self.rot_deg = degrees
    self.apply_transform()

  def translate(self, x, y):
    self.x_translate = x
    self.y_translate = y
    self.apply_transform()

  def reset_transforms(self):
    self.rot_deg = 0.0
    self.scale = 1.0
    self.x_translate = 0.0
    self.y_translate = 0.0
    self.apply_transform()

  # Convenience functions
  def zoom_in(self):
    self.scale+=0.5
    self.apply_transform()

  def zoom_out(self):
    self.scale-=0.5
    self.apply_transform()

  def rot_CW(self):
    self.rot_deg+=30
    self.apply_transform()

  def rot_CCW(self):
    self.rot_deg-=30
    self.apply_transform()

  def change_floorplan(self):
    if self.floorplan_file == "floorplan.svg":
      self.floorplan_file = "floorplan2.svg"
    else:
      self.floorplan_file = "floorplan.svg"

    self.svg_area.setAttribute("src",self.floorplan_file)

  def draw_elements(self):
    # Some dummy stuff to get an SVG

    svg_method = 2

    if(svg_method == 0):
      DOM.setInnerHTML(self.svg_area, '''
    <object data="floorplan.svg" type="image/svg+xml width="100%" height="100%" />
      ''')
    elif(svg_method == 1):
      DOM.setInnerHTML(self.svg_area, '''
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid slice" id="the_svg" >
  <g id="svg_transform_element" transform="">
    <circle  id="thedot" cx="50" cy="50" r="10" fill="red" />
    <polygon id="triangle" points="2,20 22,20 12,40" fill="black" stroke="blue" stroke-width="1" />
  </g>
</svg>
      ''')
    elif(svg_method == 2):
      self.svg_area.setAttribute("src",self.floorplan_file)


    DOM.setAttribute(self.svg_area,"id","my_div_svg_area")
