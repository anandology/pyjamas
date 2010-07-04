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

import math

from pyjamas.Timer import Timer
from pyjamas.ui.Button import Button
from pyjamas.ui.Composite import Composite
from pyjamas.ui import HasAlignment
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Widget import Widget

from pyjamas.Canvas import Color
from pyjamas.Canvas import GWTCanvasConsts

import time

from SimpleCanvasDemo import SimpleCanvasDemo




class SuiteDemoControls (Composite):
    def __init__(self, chart):
        self.chart = chart
        self.canvas = chart.canvas
        
        self.b2 = Button("Compositing", self)
        self.b3 = Button("Paths & shapes", self)
        self.b4 = Button("Arcs & circles", self)
        self.b1 = Button("Bezier curves", self)
        self.b6 = Button("Colors", self)
        self.b7 = Button("Translating", self)
        self.b8 = Button("Scaling", self)
        self.b5 = Button("Rotating", self)
        self.b10 = Button("Transparency", self)
        self.b11 = Button("Lines", self)
        self.b9 = Button("Animations", self)
        
        hp = HorizontalPanel()
        vp = VerticalPanel()
        vp.setHorizontalAlignment(HasAlignment.ALIGN_LEFT)
        vp.add(Label("MENU"))
        vp.setSpacing(6)
        vp.add(self.b2)
        vp.add(self.b3)
        vp.add(self.b4)
        vp.add(self.b1)
        vp.add(self.b6)
        vp.add(self.b7)
        vp.add(self.b8)
        vp.add(self.b5)
        vp.add(self.b10)
        vp.add(self.b11)
        vp.add(self.b9)
        hp.add(vp)
        
        Composite.__init__(self, hp)
    
    def onClick(self, sender):
        if sender == self.b2:
            self.onClickCompositing(sender)
        elif sender == self.b3:
            self.onClickPaths(sender)
        elif sender == self.b4:
            self.onClickArcs(sender)
        elif sender == self.b1:
            self.onClickBezier(sender)
        elif sender == self.b6:
            self.onClickColours(sender)
        elif sender == self.b7:
            self.onClickTranslate(sender)
        elif sender == self.b8:
            self.onClickScale(sender)
        elif sender == self.b5:
            self.onClickRotate(sender)
        elif sender == self.b11:
            self.onClickLines(sender)
        elif sender == self.b9:
            self.onClickClock(sender)
        elif sender == self.b10:
            self.onClickTrans(sender)

    # compositing
    def onClickCompositing(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(40, 40)
        self.canvas.setFillStyle(Color.Color("#f00"))
        self.canvas.fillRect(75, 50, 100, 100)
        self.canvas.setGlobalCompositeOperation(GWTCanvasConsts.DESTINATION_OVER)
        self.canvas.setFillStyle(Color.Color("#0f0"))
        self.canvas.fillRect(110, 110, 100, 100)
        self.canvas.setGlobalCompositeOperation(GWTCanvasConsts.SOURCE_OVER)
        self.canvas.setFillStyle(Color.Color("#00f"))
        self.canvas.fillRect(40, 85, 100, 100)
        self.canvas.restoreContext()
    
    # paths / shapes
    def onClickPaths(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(30, 30)
        self.canvas.setFillStyle(Color.Color("#fff"))
        self.canvas.setStrokeStyle(Color.Color("#fff"))
        self.canvas.beginPath()
        self.canvas.moveTo(25, 25)
        self.canvas.lineTo(105, 25)
        self.canvas.lineTo(25, 105)
        self.canvas.closePath()
        self.canvas.fill()
        self.canvas.beginPath()
        self.canvas.moveTo(125, 125)
        self.canvas.lineTo(125, 45)
        self.canvas.lineTo(45, 125)
        self.canvas.closePath()
        self.canvas.stroke()
        self.canvas.beginPath()
        self.canvas.moveTo(265, 265)
        self.canvas.lineTo(165, 265)
        self.canvas.lineTo(265, 165)
        self.canvas.lineTo(265, 265)
        self.canvas.fillRect(25, 165, 100, 100)
        self.canvas.setFillStyle(Color.BLACK)
        self.canvas.fillRect(45, 185, 60, 60)
        self.canvas.strokeRect(50, 190, 50, 50)
        self.canvas.rect(165, 25, 100, 100)
        self.canvas.stroke()
        self.canvas.restoreContext()
    
    # arcs / circles
    def onClickArcs(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(30, 70)
        self.canvas.setFillStyle(Color.Color("#f0f"))
        self.canvas.setStrokeStyle(Color.Color("#0ff"))
        self.canvas.setLineWidth(2)
        for i in range(4):
            for j in range(3):
                self.canvas.beginPath()
                x = 25 + j * 50
                y = 25 + i * 50
                radius = 20
                startAngle = 0
                endAngle =  (math.pi + (math.pi * j) / 2)
                anticlockwise = (i % 2 == 0) and False or True
                self.canvas.arc(x, y, radius, startAngle, endAngle, anticlockwise)
                if i > 1:
                    self.canvas.fill()
                else:
                    self.canvas.stroke()
                
            
        
        self.canvas.translate(160, 20)
        self.canvas.setStrokeStyle(Color.Color("#ff0"))
        self.canvas.setLineWidth(4)
        self.canvas.beginPath()
        self.canvas.arc(75, 75, 50, 0,  (math.pi * 2), True)
        self.canvas.moveTo(110, 75)
        self.canvas.arc(75, 75, 35, 0,  math.pi, False)
        self.canvas.moveTo(65, 65)
        self.canvas.arc(60, 65, 5, 0,  (math.pi * 2), True)
        self.canvas.moveTo(95, 65)
        self.canvas.arc(90, 65, 5, 0,  (math.pi * 2), True)
        self.canvas.stroke()
        self.canvas.restoreContext()
    
    # bezier
    def onClickBezier(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(30, 70)
        self.canvas.setFillStyle(Color.Color("#f00"))
        self.canvas.setStrokeStyle(Color.Color("#0f0"))
        self.canvas.setLineWidth(2)
        self.canvas.beginPath()
        self.canvas.moveTo(75, 25)
        self.canvas.quadraticCurveTo(25, 25, 25, 62.5)
        self.canvas.quadraticCurveTo(25, 100, 50, 100)
        self.canvas.quadraticCurveTo(50, 120, 30, 125)
        self.canvas.quadraticCurveTo(60, 120, 65, 100)
        self.canvas.quadraticCurveTo(125, 100, 125, 62.5)
        self.canvas.quadraticCurveTo(125, 25, 75, 25)
        self.canvas.stroke()
        self.canvas.translate(140, 0)
        self.canvas.beginPath()
        self.canvas.moveTo(75, 40)
        self.canvas.cubicCurveTo(75, 37, 70, 25, 50, 25)
        self.canvas.cubicCurveTo(20, 25, 20, 62.5, 20, 62.5)
        self.canvas.cubicCurveTo(20, 80, 40, 102, 75, 120)
        self.canvas.cubicCurveTo(110, 102, 130, 80, 130, 62.5)
        self.canvas.cubicCurveTo(130, 62.5, 130, 25, 100, 25)
        self.canvas.cubicCurveTo(85, 25, 75, 37, 75, 40)
        self.canvas.fill()
        self.canvas.restoreContext()
    
    # colours
    def onClickColours(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(20, 20)
        self.canvas.setFillStyle(Color.Color(255, 165, 0))
        self.canvas.setStrokeStyle(Color.Color("#FFA500"))
        for i in range(6):
            for j in range(6):
                self.canvas.setFillStyle(Color.Color(int (math.floor(255 - 42.5 * i)),
                                                     int(math.floor(255 - 42.5 * j)),
                                                     0))
                self.canvas.fillRect(j * 25, i * 25, 25, 25)
            
        
        self.canvas.translate(160, 160)
        for i in range(6):
            for j in range(6):
                self.canvas.setStrokeStyle(Color.Color(0,
                int( math.floor(255 - 42.5 * i)),
                int( math.floor(255 - 42.5 * j))))
                self.canvas.beginPath()
                self.canvas.arc(12.5 + j * 25, 12.5 + i * 25, 10, 0,
                                     (math.pi * 2), True)
                self.canvas.stroke()
            
        
        self.canvas.restoreContext()
    
    # translating
    def onClickTranslate(self, sender):
        self.chart.run = False
        
        color = [ Color.Color("#fc0"), Color.Color("#0cf"), Color.Color("#cf0") ]
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(25, 25)
        for i in range(3):
            for j in range(3):
                self.canvas.setStrokeStyle(color[j])
                self.canvas.saveContext()
                self.canvas.translate(50 + j * 100, 50 + i * 100)
                self.chart.drawSpirograph(2000, 20.0 * (j + 2) / (j + 1), -8.0 * (i + 3)
                / (i + 1), 10.0)
                self.canvas.restoreContext()
            
        
        self.canvas.restoreContext()
    
    # scaling
    def onClickScale(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(25, 25)
        self.canvas.setStrokeStyle(Color.Color("#fc0"))
        self.canvas.setLineWidth(1.5)
        self.canvas.saveContext()
        self.canvas.translate(50, 50)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.translate(100, 0)
        self.canvas.scale(0.75, 0.75)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.translate(133.333, 0)
        self.canvas.scale(0.75, 0.75)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.restoreContext()
        self.canvas.setStrokeStyle(Color.Color("#0cf"))
        self.canvas.saveContext()
        self.canvas.translate(50, 150)
        self.canvas.scale(1, 0.75)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.translate(100, 0)
        self.canvas.scale(1, 0.75)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.translate(100, 0)
        self.canvas.scale(1, 0.75)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.restoreContext()
        self.canvas.setStrokeStyle(Color.Color("#cf0"))
        self.canvas.saveContext()
        self.canvas.translate(50, 250)
        self.canvas.scale(0.75, 1)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.translate(133.333, 0)
        self.canvas.scale(0.75, 1)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.translate(177.777, 0)
        self.canvas.scale(0.75, 1)
        self.chart.drawSpirograph(2000, 22, 6, 5)
        self.canvas.restoreContext()
        self.canvas.restoreContext()
    
    # rotating
    def onClickRotate(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(175, 175)
        self.canvas.scale(1.6, 1.6)
        for i in range(1, 6):
            self.canvas.saveContext()
            self.canvas.setFillStyle(Color.Color("rgb(%d,%d,255)" % \
                                 (51 * i, 255 - 51 * i)))
            for j in range(i * 6):
                self.canvas.rotate( (math.pi * 2 / (i * 6)))
                self.canvas.beginPath()
                self.canvas.arc(0, i * 12.5, 5, 0,  (math.pi * 2), True)
                # self.canvas.rect(0,i*12.5,5,5)
                self.canvas.fill()
            
            self.canvas.restoreContext()
        
        self.canvas.restoreContext()
    
    # lines
    def onClickLines(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.scale(0.9, 0.9)
        self.canvas.translate(30, 40)
        self.canvas.saveContext()
        self.canvas.setStrokeStyle(Color.Color("#9CFF00"))
        for i in range(10):
            self.canvas.setLineWidth(1 + i)
            self.canvas.beginPath()
            self.canvas.moveTo(5 + i * 14, 5)
            self.canvas.lineTo(5 + i * 14, 140)
            self.canvas.stroke()
        
        self.canvas.restoreContext()
        self.canvas.saveContext()
        self.canvas.translate(0, 170)
        self.canvas.setStrokeStyle(Color.Color("#09f"))
        self.canvas.setLineWidth(2)
        self.canvas.beginPath()
        self.canvas.moveTo(10, 10)
        self.canvas.lineTo(140, 10)
        self.canvas.moveTo(10, 140)
        self.canvas.lineTo(140, 140)
        self.canvas.stroke()
        self.canvas.setStrokeStyle(Color.Color("#9CFF00"))
        self.canvas.setLineWidth(15)
        self.canvas.setLineCap(GWTCanvasConsts.BUTT)
        self.canvas.beginPath()
        self.canvas.moveTo(25, 10)
        self.canvas.lineTo(25, 140)
        self.canvas.stroke()
        self.canvas.setLineCap(GWTCanvasConsts.ROUND)
        self.canvas.beginPath()
        self.canvas.moveTo(75, 10)
        self.canvas.lineTo(75, 140)
        self.canvas.stroke()
        self.canvas.setLineCap(GWTCanvasConsts.SQUARE)
        self.canvas.beginPath()
        self.canvas.moveTo(125, 10)
        self.canvas.lineTo(125, 140)
        self.canvas.stroke()
        self.canvas.restoreContext()
        self.canvas.saveContext()
        self.canvas.translate(170, 0)
        self.canvas.setStrokeStyle(Color.Color("#9CFF00"))
        self.canvas.setLineWidth(10)
        self.canvas.setLineJoin(GWTCanvasConsts.ROUND)
        self.canvas.beginPath()
        self.canvas.moveTo(-5, 5)
        self.canvas.lineTo(35, 45)
        self.canvas.lineTo(75, 5)
        self.canvas.lineTo(115, 45)
        self.canvas.lineTo(155, 5)
        self.canvas.stroke()
        self.canvas.setLineJoin(GWTCanvasConsts.BEVEL)
        self.canvas.beginPath()
        self.canvas.moveTo(-5, 5 + 40)
        self.canvas.lineTo(35, 45 + 40)
        self.canvas.lineTo(75, 5 + 40)
        self.canvas.lineTo(115, 45 + 40)
        self.canvas.lineTo(155, 5 + 40)
        self.canvas.stroke()
        self.canvas.setLineJoin(GWTCanvasConsts.MITER)
        self.canvas.beginPath()
        self.canvas.moveTo(-5, 5 + 80)
        self.canvas.lineTo(35, 45 + 80)
        self.canvas.lineTo(75, 5 + 80)
        self.canvas.lineTo(115, 45 + 80)
        self.canvas.lineTo(155, 5 + 80)
        self.canvas.stroke()
        self.canvas.restoreContext()
        self.canvas.saveContext()
        self.canvas.translate(170, 170)
        self.canvas.setStrokeStyle(Color.Color("#09f"))
        self.canvas.setLineWidth(2)
        self.canvas.strokeRect(-5, 50, 160, 50)
        self.canvas.setStrokeStyle(Color.Color("#9CFF00"))
        self.canvas.setLineWidth(10)
        self.canvas.setMiterLimit(10)
        self.canvas.beginPath()
        self.canvas.moveTo(0, 100)
        for i in range(19):
            if i % 2 == 0:
                dy = 25.0
            else:
                dy = -25.0
            
            self.canvas.lineTo( (math.pow(i, 1.5) * 2.0), 75 + dy)
        
        self.canvas.stroke()
        self.canvas.restoreContext()
        self.canvas.restoreContext()
    
    # timer
    def onClickClock(self, sender):
        self.chart.run = True
        self.chart.drawClock()
    
    # transparency
    def onClickTrans(self, sender):
        self.chart.run = False
        
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(20, 180)
        self.canvas.setFillStyle(Color.Color("rgb(255,221,0)"))
        self.canvas.fillRect(0, 0, 150, 37.5)
        self.canvas.setFillStyle(Color.Color("rgb(102,204,0)"))
        self.canvas.fillRect(0, 37.5, 150, 37.5)
        self.canvas.setFillStyle(Color.Color("rgb(0,153,255)"))
        self.canvas.fillRect(0, 75, 150, 37.5)
        self.canvas.setFillStyle(Color.Color("rgb(255,51,0)"))
        self.canvas.fillRect(0, 112.5, 150, 37.5)
        for i in range(10):
            self.canvas.setFillStyle(Color.Color("rgba(255,255,255,%f)" %
                                                ((i + 1) / 10.0)))
            for j in range(4):
                self.canvas.fillRect(5 + i * 14.0, 5 + j * 37.5, 14, 27.5)
            
        
        self.canvas.restoreContext()
        self.canvas.saveContext()
        self.canvas.translate(180, 20)
        self.canvas.setGlobalAlpha(1.0)
        self.canvas.setFillStyle(Color.Color("#FD0"))
        self.canvas.fillRect(0, 0, 75, 75)
        self.canvas.setFillStyle(Color.Color("#6C0"))
        self.canvas.fillRect(75, 0, 75, 75)
        self.canvas.setFillStyle(Color.Color("#09F"))
        self.canvas.fillRect(0, 75, 75, 75)
        self.canvas.setFillStyle(Color.Color("#F30"))
        self.canvas.fillRect(75, 75, 75, 75)
        self.canvas.setFillStyle(Color.Color("#FFF"))
        self.canvas.setGlobalAlpha(0.2)
        for i in range(7):
            self.canvas.beginPath()
            self.canvas.arc(75, 75, 10 + (10 * i), 0,  (math.pi * 2), True)
            self.canvas.fill()
        
        self.canvas.restoreContext()
    
    
"""*
* Demo showcaseing a range of tests from the Mozilla Canvas Tutorial
* and from contributions from Oliver Zoran.
*
"""
class SuiteDemo (SimpleCanvasDemo):
    
    def __init__(self, theCanvas):
        SimpleCanvasDemo.__init__(self, theCanvas)
        self.width = 350
        self.height = 350
        self.demoName = "Feature Suite"
        self.run = False
    
    def createControls(self):
        self.controls = SuiteDemoControls(self)
    
    
    def drawDemo(self):
        self.canvas.resize(self.width, self.height)
        self.canvas.setBackgroundColor(Color.BLACK)
    
    
    def stopDemo(self):
        self.run = False
        self.canvas.setBackgroundColor(GWTCanvasConsts.TRANSPARENT)
    
    def getTimeSeconds(self):
        return time.time() % 60.0

    def getTimeMilliseconds(self):
        return (time.time() * 1000.0) % 1.0

    def getTimeMinutes(self):
        return (time.time() / 60) % 60.0

    def getTimeHours(self):
        return (time.time() / 3600) % 12.0

    def onTimer(self, tid):
        if not self.run:
            return
        self.drawClock()

    def drawClock(self):
        self.canvas.saveContext()
        self.canvas.clear()
        self.canvas.translate(175, 175)
        self.canvas.scale(0.8, 0.8)
        self.canvas.rotate( (-math.pi / 2))
        
        self.canvas.saveContext()
        self.canvas.beginPath()
        self.canvas.setLineWidth(7)
        self.canvas.setStrokeStyle(Color.Color("#325FA2"))
        self.canvas.setFillStyle(Color.Color("#fff"))
        self.canvas.arc(0, 0, 142, 0,  (math.pi * 2), True)
        self.canvas.fill()
        self.canvas.arc(0, 0, 142, 0,  (math.pi * 2), True)
        self.canvas.stroke()
        self.canvas.restoreContext()
        
        self.canvas.setStrokeStyle(Color.BLACK)
        self.canvas.setFillStyle(Color.WHITE)
        self.canvas.setLineWidth(4)
        self.canvas.setLineCap("round")
        
        # Hour marks
        self.canvas.saveContext()
        for i in range(12):
            self.canvas.beginPath()
            self.canvas.rotate( (math.pi / 6))
            self.canvas.moveTo(100, 0)
            self.canvas.lineTo(120, 0)
            self.canvas.stroke()
        
        self.canvas.restoreContext()
        
        # Minute marks
        self.canvas.saveContext()
        self.canvas.setLineWidth(2.5)
        for i in range(60):
            if i % 5 != 0:
                self.canvas.beginPath()
                self.canvas.moveTo(117, 0)
                self.canvas.lineTo(120, 0)
                self.canvas.stroke()
            
            self.canvas.rotate( (math.pi / 30))
        
        self.canvas.restoreContext()
        
        sec = self.getTimeSeconds()
        min = self.getTimeMinutes() + sec / 60.0
        hr = self.getTimeHours() + min / 60.0

        self.canvas.setFillStyle(Color.BLACK)
        
        # write Hours
        self.canvas.saveContext()
        self.canvas.rotate( (hr * math.pi / 6 + math.pi / 360 * min + math.pi
                                / 21600 * sec))
        self.canvas.setLineWidth(7)
        self.canvas.beginPath()
        self.canvas.moveTo(-20, 0)
        self.canvas.lineTo(80, 0)
        self.canvas.stroke()
        self.canvas.restoreContext()
        
        # write Minutes
        self.canvas.saveContext()
        self.canvas.rotate( (math.pi / 30 * min + math.pi / 1800 * sec))
        self.canvas.setLineWidth(5)
        self.canvas.beginPath()
        self.canvas.moveTo(-28, 0)
        self.canvas.lineTo(112, 0)
        self.canvas.stroke()
        self.canvas.restoreContext()
        
        # Write seconds
        self.canvas.saveContext()
        self.canvas.rotate( (sec * math.pi / 30))
        self.canvas.setStrokeStyle(Color.Color("#D40000"))
        self.canvas.setFillStyle(Color.Color("#D40000"))
        self.canvas.setLineWidth(3)
        self.canvas.beginPath()
        self.canvas.moveTo(-30, 0)
        self.canvas.lineTo(83, 0)
        self.canvas.stroke()
        self.canvas.beginPath()
        self.canvas.moveTo(107, 0)
        self.canvas.lineTo(121, 0)
        self.canvas.stroke()
        self.canvas.beginPath()
        self.canvas.arc(0, 0, 10, 0,  (math.pi * 2), True)
        self.canvas.fill()
        self.canvas.beginPath()
        self.canvas.arc(95, 0, 10, 0,  (math.pi * 2), True)
        self.canvas.stroke()
        self.canvas.beginPath()
        self.canvas.setFillStyle(Color.Color("#555"))
        self.canvas.arc(0, 0, 3, 0,  (math.pi * 2), True)
        self.canvas.fill()
        self.canvas.restoreContext()
        
        self.canvas.restoreContext()
        Timer(1000, self)
    
    def drawSpirograph(self, p, r0, r, o):
        x1 = r0 - o
        y1 = 0
        i = 1
        x2 = None
        y2 = None
        self.canvas.beginPath()
        self.canvas.moveTo(x1, y1)
        while x2 != r0 - o  and  y2 != 0  and  i < p:
            x2 =  ((r0 + r) * math.cos(i * math.pi / 72) - (r + o)
                    * math.cos(((r0 + r) / r) * (i * math.pi / 72)))
            y2 =  ((r0 + r) * math.sin(i * math.pi / 72) - (r + o)
                    * math.sin(((r0 + r) / r) * (i * math.pi / 72)))
            self.canvas.lineTo(x2, y2)
            x1 = x2
            y1 = y2
            i += 1
        self.canvas.stroke()
    


