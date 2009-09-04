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

from pyjamas import DOM
from __pyjamas__ import JS, doc



from pyjamas.canvas.GWTCanvasImplIE6Consts import BUTT, DESTINATION_OVER, SOURCE_OVER
from pyjamas.canvas import GWTCanvasConsts 
#from pyjamas.canvas import JSOStack 
from pyjamas.canvas import PathElement 
from pyjamas.canvas.VMLContext import VMLContext

def addNamespace():
    JS("""
    if (!doc().namespaces["v"]) {
        doc().namespaces.add("v", "urn:schemas-microsoft-com:vml");
        doc().createStyleSheet().cssText = "v\\:*{behavior:url(#default#VML);}";
    }
    """)


"""*
* Deferred binding implementation of GWTCanvas for IE6. It is an implementation
* of canvas on top of VML.
"""
class GWTCanvasImplIE6:

    def __init__(self):
        addNamespace()


        """*
        * This will be used for an array join. Currently a bit faster than
        * StringBuilder.append() & toString() because of the extra collections
        * overhead.
        """
        #self.pathStr = JSOStack.JSOStack.create()
        self.pathStr = [] # buggrit.  use a list.

        """*
        * Stack uses preallocated arrays which makes push() slightly faster than
        * [].push() since each push is simply an indexed setter.
        """
        self.contextStack = []

        self.currentX = 0

        self.currentY = 0

        self.parentElement = None

        self.parentHeight = 0

        self.parentWidth = 0


    """*
    * Takes in a and returns a floored int.
    * Leverages the fact that bitwise OR intifies the value.
    """
    def doubleToFlooredInt(self, val):
        return val or 0


    def arc(self, x, y, radius, startAngle, endAngle, anticlockwise):
        self.pathStr.append(PathElement.arc(x, y, radius, startAngle, endAngle,
                                            anticlockwise, self))


    def beginPath(self):
        #self.pathStr.clear()
        self.pathStr = []


    def clear(self, width=0, height=0):
        #self.pathStr.clear()
        self.pathStr = []
        DOM.setInnerHTML(self.parentElement, "")

    def closePath(self):
        self.pathStr.append(PathElement.closePath())


    def createElement(self):
        self.context = VMLContext()
        self.matrix = self.context.matrix
        return self.createParentElement()


    def createParentElement(self):
        self.parentElement = DOM.createElement("div")
        DOM.setStyleAttribute(self.parentElement, "overflow", "hidden")
        return self.parentElement


    def cubicCurveTo(self, cp1x, cp1y, cp2x, cp2y, x, y):
        self.pathStr.append(PathElement.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y, self))
        self.currentX = x
        self.currentY = y


    def drawImage(self, img, sourceX, sourceY, sourceWidth, sourceHeight, destX, destY, destWidth, destHeight):

        fullWidth = img.getWidth()
        fullHeight = img.getHeight()

        vmlStr = [] # JSOStack.getScratchArray()

        vmlStr.append("<v:group style=\"position:absolute;width:10;height:10;")
        dX = getCoordX(matrix, destX, destY)
        dY = getCoordY(matrix, destX, destY)

        # If we have a transformation matrix with rotation/scale, we
        # apply a filter
        if self.context.matrix[0] != 1  or  self.context.matrix[1] != 0:

            # We create a padding bounding box to prevent clipping.
            vmlStr.append("padding-right:")
            vmlStr.append(str(self.parentWidth) + "px;")
            vmlStr.append("padding-bottom:")
            vmlStr.append(str(self.parentHeight) + "px;")
            vmlStr.append("filter:progid:DXImageTransform.Microsoft.Matrix(M11='")
            vmlStr.append("" + str(self.matrix[0]))
            vmlStr.append("',")
            vmlStr.append("M12='")
            vmlStr.append("" + str(self.matrix[1]))
            vmlStr.append("',")
            vmlStr.append("M21='")
            vmlStr.append("" + str(self.matrix[3]))
            vmlStr.append("',")
            vmlStr.append("M22='")
            vmlStr.append("" + str(self.matrix[4]))
            vmlStr.append("',")
            vmlStr.append("Dx='")
            vmlStr.append("" + str(math.floor(((dX / 10)))))
            vmlStr.append("',")
            vmlStr.append("Dy='")
            vmlStr.append("" + str(math.floor(((dY / 10)))))
            vmlStr.append("', SizingMethod='clip');")

        else:
            vmlStr.append("left:")
            vmlStr.append("%dpx;" % int(dX / 10))
            vmlStr.append("top:")
            vmlStr.append("%dpx" % int(dY / 10))


        vmlStr.append("\" coordsize=\"100,100\" coordorigin=\"0,0\"><v:image src=\"")
        vmlStr.append(img.getSrc())
        vmlStr.append("\" style=\"")

        vmlStr.append("width:")
        vmlStr.append(str(int(destWidth * 100)))
        vmlStr.append(";height:")
        vmlStr.append(str(int(destHeight * 100)))
        vmlStr.append(";\" cropleft=\"")
        vmlStr.append(str(sourceX / fullWidth))
        vmlStr.append("\" croptop=\"")
        vmlStr.append(str(sourceY / fullHeight))
        vmlStr.append("\" cropright=\"")
        vmlStr.append(str((fullWidth - sourceX - sourceWidth) / fullWidth))
        vmlStr.append("\" cropbottom=\"")
        vmlStr.append(str((fullHeight - sourceY - sourceHeight) / fullHeight))
        vmlStr.append("\"/></v:group>")

        self.insert("BeforeEnd", vmlStr.join())


    def fill(self):
        if self.pathStr.isEmpty():
            return

        shapeStr = JSOStack.getScratchArray()
        shapeStr.push("<v:shape style=\"position:absolute;width:10;height:10;\" coordsize=\"100,100\" fillcolor=\"")
        shapeStr.push(self.context.fillStyle)
        shapeStr.push("\" stroked=\"f\" path=\"")

        shapeStr.push(self.pathStr.join())

        shapeStr.push(" e\"><v:fill opacity=\"")
        shapeStr.push(str(self.context.globalAlpha * self.context.fillAlpha))

        if (self.context.fillGradient is not None  and  
                   len(self.context.fillGradient.colorStops) > 0):
            colorStops = self.context.fillGradient.colorStops

            shapeStr.push("\" color=\"")
            shapeStr.push(str(colorStops[0].color))
            shapeStr.push("\" color2=\"")
            shapeStr.push(str(colorStops[colorStops.size() - 1].color))
            shapeStr.push("\" type=\"")
            shapeStr.push(self.context.fillGradient.type)

            minX = self.pathStr.getMinCoordX()
            maxX = self.pathStr.getMaxCoordX()
            minY = self.pathStr.getMinCoordY()
            maxY = self.pathStr.getMaxCoordY()

            dx = maxX - minX
            dy = maxY - minY

            fillLength = math.sqrt((dx * dx) + (dy * dy))
            gradLength = len(self.context.fillGradient)

            # Now add all the color stops
            colors = ""
            for i in range(1, len(colorStops)):
                cs = colorStops[i]
                stopPosn = cs.offset * gradLength
                # /(math.min(((stopPosn / fillLength) * 100), 100))
                colors += "%d%%" % (100 - int(((stopPosn / fillLength) * 100)))
                colors += str(cs.color) + ","
                if stopPosn > fillLength:
                    break


            shapeStr.push("\" colors=\"")
            # shapeStr.push(colors)
            shapeStr.push("50% white,51% #0f0,100% #fff,")
            shapeStr.push("\" angle=\"")
            #shapeStr.push(str(self.context.fillGradient.angle))
            shapeStr.push("180" + "")


        shapeStr.push("\"></v:fill></v:shape>")
        daStr = shapeStr.join()
        # Window.alert(daStr)
        self.insert(self.context.globalCompositeOperation, daStr)


    def fillRect(self, x, y, w, h):
        w += x
        h += y
        beginPath()
        moveTo(x, y)
        lineTo(x, h)
        lineTo(w, h)
        lineTo(w, y)
        closePath()
        fill()
        self.pathStr.clear()


    def getContext(self):
        return self.context


    def getCoordX(self, matrix, x, y):
        coordX = doubleToFlooredInt(math.floor(10 * (matrix[0] * x + matrix[1]
                                * y + matrix[2]) - 4.5))
        # record current point to derive bounding box of current open path.
        self.pathStr.logCoordX(coordX / 10)
        return coordX


    def getCoordY(self, matrix, x, y):
        coordY = doubleToFlooredInt(math.floor(10 * (matrix[3] * x + matrix[4]
                                        * y + matrix[5]) - 4.5))
        # record current point to derive bounding box of current open path.
        self.pathStr.logCoordY(coordY / 10)
        return coordY


    def getFillStyle(self):
        return self.context.fillStyle


    def getGlobalAlpha(self):
        return self.context.globalAlpha


    def getGlobalCompositeOperation(self):
        if self.context.globalCompositeOperation == DESTINATION_OVER:
            return GWTCanvasConsts.DESTINATION_OVER
        else:
            return GWTCanvasConsts.SOURCE_OVER



    def getLineCap(self):
        if self.context.lineCap == BUTT:
            return GWTCanvasConsts.BUTT

        return self.context.lineCap


    def getLineJoin(self):
        return self.context.lineJoin


    def getLineWidth(self):
        return self.context.lineWidth


    def getMiterLimit(self):
        return self.context.miterLimit


    def getStrokeStyle(self):
        return self.context.strokeStyle


    def lineTo(self, x, y):
        self.pathStr.append(PathElement.lineTo(x, y, self))
        self.currentX = x
        self.currentY = y


    def moveTo(self, x, y):
        self.pathStr.append(PathElement.moveTo(x, y, self))
        self.currentX = x
        self.currentY = y


    def quadraticCurveTo(self, cpx, cpy, x, y):
        cp1x = (self.currentX + 2.0 / 3.0 * (cpx - self.currentX))
        cp1y = (self.currentY + 2.0 / 3.0 * (cpy - self.currentY))
        cp2x = (cp1x + (x - self.currentX) / 3.0)
        cp2y = (cp1y + (y - self.currentY) / 3.0)
        self.pathStr.append(PathElement.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y, self))
        self.currentX = x
        self.currentY = y


    def rect(self, x, y, w, h):
        self.pathStr.append(PathElement.moveTo(x, y, self))
        self.pathStr.append(PathElement.lineTo(x + w, y, self))
        self.pathStr.append(PathElement.lineTo(x + w, y + h, self))
        self.pathStr.append(PathElement.lineTo(x, y + h, self))
        self.pathStr.append(PathElement.closePath())
        self.currentX = x
        self.currentY = y + h


    def restoreContext(self):
        if len(self.contextStack) > 0:
            self.context = self.contextStack.pop()
            self.matrix = self.context.matrix



    def rotate(self, angle):
        s = math.sin(-angle)
        c = math.cos(-angle)
        a = self.matrix[0]
        b = self.matrix[1]
        self.matrix[0] = a * c - (b * s)
        self.matrix[1] = a * s + b * c
        a = self.matrix[3]
        b = self.matrix[4]
        self.matrix[3] = a * c - (b * s)
        self.matrix[4] = a * s + b * c


    def saveContext(self):
        self.contextStack.append(self.context)
        self.context = VMLContext(self.context)
        self.matrix = self.context.matrix


    def scale(self, x, y):
        self.context.arcScaleX *= x
        self.context.arcScaleY *= y
        self.matrix[0] *= x
        self.matrix[1] *= y
        self.matrix[3] *= x
        self.matrix[4] *= y


    def setBackgroundColor(self, element, color):
        DOM.setStyleAttribute(element, "backgroundColor", color)


    def setCoordHeight(self, elem, height):
        DOM.setElemAttribute(elem, "width", int(height))
        self.clear(0, 0)


    def setCoordWidth(self, elem, width):
        DOM.setElemAttribute(elem, "width", int(width))
        self.clear(0, 0)


    def setCurrentX(self, currentX):
        self.currentX = currentX


    def setCurrentY(self, currentY):
        self.currentY = currentY


    def setFillStyle(self, gradient):
        self.context.fillGradient = gradient


    def setFillStyle(self, fillStyle):
        fillStyle = fillStyle.strip()
        if fillStyle.startswith("rgba("):
            end = fillStyle.find(")", 12)
            if end > -1:
                guts = fillStyle[5:end].split(",")
                if len(guts) == 4:
                    self.context.fillAlpha = float(guts[3])
                    self.context.fillStyle = "rgb(" + guts[0] + "," + guts[1] + "," + guts[2] + ")"


        else:
            self.context.fillAlpha = 1
            self.context.fillStyle = fillStyle



    def setGlobalAlpha(self, globalAlpha):
        self.context.globalAlpha = globalAlpha


    def setGlobalCompositeOperation(self, gco):
        gco = gco.strip()
        if gco.lower == GWTCanvasConsts.SOURCE_OVER:
            self.context.globalCompositeOperation = SOURCE_OVER
        elif gco.lower == GWTCanvasConsts.DESTINATION_OVER:
            self.context.globalCompositeOperation = DESTINATION_OVER



    def setLineCap(self, lineCap):
        if lineCap.strip().lower == GWTCanvasConsts.BUTT:
            self.context.lineCap = BUTT
        else:
            self.context.lineCap = lineCap



    def setLineJoin(self, lineJoin):
        self.context.lineJoin = lineJoin


    def setLineWidth(self, lineWidth):
        self.context.lineWidth = lineWidth


    def setMiterLimit(self, miterLimit):
        self.context.miterLimit = miterLimit

    def setParentElement(self, g):
        self.parentElement = g


    def setPixelHeight(self, elem, height):
        DOM.setStyleAttribute(elem, "height", str(height) + "px")
        self.parentHeight = height


    def setPixelWidth(self, elem, width):
        DOM.setStyleAttribute(elem, "width", str(width) + "px")
        self.parentWidth = width


    def setStrokeStyle(self, gradient):
        self.context.strokeGradient = gradient


    def setStrokeStyle(self, strokeStyle):
        strokeStyle = strokeStyle.strip()
        if strokeStyle.startswith("rgba("):
            end = strokeStyle.find(")", 12)
            if end > -1:
                guts = strokeStyle[5:end].split(",")
                if len(guts) == 4:
                    self.context.strokeAlpha = float(guts[3])
                    self.context.strokeStyle = "rgb(" + guts[0] + "," + guts[1] + "," + guts[2] + ")"


        else:
            self.context.strokeAlpha = 1
            self.context.strokeStyle = strokeStyle



    def stroke(self):
        if self.pathStr.isEmpty():
            return

        shapeStr = JSOStack.getScratchArray()
        shapeStr.push("<v:shape style=\"position:absolute;width:10;height:10;\" coordsize=\"100,100\" filled=\"f\" strokecolor=\"")
        shapeStr.push(self.context.strokeStyle)
        shapeStr.push("\" strokeweight=\"")
        shapeStr.push("" + self.context.lineWidth)
        shapeStr.push("px\" path=\"")

        shapeStr.push(self.pathStr.join())

        shapeStr.push(" e\"><v:stroke opacity=\"")
        shapeStr.push("" + self.context.globalAlpha * self.context.strokeAlpha)
        shapeStr.push("\" miterlimit=\"")
        shapeStr.push("" + self.context.miterLimit)
        shapeStr.push("\" joinstyle=\"")
        shapeStr.push(self.context.lineJoin)
        shapeStr.push("\" endcap=\"")
        shapeStr.push(self.context.lineCap)

        shapeStr.push("\"></v:stroke></v:shape>")
        self.insert(self.context.globalCompositeOperation, shapeStr.join())


    def strokeRect(self, x, y, w, h):
        w += x
        h += y
        beginPath()
        moveTo(x, y)
        lineTo(x, h)
        lineTo(w, h)
        lineTo(w, y)
        closePath()
        stroke()
        self.pathStr.clear()


    def transform(m11, m12, m21, m22, dx, dy):
        a = self.matrix[0]
        b = self.matrix[1]
        self.matrix[0] = a * m11 + b * m21
        self.matrix[1] = a * m12 + b * m22
        self.matrix[2] += a * dx + b * dy
        a = self.matrix[3]
        b = self.matrix[4]
        self.matrix[3] = a * m11 + b * m21
        self.matrix[4] = a * m12 + b * m22
        self.matrix[5] += a * dx + b * dy


    def translate(self, x, y):
        self.matrix[2] += self.matrix[0] * x + self.matrix[1] * y
        self.matrix[5] += self.matrix[3] * x + self.matrix[4] * y


    def insert(self, gco, html):
        self.parentElement.insertAdjacentHTML(gco, html)



