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
from pyjamas.ui.Label import Label
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.Timer import Timer

from pyjamas.Canvas.Color import Color

import time

from SimpleCanvasDemo import SimpleCanvasDemo

""" Linear congruent random number generator.
*
* Constants are from Knuth via Numerical Recipes in C.
*
"""
global ig
ig = 0
def rnd():
    global ig
    m = 217728
    a = 84589
    c = 45989
    ig = (a*ig + c) % m
    return float(ig)/m


"""*
* Model of  a single particle object in the simulation.
"""
class Particle:

    def __init__(self, chart):
        self.chart = chart
        self.kill = False
        self.gravity = 0.1
        self.xDampening = 0.9
        self.yDampening = 0.9
        self.xPos =   (rnd() * self.chart.width)
        self.yPos =   (rnd() * self.chart.height)
        # Get some negative velocities
        self.xVel =  (rnd() * 5 - 2.5)
        self.yVel =  (rnd() * 5 - 2.5)


    def update(self):

        # Reverse direction on boundaries
        if self.xPos > self.chart.width  or  self.xPos < 0:

            self.xVel = -self.xVel
            self.xPos += self.xVel
            # suck out some energy
            self.xDampening =  max(self.xDampening - 0.1, 0)
            self.xVel *= self.xDampening


        if self.yPos > self.chart.height  or  self.yPos < 0:

            self.yVel = -self.yVel
            self.yPos += self.yVel
            # suck out some energy
            self.yDampening =  max(self.yDampening - 0.1,0)
            self.yVel *=  self.yDampening

            if (self.yPos > self.chart.height - 4)  and  (abs(self.yVel) < 0.1):
                self.yPos = self.chart.height
                self.xVel = 0
                self.gravity = 0
                self.kill = True



        self.xPos += self.xVel
        self.yPos += self.yVel

        # apply gravity
        self.yVel += self.gravity


"""
* Not so much controls as feedback for benchmarking.
"""
class ParticleDemoControls (Composite):
    def __init__(self):
        self.average = 1
        self.iterations = 1
        self.startTime = -1

        self.refreshRateLabel = Label("")
        self.averageLabel = Label("")

        layout = VerticalPanel()
        layout.add(self.refreshRateLabel)
        layout.add(self.averageLabel)

        Composite.__init__(self, layout)

    def doBenchmark(self, now):
        if self.startTime < 0:
            self.startTime = now
        else:
            self.refreshRate = now - self.startTime
            self.startTime = now
            self.average = ((self.average * self.iterations) + self.refreshRate) / (self.iterations + 1)
            self.iterations += 1

            self.refreshRateLabel.setText("Refresh Interval: " + str(refreshRate))
            self.averageLabel.setText("Average Interval: " + str(average))



    def resetBenchmark(self):
        self.average = 1
        self.iterations = 1
        self.startTime = -1




"""*
* Simple particle Simulation showing off some of the Path API.
"""
class ParticleDemo (SimpleCanvasDemo):


    def __init__(self, theCanvas):
        SimpleCanvasDemo.__init__(self, theCanvas)
        self.numParticles = 20
        self.particles = []
        self.takeBenchmarks = False

        self.width = 400
        self.height = 300
        self.canvas = theCanvas
        self.demoName = "Particle Demo"
        self.run = False


    def createControls(self):
        self.controls = ParticleDemoControls()


    def drawDemo(self):
        self.canvas.resize(self.width, self.height)

        self.particles = []

        for i in range(self.numParticles):
            self.particles.append( Particle(self) )

        self.canvas.saveContext()
        self.canvas.setLineWidth(2)
        self.canvas.setStrokeStyle(Color(255,0,0))
        self.run = True
        Timer(10, self)

    def onTimer(self, tid):
        if not self.run:
            return
        self.renderingLoop()
        Timer(10, self)

    def renderingLoop(self):
        self.canvas.clear()

        for i in range(len(self.particles)):
            if self.particles[i].kill:
                continue

            self.particles[i].update()

            self.canvas.beginPath()
            self.canvas.moveTo(self.particles[i].xPos, self.particles[i].yPos)
            self.canvas.lineTo(self.particles[i].xPos - self.particles[i].xVel,
                            self.particles[i].yPos - self.particles[i].yVel)
            self.canvas.closePath()
            self.canvas.stroke()


        # take a benchmark
        if self.takeBenchmarks:
            self.controls.doBenchmark(time.gmtime())


    def stopDemo(self):
        self.run = False
        self.controls.resetBenchmark()
        self.canvas.restoreContext()


