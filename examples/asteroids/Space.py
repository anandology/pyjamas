#   Copyright 2009 Joe Rumsey
#   (joe@rumsey.org)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import pyjd # this is dummy in pyjs.
from pyjamas import DOM

from pyjamas.ui.RootPanel import RootPanel, RootPanelCls, manageRootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Label import Label
from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.Canvas.GWTCanvas import GWTCanvas
from pyjamas.Canvas.ImageLoader import loadImages
from pyjamas.Canvas import Color

#from pyjamas.Canvas2D import Canvas, CanvasImage, ImageLoadListener
from pyjamas.Timer import Timer
from pyjamas import Window
from pyjamas import log
from pyjamas.ui import Event
from pyjamas.ui import KeyboardListener
from pyjamas.ui.KeyboardListener import KeyboardHandler
from pyjamas.ui.ClickListener import ClickHandler

from pyjamas.ui.Image import Image

import math
import pygwt
import random

NUM_ASTEROIDS = 2
FPS = 30
ROTATE_SPEED_PER_SEC = math.pi
ROTATE_SPEED = ROTATE_SPEED_PER_SEC / FPS
FRICTION=0.05
THRUST=0.2
SPEED_MAX = 10
MAX_ASTEROID_SPEED = 2.0
SHOT_LIFESPAN = 60
SHOT_COLOR = Color.Color('#fff')
SHOT_SPEED = 7.0
SHOT_DELAY = 10
ASTEROID_RADIUS = 45.0
ASTEROID_IMAGE_SIZE=180.0
ASTEROID_SIZES = [90.0, 45.0, 22.0, 11.0]

def randfloat(absval):
    return (random.random() * (2 * absval) - absval)

def distsq(x1,y1, x2,y2):
    return ((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2))

class Asteroid:
    def __init__(self, canvas, x=None, y=None, size=0):
        self.canvas = canvas
        if x is None or y is None:
            self.x = canvas.width/2
            self.y = canvas.height/2
            while distsq(self.x, self.y, canvas.width / 2, canvas.height / 2) < (180*180):
                self.x = random.randint(0, canvas.width)
                self.y = random.randint(0, canvas.height)
        else:
            self.x = x
            self.y = y

        self.dx = randfloat(MAX_ASTEROID_SPEED)
        self.dy = randfloat(MAX_ASTEROID_SPEED)
        self.rot = (random.random() * (2 * math.pi)) - math.pi
        self.rotspeed = (random.random() * 0.1) - 0.05
        self.size = size
        self.radius = ASTEROID_SIZES[self.size]
        self.scale = (self.radius / ASTEROID_IMAGE_SIZE) * 2

    def move(self):
        if self.dx > 0 and self.x >= self.canvas.width:
            self.dx = -self.dx
        elif self.dx < 0 and self.x <= 0:
            self.dx = -self.dx

        if self.dy > 0 and self.y >= self.canvas.height:
            self.dy = -self.dy
        elif self.dy < 0 and self.y <= 0:
            self.dy = -self.dy

        self.x += self.dx
        self.y += self.dy
        self.rot += self.rotspeed

    def draw(self):

        ctx = self.canvas

        ctx.saveContext()
        ctx.translate(self.x, self.y)
        ctx.rotate(self.rot)
        ctx.scale(self.scale,self.scale)
        ctx.drawImage(self.canvas.asteroid, -(ASTEROID_IMAGE_SIZE / 2), -(ASTEROID_IMAGE_SIZE / 2))
        ctx.restoreContext()

class Shot:
    def __init__(self, canvas, x, y, dx, dy, dir):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.dir = dir
        self.lifespan = SHOT_LIFESPAN

    def move(self):
        self.lifespan -= 1
        if self.lifespan <= 0:
            return False
        self.x = self.x + self.dx + SHOT_SPEED * math.sin(self.dir)
        self.y = self.y + self.dy - SHOT_SPEED * math.cos(self.dir)
        for a in self.canvas.asteroids:
            if distsq(self.x, self.y, a.x, a.y) < (a.radius * a.radius):
                self.canvas.destroyAsteroid(a)
                return False

        return True

    def draw(self, ctx):
        ctx.setFillStyle(SHOT_COLOR)
        ctx.fillRect(int(self.x - 1),int(self.y - 1),3,3)

