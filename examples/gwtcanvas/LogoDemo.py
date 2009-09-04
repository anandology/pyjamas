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



from pyjamas.Timer import Timer
from pyjamas import Window
from pyjamas import DOM
from pyjamas.ui.Composite import Composite
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.Canvas.ImageLoader import loadImages

from SimpleCanvasDemo import SimpleCanvasDemo

#from pyjamas import log

class LogoDemoControls(Composite):
    def __init__(self):
        Composite.__init__(self, VerticalPanel())

"""*
* Demo Showcasing simple image rendering, transformations and animations.
"""
class LogoDemo(SimpleCanvasDemo):

    """
    * Controls for the logo demo. We dont actually have any controls at the
    * moment, so we just initialize with an empty Vertical Panel.
    """


    def __init__(self, theCanvas):
        SimpleCanvasDemo.__init__(self, theCanvas)
        self.height = 400
        self.width = 600
        self.demoName = "Pyjamas Logo"

        """
        * Reference to our ImageHandle that gets initialized on the callback from
        * ImageLoader.
        """
        self.img = None

        self.rotation = 0.1

        self.run = False

    def createControls(self):
        self.controls = LogoDemoControls()


    def drawDemo(self):
        # The following is the same as doing
        self.canvas.resize(self.width,self.height)
        #self.canvas.setCoordSize(self.width, self.height)
        #self.canvas.setPixelHeight(self.height)
        #self.canvas.setPixelWidth(self.width)

        imageUrls = ["./pyjamas.128x128.png"]


        if self.img is None:
            # The first time this demo gets run we need to load our images.
            # Maintain a reference to the image we load so we can use it
            # the next time the demo is selected
            loadImages(imageUrls, self)

        else:
            # Go ahead and animate
            if self.isImageLoaded(self.img):
                self.run = True
                #log.writebr("already loaded")
                Timer(1, self)
            else:
                Window.alert("Refresh the page to reload the image.")


    def onImagesLoaded(self, imageHandles):
        #log.writebr("loaded")
        # Drawing code involving images goes here
        self.img = imageHandles[0]
        self.run = True
        Timer(1, self)


    def stopDemo(self):
        self.run = False


    def isImageLoaded(self, imgElem):
        return imgElem.__isLoaded

    def renderingLoop(self):
        self.canvas.saveContext()

        self.canvas.clear()
        # Draw a version of the logo, sampling the last 100x100
        # (image is 185x175) pixels of the image.
        # Draw starting at position 10, 10
        # scaled up by a factor of 2 on the self.canvas (using 200x200 as the
        # destination dimensions).
        #log.writebr(str(self.img))
        #log.writebr(DOM.getAttribute("src"))
        self.canvas.drawImage(self.img, 84, 74, 100, 100, 10, 10, 200, 200)
        #self.canvas.drawImage(self.img, 84, 74)

        # draw an animated version
        self.canvas.translate(300, 200)
        self.canvas.rotate(self.rotation)
        self.canvas.scale(.9, .9)

        self.canvas.drawImage(self.img, 0, 0)
        self.rotation += 0.1

        self.canvas.restoreContext()

        #log.writebr(str(self.rotation))

    def onTimer(self, tid):
        if not self.run:
            return
        self.renderingLoop()
        Timer(10, self)


