""" raphael.py

    This Python module is a Pyjamas wrapper around the Raphael SVG graphics
    library.

    The Raphael wrapper was written by Erik Westra (ewestra at gmail dot com).
"""

from pyjamas.ui.Widget import Widget
from pyjamas import DOM
from pyjamas import Window
from __pyjamas__ import JS

#############################################################################

class Raphael(Widget):
    """ A Pyjamas wrapper around the Raphael canvas object.
    """
    def __init__(self, width, height):
        """ Standard initialiser.

            'width' and 'height' are the dimensions to use for the canvas, in
            pixels.
        """
        Widget.__init__(self)

        element = DOM.createDiv()
        self.setElement(element)
        self.setPixelSize(width, height)
        JS("""
           this._canvas = $wnd.Raphael(@{{element}}, @{{width}}, @{{height}});
        """)


    def getCanvas(self):
        """ Return our Raphael canvas object.

            This can be used to directly access any Raphael functionality which
            has not been implemented by this wrapper module.  You'll probably
            never need to use it, but it's here just in case.
        """
        return self._canvas


    def setSize(self, width, height):
        """ Change the dimensions of the canvas.
        """
        JS("""
           this._canvas.setSize(@{{width}}, @{{height}});
        """)


    def getColor(self, brightness=None):
        """ Return the next colour to use in the spectrum.
        """
        JS("""
           @{{colour}} = this._canvas.getColor();
        """)
        return colour


    def resetColor(self):
        """ Reset getColor() so that it will start from the beginning.
        """
        JS("""
           this._canvas.getColor().reset();
        """)


    def circle(self, x, y, radius):
        """ Create and return a circle element.

            The circle will be centred around (x,y), and will have the given
            radius.

            We return a RaphaelElement object representing the circle.
        """
        JS("""
           this._element = this._canvas.circle(@{{x}}, @{{y}}, @{{radius}});
        """)
        return RaphaelElement(self._element)


    def rect(self, x, y, width, height, cornerRadius=0):
        """ Create and return a rectangle element.

            The rectangle will have its top-left corner at (x,y), and have the
            given width and height.  If 'cornerRadius' is specified, the
            rectangle will have rounded corners with the given radius.

            We return a RaphaelElement object representing the rectangle.
        """
        JS("""
           this._element = this._canvas.rect(@{{x}}, @{{y}}, @{{width}}, @{{height}},
                                             @{{cornerRadius}});
        """)
        return RaphaelElement(self._element)


    def ellipse(self, x, y, xRadius, yRadius):
        """ Create and return an ellipse element.

            The ellipse will be centred around (x,y), and will have the given
            horizontal and vertical radius.

            We return a RaphaelElement object representing the ellipse.
        """
        JS("""
           this._element = this._canvas.ellipse(@{{x}}, @{{y}}, @{{xRadius}}, @{{yRadius}});
        """)
        return RaphaelElement(self._element)


    def image(self, src, x, y, width, height):
        """ Create and return an image element.

            The image will use 'src' as the URI to read the image data from.
            The top-left corner of the image will be at (x,y), and the image
            element will have the given width and height.

            We return a RaphaelElement object representing the image.
        """
        JS("""
           this._element = this._canvas.image(@{{src}}, @{{x}}, @{{y}}, @{{width}}, @{{height}});
        """)
        return RaphaelElement(self._element)


    def set(self):
        """ Create and return a set element.

            This can be used to group elements together and operate on these
            elements as a unit.

            We return a RaphaelSetElement representing the set.
        """
        JS("""
           @{{self}}._element = this._canvas.set();
        """)
        return RaphaelSetElement(self._element)


    def text(self, x, y, text):
        """ Create and return a text element.

            The element will be placed at (x,y), and will display the given
            text.  Note that you can embed newline ("\n") characters into the
            text to force line breaks.

            We return a RaphaelElement representing the text.
        """
        JS("""
           this._element = this._canvas.text(@{{x}}, @{{y}}, @{{text}});
        """)
        return RaphaelElement(self._element)


    def path(self, attrs=None, data=None):
        """ Create and return a path object.

            If 'attrs' is defined, it should be a dictionary mapping attribute
            names to values for the new path object.  If 'data' is not None, it
            should be a string containing the path data, in SVG path string
            format.

            We return a RaphaelPathElement representing the path.
        """
        if data != None:
            JS("""
               this._element = this._canvas.path({});
            """)
        else:
            JS("""
               this._element = this._canvas.path({}, @{{data}});
            """)

        if attrs != None:
            for attr in attrs.keys():
                value = attrs[attr]
                JS("""
                    this._element.attr(@{{attr}}, @{{value}});
                """)

        return RaphaelPathElement(self._element)

