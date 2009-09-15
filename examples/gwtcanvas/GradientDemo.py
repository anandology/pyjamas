"""
* Copyright 2008 Google Inc.
* Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
*
* Licensed under the Apache License, Version 2.0 (the "License"); you may not
* use this file except in compliance with the License. You may obtain a copy of
* the License at
*
* http:#www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
* License for the specific language governing permissions and limitations under
* the License.
"""


from pyjamas.ui.Composite import Composite
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel

from pyjamas.Canvas.Color import Color


from SimpleCanvasDemo import SimpleCanvasDemo

class GradientDemoControls (Composite):
    def __init__(self):
        layout = VerticalPanel()
        layout.add(HTML(
        "<b style=\"color:#f00;\">Gradients currently not working correctly in IE. Contributor assistance welcome :).</b>"))
        Composite.__init__(self, layout)
    


"""*
* Simple Demo of gradient fills and strokes.
"""
class GradientDemo (SimpleCanvasDemo):
    
    def __init__(self, theCanvas):
        SimpleCanvasDemo.__init__(self, theCanvas)

        self.width = 400
        self.height = 400
        self.demoName = "Gradients"
    
    
    def createControls(self):
        self.controls = GradientDemoControls()
    
    
    def drawDemo(self):
        self.canvas.resize(self.width, self.height)
        
        # DRAW SOME LINEAR GRADIENTS
        # Demos ported from Mozilla Development Center Canvas Tutorial
        self.canvas.saveContext()
        
        # Create gradients
        lingrad = self.canvas.createLinearGradient(0, 0, 0, 150)
        lingrad.addColorStop(0.0, Color("#00ABEB"))
        lingrad.addColorStop(0.5, Color("#fff"))
        lingrad.addColorStop(0.5, Color("#26C000"))
        lingrad.addColorStop(1, Color("#fff"))
        
        lingrad2 = self.canvas.createLinearGradient(0, 50, 0, 95)
        lingrad2.addColorStop(0.5, Color("#000"))
        lingrad2.addColorStop(1, Color("rgba(0,0,0,0)"))
        
        # assign gradients to fill and stroke styles
        self.canvas.setFillStyle(lingrad)
        self.canvas.setStrokeStyle(lingrad2)
        
        # draw shapes
        self.canvas.fillRect(10, 10, 130, 130)
        self.canvas.strokeRect(50, 50, 50, 50)
        
        self.canvas.restoreContext()
        
        # DRAW SOME RADIAL GRADIENTS
        # Demos ported from Mozilla Development Center Canvas Tutorial
        self.canvas.saveContext()
        self.canvas.translate(150, 150)
        
        radgrad = self.canvas.createRadialGradient(45, 45, 10, 52, 50, 30)
        radgrad.addColorStop(0, Color("#A7D30C"))
        radgrad.addColorStop(0.9, Color("#019F62"))
        radgrad.addColorStop(1, Color("rgba(1,159,98,0)"))
        
        radgrad2 = self.canvas.createRadialGradient(105, 105, 20, 112, 120, 50)
        radgrad2.addColorStop(0, Color("#FF5F98"))
        radgrad2.addColorStop(0.75, Color("#FF0188"))
        radgrad2.addColorStop(1, Color("rgba(255,1,136,0)"))
        
        radgrad3 = self.canvas.createRadialGradient(95, 15, 15, 102, 20, 40)
        radgrad3.addColorStop(0, Color("#00C9FF"))
        radgrad3.addColorStop(0.8, Color("#00B5E2"))
        radgrad3.addColorStop(1, Color("rgba(0,201,255,0)"))
        
        radgrad4 = self.canvas.createRadialGradient(0, 150, 50, 0, 140, 90)
        radgrad4.addColorStop(0, Color("#F4F201"))
        radgrad4.addColorStop(0.8, Color("#E4C700"))
        radgrad4.addColorStop(1, Color("rgba(228,199,0,0)"))
        
        # draw shapes
        self.canvas.setFillStyle(radgrad4)
        self.canvas.fillRect(0, 0, 150, 150)
        self.canvas.setFillStyle(radgrad3)
        self.canvas.fillRect(0, 0, 150, 150)
        self.canvas.setFillStyle(radgrad2)
        self.canvas.fillRect(0, 0, 150, 150)
        self.canvas.setFillStyle(radgrad)
        self.canvas.fillRect(0, 0, 150, 150)
        
        self.canvas.restoreContext()
    
    
    def stopDemo(self):
        pass
    


