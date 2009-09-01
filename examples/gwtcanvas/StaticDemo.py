"""
* Copyright 2008 Google Inc.
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

import math

from pyjamas.ui.Composite import Composite
from pyjamas.ui.VerticalPanel import VerticalPanel

from pyjamas.Canvas import Color

from SimpleCanvasDemo import SimpleCanvasDemo


# All SimpleCanvasDemos need to set some controls
# Even if they don't have any :).
class StaticDemoControls(Composite):
    def __init__(self):
        Composite.__init__(self, VerticalPanel())

"""*
* Demo that showcases most of the GWTCanvas drawing Api,
* as well as transformations, and style settings.
"""
class StaticDemo (SimpleCanvasDemo):
    
    def __init__(self, theCanvas):
        SimpleCanvasDemo.__init__(self, theCanvas)
        self.width = 400
        self.height = 400
        self.demoName = "Static Scene"
    
    
    def createControls(self):
        self.controls = StaticDemoControls()
    
    
    """
    * Test cases derived from javascript test cases by Emil Eklund
    * and from Mozilla foundation Canvas tutorial. Please note that
    * his test cases are NOT bound by license since they were
    * originally derived from mozilla foundation test cases
    """
    def drawDemo(self):
        
        self.canvas.resize(self.width, self.height)
        
        # Changing the coordinate size will implicitly clear the self.canvas
        # self.canvas.clear()
        self.canvas.saveContext()
        
        self.canvas.setLineWidth(1)
        self.canvas.setFillStyle(Color.GREEN)
        self.canvas.fillRect(5, 5, 25, 25)
        self.canvas.setStrokeStyle(Color.RED)
        self.canvas.strokeRect(20, 20, 25, 25)
        
        self.canvas.beginPath()
        
        self.canvas.setLineWidth(1)
        
        self.canvas.moveTo(1,1)
        self.canvas.lineTo(80,80)
        self.canvas.lineTo(100,20)
        self.canvas.closePath()
        self.canvas.stroke()
        
        self.canvas.setStrokeStyle(Color.BLUE)
        self.canvas.setFillStyle(Color.BLACK)
        
        self.canvas.beginPath()
        self.canvas.moveTo(120,50)
        self.canvas.lineTo(150,70)
        self.canvas.lineTo(150,50)
        
        self.canvas.quadraticCurveTo(150, 150, 80, 80)
        self.canvas.cubicCurveTo(85,25,75,37,75,40)
        self.canvas.closePath()
        self.canvas.fill()
        
        self.canvas.beginPath()
        self.canvas.rect(180,180,80,80)
        self.canvas.rect(200,200,80,80)
        self.canvas.stroke()
        
        self.canvas.beginPath()
        self.canvas.arc(200, 100, 20, 0,  math.pi, False)
        self.canvas.stroke()
        
        self.canvas.saveContext()
        self.canvas.translate(150, 0)
        
        self.canvas.fillRect(0,0,150,150)
        self.canvas.setFillStyle(Color("#09F"))
        self.canvas.fillRect(15,15,120,120)
        self.canvas.setFillStyle(Color("#FFF"))
        self.canvas.setGlobalAlpha(0.5)
        self.canvas.fillRect(30,30,90,90)
        self.canvas.fillRect(45,45,60,60)
        self.canvas.fillRect(60,60,30,30)
        
        self.canvas.restoreContext()
        self.canvas.saveContext()
        self.canvas.translate(10, 140)
        
        self.canvas.setFillStyle(Color("#FD0"))
        self.canvas.fillRect(0,0,75,75)
        self.canvas.setFillStyle(Color("#6C0"))
        self.canvas.fillRect(75,0,75,75)
        self.canvas.setFillStyle(Color("#09F"))
        self.canvas.fillRect(0,75,75,75)
        self.canvas.setFillStyle(Color("#F30"))
        self.canvas.fillRect(75,75,75,75)
        self.canvas.setFillStyle(Color("#FFF"))
        
        self.canvas.setGlobalAlpha(0.2)
        
        for i in range(7):
            self.canvas.beginPath()
            self.canvas.arc(75, 75, 10 + (10 * i), 0,  math.pi * 2, False)
            self.canvas.fill()
        
        
        self.canvas.saveContext()
        self.canvas.setGlobalAlpha(0.8)
        self.canvas.beginPath()
        self.canvas.arc(75,75,50,0, math.pi * 2,True); # Outer circle
        self.canvas.moveTo(110,75)
        self.canvas.arc(75,75,35,0, math.pi,False);   # Mouth
        self.canvas.moveTo(65,65)
        self.canvas.arc(60,65,5,0, math.pi * 2,True);  # Left eye
        self.canvas.moveTo(95,65)
        self.canvas.arc(90,65,5,0, math.pi * 2,True);  # Right eye
        self.canvas.stroke()
        self.canvas.restoreContext()
        
        self.canvas.restoreContext()
        
        self.canvas.beginPath()
        self.canvas.arc(200, 200, 20, 0, math.pi * 2, False)
        self.canvas.stroke()
        
        self.canvas.saveContext()
        self.canvas.setGlobalAlpha(1.0)
        
        for i in range(6):
            # Loop through rings (from inside to out)
            self.canvas.saveContext()
            self.canvas.setFillStyle(Color((51 * i),(255 - 51 * i),255))
            
            for j in range(i*6):
                # draw individual dots
                self.canvas.rotate(math.pi * 2 / ( i * 6.))
                self.canvas.beginPath()
                
                self.canvas.rect(0, i * 12.5,5,5)
                self.canvas.fill()
            
            
            self.canvas.restoreContext()
        
        
        self.canvas.restoreContext()
        
        self.canvas.restoreContext()
        # self.canvas.clear()
    
    
    def stopDemo(self):
        # This demo is not animated so this is a no-op
        pass
    
    