#############################################################################

class RaphaelElement:
    """ Wrapper object for a Raphael element.

        Note that these objects are created by the appropriate methods within
        the Raphael object; you should never need to initialise one of these
        objects yourself.
    """
    def __init__(self, raphaelElement):
        """ Standard initialiser.

            'raphaelElement' is the raphael element that we are wrapping.
        """
        self._element   = raphaelElement
        self._listeners = {'click'      : [],
                           'mousedown'  : [],
                           'mouseup'    : [],
                           'mousemove'  : [],
                           'mouseenter' : [],
                           'mouseleave' : []}

        onClick      = getattr(self, "_onClick")
        onMouseDown  = getattr(self, "_onMouseDown")
        onMouseUp    = getattr(self, "_onMouseUp")
        onMouseMove  = getattr(self, "_onMouseMove")
        onMouseEnter = getattr(self, "_onMouseEnter")
        onMouseLeave = getattr(self, "_onMouseLeave")

        JS("""
           this._element.node.onclick      = @{{onClick}};
           this._element.node.onmousedown  = @{{onMouseDown}};
           this._element.node.onmouseup    = @{{onMouseUp}};
           this._element.node.onmousemove  = @{{onMouseMove}};
           this._element.node.onmouseenter = @{{onMouseEnter}};
           this._element.node.onmouseleave = @{{onMouseLeave}};
        """)


    def addListener(self, type, listener):
        """ Add a listener function to this element.

            The parameters are as follows:

                'type'

                    The type of event to listen out for.  One of:

                        "click"
                        "mousedown"
                        "mouseup"
                        "mousemove"
                        "mouseenter"
                        "mouseleave"

                'listener'

                    A Python callable object which accepts two parameters: the
                    RaphaelElement object that was clicked on, and the event
                    object.

            The given listener function will be called whenever an event of the
            given type occurs.
        """
        self._listeners[type].append(listener)


    def removeListener(self, type, listener):
        """ Remove a previously-defined listener function.
        """
        self._listeners[type].remove(listener)


    def getElement(self):
        """ Return the DOM element we are wrapping.
        """
        return self._element


    def remove(self):
        """ Remove this element from the canvas.

            You can't use the element after you call this method.
        """
        JS("""
           this._element.remove();
        """)


    def hide(self):
        """ Make this element invisible.
        """
        JS("""
           this._element.hide();
        """)


    def show(self):
        """ Make this element visible.
        """
        JS("""
           this._element.show();
        """)


    def rotate(self, angle, cx, cy=None):
        """ Rotate the element by the given angle.

            This can be called in two different ways:

                element.rotate(angle, isAbsolute)

                   where 'angle' is the angle to rotate the element by, in
                   degrees, and 'isAbsolute' specifies it the angle is relative
                   to the previous position (False) or if it is the absolute
                   angle to rotate the element by (True).

            or:

                element.rotate(angle, cx, cy):

                    where 'angle' is the angle to rotate the element by, in
                    degrees, and 'cx' and 'cy' define the origin around which
                    to rotate the element.
        """
        if cy == None:
            isAbsolute = cx
            JS("""
               this._element.rotate(@{{angle}}, @{{isAbsolute}});
            """)
        else:
            JS("""
               this._element.rotate(@{{angle}}, @{{cx}}, @{{cy}});
            """)


    def translate(self, dx, dy):
        """ Move the element around the canvas by the given number of pixels.
        """
        JS("""
           this._element.translate(@{{dx}}, @{{dy}});
        """)


    def scale(self, xtimes, ytimes):
        """ Resize the element by the given horizontal and vertical multiplier.
        """
        JS("""
           this._element.scale(@{{xtimes}}, @{{ytimes}});
        """)


    def setAttr(self, attr, value):
        """ Set the value of a single attribute for this element.

            The following attributes are currently supported:

                cx number
                cy number
                fill colour
                fill-opacity number
                font string
                font-family string
                font-size number
                font-weight string
                gradient object|string
                        "‹angle›-‹colour›[-‹colour›[:‹offset›]]*-‹colour›"
                height number
                opacity number
                path pathString
                r number
                rotation number
                rx number
                ry number
                scale CSV
                src string (URL)
                stroke colour
                stroke-dasharray string ['-', '.', '-.', '-..', '. ', '- ',
                                         '--', '- .', '--.', '--..']
                stroke-linecap string ['butt', 'square', 'round', 'miter']
                stroke-linejoin string ['butt', 'square', 'round', 'miter']
                stroke-miterlimit number
                stroke-opacity number
                stroke-width number
                translation CSV
                width number
                x number
                y number

            Please refer to the SVG specification for an explanation of these
            attributes and how to use them.
        """
        JS("""
           this._element.attr(@{{attr}}, @{{value}});
        """)


    def setAttrs(self, attrs):
        """ Set the value of multiple attributes at once.

            'attrs' should be a dictionary mapping attribute names to values.

            The available attributes are listed in the description of the
            setAttr() method, above.
        """
        for attr,value in attrs.items():
            JS("""
               this._element.attr(@{{attr}}, @{{value}});
            """)


    def getAttr(self, attr):
        """ Return the current value for the given attribute.
        """
        JS("""
           var value = this._element.attr(@{{attr}});
        """)
        return value


    def animate(self, attrs, duration):
        """ Linearly change one or more attributes over a given timeframe.

            'attrs' should be a dictionary mapping attribute names to values,
            and 'duration' should be how long to run the animation for (in
            milliseconds).

            Only the following attributes can be animated:

                cx number
                cy number
                fill colour
                fill-opacity number
                font-size number
                height number
                opacity number
                path pathString
                r number
                rotation number
                rx number
                ry number
                scale CSV
                stroke colour
                stroke-opacity number
                stroke-width number
                translation CSV
                width number
                x number
                y number

            Note that the use of a callback function is not yet supported
            within the Raphael wrapper, even though Raphael itself supports it.
        """
        JS("""
           var jsAttrs = {};
        """)
        for attr,value in attrs.items():
            JS("""
               @{{!jsAttrs}}[@{{attr}}] = @{{value}};
            """)

        JS("""
           this._element.animate(@{{!jsAttrs}}, @{{duration}});
        """)


    def getBBox(self):
        """ Return the bounding box for this element.

            We return a dictionary with 'x', 'y', 'width' and 'height'
            elements.
        """
	x = y = width = height = 0 #declared
        JS("""
           var bounds = this._element.getBBox();
           @{{x}} = bounds.x;
           @{{y}} = bounds.y;
           @{{width}} = bounds.width;
           @{{height}} = bounds.height;
        """)
        return {'x'      : x,
                'y'      : y,
                'width'  : width,
                'height' : height}


    def toFront(self):
        """ Move the element in front of all other elements on the canvas.
        """
        JS("""
           this._element.toFront();
        """)


    def toBack(self):
        """ Move the element behind all the other elements on the canvas.
        """
        JS("""
           this._element.toBack();
        """)


    def insertBefore(self, element):
        """ Move this element so that it appears in front of the given element.

            'element' should be a RaphaelElement object.
        """
        otherElement = element.getElement()
        JS("""
           this._element.insertBefore(@{{otherElement}});
        """)


    def insertAfter(self, element):
        """ Move this element so that it appears behind the given element.
        """
        otherElement = element.getElement()
        JS("""
           this._element.insertAfter(@{{otherElement}});
        """)

    # =====================
    # == PRIVATE METHODS ==
    # =====================

    def _onClick(self, event):
        """ Respond to a mouse-click event.
        """
        listeners = self._listeners['click']
        for listener in listeners:
            listener(self, event)


    def _onMouseDown(self, event):
        """ Respond to a mouse-down event.
        """
        listeners = self._listeners['mousedown']
        for listener in listeners:
            listener(self, event)


    def _onMouseUp(self, event):
        """ Respond to a mouse-up event.
        """
        listeners = self._listeners['mouseup']
        for listener in listeners:
            listener(self, event)


    def _onMouseMove(self, event):
        """ Respond to a mouse-move event.
        """
        listeners = self._listeners['mousemove']
        for listener in listeners:
            listener(self, event)


    def _onMouseEnter(self, event):
        """ Respond to a mouse-enter event.
        """
        listeners = self._listeners['mouseenter']
        for listener in listeners:
            listener(self, event)


    def _onMouseLeave(self, event):
        """ Respond to a mouse-leave event.
        """
        listeners = self._listeners['mouseleave']
        for listener in listeners:
            listener(self, event)