class GameCanvas(GWTCanvas):
    def __init__(self, w, h):
        GWTCanvas.__init__(self, w, h)

        self.width = w
        self.height = h
        self.key_up = self.key_down = self.key_left = self.key_right = self.key_fire = False        

        images = ['./images/Ship1.png', './images/Ship2.png', './images/Asteroid.png']
        loadImages(images, self)
        self.run = False
        #self.ship = CanvasImage('images/Ship1.png')
        #self.ship_thrust = CanvasImage('images/Ship2.png')
        #self.asteroid = CanvasImage('images/Asteroid.png')
        #self.loader = ImageLoadListener()
        #self.loader.add(self.ship)
        #self.loader.add(self.ship_thrust)
        #self.loader.add(self.asteroid)

        self.num_asteroids = NUM_ASTEROIDS

        self.sinkEvents(Event.KEYEVENTS) 
        self.onTimer()

    def onImagesLoaded(self, imagesHandles):
        print "loaded images", imagesHandles
        self.ship = imagesHandles[0]
        self.ship_thrust = imagesHandles[1]
        self.asteroid = imagesHandles[2]

        print "resize", self.width, self.height
        self.resize(self.width, self.height)
        self.reset()

        self.run = True
        
    def addTo(self, panel):
        panel.add(self)
        self.top = DOM.getAbsoluteTop(self.getElement())
        self.left = DOM.getAbsoluteLeft(self.getElement())

    def onTimer(self, t=None):
        Timer(int(1000/FPS), self)
        if not self.run:
            return

        self.advance()
        self.draw()

        return

        self.saveContext()
        self.clear()
        self.translate(30, 30)
        self.setFillStyle(Color.Color("#fff"))
        self.setStrokeStyle(Color.Color("#fff"))
        self.beginPath()
        self.moveTo(25, 25)
        self.lineTo(105, 25)
        self.lineTo(25, 105)
        self.closePath()
        self.fill()
        self.beginPath()
        self.moveTo(125, 125)
        self.lineTo(125, 45)
        self.lineTo(45, 125)
        self.closePath()
        self.stroke()
        self.beginPath()
        self.moveTo(265, 265)
        self.lineTo(165, 265)
        self.lineTo(265, 165)
        self.lineTo(265, 265)
        self.fillRect(25, 165, 100, 100)
        self.setFillStyle(Color.BLACK)
        self.fillRect(45, 185, 60, 60)
        self.strokeRect(50, 190, 50, 50)
        self.rect(165, 25, 100, 100)
        self.stroke()
        self.restoreContext()



    def followMouse(self):
        self.dx = self.mouseX - self.xx
        if self.dx != 0:
            self.dx = self.dx / math.fabs(self.dx)

        self.dy = self.mouseY - self.yy
        if self.dy != 0:
            self.dy = self.dy / math.fabs(self.dy)

    def keyboardMotion(self):
        if self.key_left:
            self.rot -= ROTATE_SPEED
        if self.key_right:
            self.rot += ROTATE_SPEED

        if self.rot < 0-math.pi:
            self.rot += 2*math.pi
        elif self.rot > math.pi:
            self.rot -= 2*math.pi

        if self.key_up:
            self.dx += THRUST * math.sin(self.rot)
            self.dy -= THRUST * math.cos(self.rot)
        else:
            if math.fabs(self.dx) < 0.001 and math.fabs(self.dy) < 0.001:
                self.dx = 0
                self.dy = 0
            else:
                dir = math.atan2(self.dx, self.dy)
                self.dx -= FRICTION * math.sin(dir)
                self.dy -= FRICTION * math.cos(dir)
        if self.key_fire:
            self.checkAddShot()

    def setMotion(self):
        self.keyboardMotion()

    def advance(self):
        for a in self.asteroids:
            a.move()
            if(distsq(self.xx, self.yy, a.x, a.y) < (a.radius * a.radius)):
                self.destroyShip()

        for s in self.shots:
            if not s.move():
                self.removeShot(s)

        self.shot_delay -= 1

        self.setMotion()

        self.xx += self.dx
        self.yy += self.dy
        if self.dx > 0 and self.xx >= self.width:
            self.xx -= self.width
        elif self.dx < 0 and self.xx < 0:
            self.xx += self.width
        if self.yy > 0 and self.yy >= self.height:
            self.yy -= self.height
        elif self.dy < 0 and self.yy < 0:
            self.yy += self.height
        
    def setKey(self, k, set):
        DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
        if k == KeyboardListener.KEY_UP:
            self.key_up = set
        elif k == KeyboardListener.KEY_DOWN:
            self.key_down = set
        elif k == KeyboardListener.KEY_LEFT:
            self.key_left = set
        elif k == KeyboardListener.KEY_RIGHT:
            self.key_right = set
        elif k == 32:
            self.key_fire = set
            
    def onKeyPress(self, sender, keyCode, modifiers = None):
        pass
        #self.setKey(keyCode, True)

    def onKeyDown(self, sender, keyCode, modifiers = None):
        self.setKey(keyCode, True)

    def onKeyUp(self, sender, keyCode, modifiers = None):
        self.setKey(keyCode, False)

    def checkAddShot(self):
        if self.shot_delay > 0:
            return
        if self.key_fire:
            s = Shot(self, self.xx, self.yy, self.dx, self.dy, self.rot)
            self.shots.append(s)
            self.shot_delay = SHOT_DELAY

    def destroyAsteroid(self, a):
        self.asteroids.remove(a)
        if a.size < len(ASTEROID_SIZES) - 1:
            for i in range(2):
                self.asteroids.append(Asteroid(self, a.x, a.y, a.size + 1))
        if len(self.asteroids) <= 0:
            self.num_asteroids += 1
            self.reset()

    def removeShot(self, s):
        if s in self.shots:
            self.shots.remove(s)

    def destroyShip(self):
        self.num_asteroids = NUM_ASTEROIDS
        self.reset()

    def reset(self):
        self.asteroids = []
        self.shots = []
        self.shot_delay = 0
        for a in range(self.num_asteroids):
            self.asteroids.append(Asteroid(self))

        # The one thing that really needs to change before going any further
        # is the player's ship being defined solely as members of this canvas
        # class.  It's bad, and comes from having done this whole thing very
        # organically starting from just noodling around with Pyjamas.
        self.xx = self.width/2
        self.yy = self.height/2
        self.dx = 0
        self.dy = 0
        self.rot = 0
        self.speed = 0
        
    def draw(self):

        #if not self.loader.isLoaded():
        #    return
        self.setFillStyle(Color.Color('#000'))
        self.fillRect(0,0,self.width,self.height)

        for a in self.asteroids:
            a.draw()

        for s in self.shots:
            s.draw(self)
        self.saveContext()
        self.translate(self.xx, self.yy)
        self.rotate(self.rot)
        if self.key_up:
            img = self.ship_thrust
        else:
            img = self.ship
        self.drawImage(img, -15, -12)
        self.restoreContext()

class RootPanelListener(RootPanelCls, KeyboardHandler, ClickHandler):
    def __init__(self, Parent, *args, **kwargs):
        self.Parent = Parent
        self.focussed = False
        RootPanelCls.__init__(self, *args, **kwargs)
        ClickHandler.__init__(self)
        KeyboardHandler.__init__(self)

        self.addClickListener(self)

    def onClick(self, Sender):
        self.focussed = not self.focussed
        self.Parent.setFocus(self.focussed)

if __name__ == '__main__':
    pyjd.setup("public/Space.html")
    c = GameCanvas(800, 600)
    panel = FocusPanel(Widget=c)
    RootPanel().add(panel)
    panel.addKeyboardListener(c)
    panel.setFocus(True)
    RootPanel().add(HTML("""
<hr/>
Left/Right arrows turn, Up key thrusts, Space bar fires<br/>
<a href="http://rumsey.org/blog/?p=215">About Space Game</a> by <a href="http://rumsey.org/blog/">Ogre</a><br/>
Written entirely in Python, using <a href="http://pyjs.org/">Pyjamas</a></br>
Copyright &copy; 2009 Joe Rumsey
"""))

    #c.getElement().focus()
    pyjd.run()
