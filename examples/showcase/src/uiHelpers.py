""" uiHelpers.py

    This module contains various helper classes and functions to make it easier
    to build a Pyjamas application.
"""
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Widget import Widget

from pyjamas import DOM
from pyjamas import Window

#############################################################################

def indent(contents, all=None, left=None, right=None, top=None, bottom=None,
                     hIndent=None, vIndent=None):
    """ Add a wrapper around the given contents to indent it.

        The parameters are as follows:
            
            'contents'

                The contents to indent.  This should be a widget or a panel.

            'all'

                The indent to use for all four sides.  This is the first
                argument, allowing you to call indent(c, 20) to indent the
                contents on all sides by the same amount.

            'left'

                The left indent to use.

            'right'

                The right indent to use.

            'top'

                The top indent to use.

            'bottom'

                The bottom indent to use.

            'hIndent'

                The indent to use for the left and right sides.

            'vIndent'

                The indent to use for the top and bottom.

        The contents will be wrapped in a panel which include whitespace on
        each side of the panel as specified.

        Upon completion, we return a Panel object contained the wrapped-up
        contents.
    """
    if all != None:
        left   = all
        right  = all
        top    = all
        bottom = all

    if hIndent != None:
        left  = hIndent
        right = hIndent

    if vIndent != None:
        top    = vIndent
        bottom = vIndent

    wrapper = DockPanel()
    wrapper.setSpacing(0)
    wrapper.add(contents, DockPanel.CENTER)

    if left > 0:
        padding = Whitespace(width=left)
        wrapper.add(padding, DockPanel.WEST)

    if top > 0:
        padding = Whitespace(height=top)
        wrapper.add(padding, DockPanel.NORTH)

    if right > 0:
        padding = Whitespace(width=right)
        wrapper.add(padding, DockPanel.EAST)

    if bottom > 0:
        padding = Whitespace(height=bottom)
        wrapper.add(padding, DockPanel.SOUTH)

    return wrapper

#############################################################################

def border(contents):
    """ Draw a border around the given contents.

        We return a Panel which wraps up the given contents and draws a border
        around it.
    """
    wrapper = VerticalPanel()
    wrapper.add(contents)
    wrapper.setBorderWidth(1)
    return wrapper

#############################################################################

def colour(contents, colour):
    """ Add colour to the given contents.

        'contents' is a widget or panel to colour, and 'colour' is the HTML
        colour code (eg, "#808080", etc) to use for the background colour.

        We returned the given contents wrapped in a Panel which has the given
        background colour attached.
    """
    wrapper = VerticalPanel()
    wrapper.add(contents)
    DOM.setStyleAttribute(wrapper.getElement(), "background-color", colour)
    return wrapper

#############################################################################

def prompt(msg, defaultReply=""):
    """ Prompt the user to enter some text.

        We return the entered text, or None if the user cancelled.
    """
    JS("""
       return $wnd.prompt(msg, defaultReply);
    """)

#############################################################################

class Whitespace(Widget):
    """ A custom widget which has a fixed size and no contents.

        This can be used to add arbitrary whitespace to your user interface.
    """
    def __init__(self, width=0, height=0):
        """ Standard initialiser.

            'width' and 'height' are the dimensions to use for this whitespace,
            in pixels.
        """
        Widget.__init__(self)
        self.setElement(DOM.createElement('div'))
        self.setPixelSize(width, height)

#############################################################################

class PanelWithLabel(SimplePanel):
    """ A generic panel with a label at the top.
    """
    def __init__(self, label, contents):
        """ Standard initialiser.

            'label' is the string to show at the top, while 'contents' is a
            panel or widget to show in the main body of the panel.
        """
        SimplePanel.__init__(self)

        label = HTML('<b>' + label + '</b>')

        vPanel = VerticalPanel()
        vPanel.add(indent(label, left=5))
        vPanel.add(border(indent(contents, 10)))

        self.add(vPanel)

#############################################################################

class PanelApp:
    """ A generic multiple-panel web application.

        This class makes it easy to handle multiple panels within a web
        application.  Panels are shown as they are required.
    """
    def onModuleLoad(self):
        """ Dynamically build our user interface when the web page is loaded.
        """
        self._curPanelID = None # ID of currently-shown panel.
        self._root       = RootPanel()

        self._panels = self.createPanels()
        self.showPanel(self.getDefaultPanel())


    def showPanel(self, panelID):
        """ Show the panel with the given ID.
        """
        if panelID == self._curPanelID: return

        if self._curPanelID != None:
            self._root.remove(self._panels[self._curPanelID])

        self._root.add(self._panels[panelID])
        self._curPanelID = panelID

    # ==============================
    # == METHODS TO BE OVERRIDDEN ==
    # ==============================

    def createPanels(self):
        """ Create the various panels to be used by this application.

            This should be overridden by the subclass to create the various
            panels the application will use.  Upon completion, the subclass
            should return a dictionary mapping the ID to use for each panel to
            the panel to be displayed.
        """
        Window.alert("Must be overridden.")


    def getDefaultPanel(self):
        """ Return the ID of the panel to show on system startup.
        """
        Window.alert("Must be overridden.")

#############################################################################

class CommandWrapper:
    """ A wrapper which lets you use a method as a deferred command handler.

        The DeferredCommand module assumes that the command object it is given
        will have an execute() method.  This makes having multiple commands
        within a single class difficult; the command wrapper lets you simply
        pass an object and method name, and that method will be called when the
        deferred command is executed.
    """
    def __init__(self, object, handler):
        """ Standard initialiser.

            'object' is the object the command will be associated with, and
            'handler' is the name of the method within that object to call to
            execute the command.
        """
        self._object  = object
        self._handler = handler


    def execute(self):
        """ Respond to the command being executed.

            We call object.handler().
        """
        handler = getattr(self._object, self._handler)
        handler()