#############################################################################

class RaphaelSetElement(RaphaelElement):
    """ A RaphaelElement that represents a set of elements.
    """
    def add(self, element):
        """ Add an element to this set.
        """
        otherElement = element.getElement()
        JS("""
           this._element.push(@{{otherElement}});
        """)

#############################################################################

class RaphaelPathElement(RaphaelElement):
    """ A RaphaelElement that represents a path.

        Note that the RaphaelPathElement object is returned by each of the
        methods defined in this calss, allowing method calls to be chained
        together.
    """
    def absolutely(self):
        """ Tell the path to treat all subsequent units as absolute ones.

            Coordinates are absolute by default.
        """
        JS("""
            this._element.absolutely();
        """)
        return self


    def relatively(self):
        """ Tell the path to treat all subsequent units as relative ones.

            Coordinates are absolute by default.
        """
        JS("""
            this._element.relatively();
        """)
        return self


    def moveTo(self, x, y):
        """ Move the drawing point to the given coordinates.
        """
        JS("""
            this._element.moveTo(@{{x}}, @{{y}});
        """)
        return self


    def lineTo(self, x, y):
        """ Draw a straight line to the given coordinates.
        """
        JS("""
            this._element.lineTo(@{{x}}, @{{y}});
        """)
        return self


    def cplineTo(self, x, y, width=None):
        """ Draw a curved line to the given coordinates.

            'x' and 'y' define the ending coordinates, and 'width' defines how
            much of a curve to give to the line.  The line will have horizontal
            anchors at the start and finish points.
        """
        if width != None:
            JS("""
               this._element.cplineTo(@{{x}}, @{{y}}, @{{width}});
            """)
        else:
            JS("""
               this._element.cplineTo(@{{x}}, @{{y}});
            """)
        return self


    def curveTo(self, x1, y1, x2, y2, x3, y3):
        """ Draw a bicubic curve to the given coordinates.
        """
        JS("""
            this._element.curveTo(@{{x1}}, @{{y1}}, @{{x}}, @{{y2}}, @{{x3}}, @{{y3}});
        """)
        return self


    def qcurveTo(self, x1, y1, x2, y2):
        """ Draw a quadratic curve to the given coordinates.
        """
        JS("""
            this._element.qcurveTo(@{{x1}}, @{{y1}}, @{{x2}}, @{{y2}});
        """)
        return self


    def addRoundedCorner(self, radius, direction):
        """ Draw a quarter of a circle from the current drawing point.

            'radius' should be the radius of the circle, and 'direction' should
            be one of the following strings:

                "lu"   Left up.
                "ld"   Left down.
                "ru"   Right up.
                "rd"   Right down.
                "ur"   Up right.
                "ul"   Up left.
                "dr"   Down right.
                "dl"   Down left.
        """
        JS("""
            this._element.addRoundedCorner(@{{radius}}, @{{direction}});
        """)
        return self


    def andClose(self):
        """ Close the path being drawn.
        """
        JS("""
            this._element.andClose();
        """)
        return self
