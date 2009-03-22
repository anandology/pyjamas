# Copyright 2006 James Tauber and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pyjamas import DOM

from pyjamas.ui.UIObject import UIObject

class Widget(UIObject):
    """
        Base class for most of the UI classes.  This class provides basic services
        used by any Widget, including management of parents and adding/removing the
        event handler association with the DOM.
    """
    def __init__(self, **kwargs):
        self.attached = False
        self.parent = None
        self.layoutData = None

        UIObject.__init__(**kwargs)

    def getLayoutData(self):
        return self.layoutData

    def getParent(self):
        """Widgets are kept in a hierarchy, and widgets that have been added to a panel
        will have a parent widget that contains them.  This retrieves the containing
        widget for this widget."""
        return self.parent

    def isAttached(self):
        """Return whether or not this widget has been attached to the document."""
        return self.attached

    def onBrowserEvent(self, event):
        pass

    def onLoad(self):
        pass

    def doDetachChildren(self):
        pass

    def doAttachChildren(self):
        pass

    def onAttach(self):
        """Called when this widget has an element, and that element is on the document's
        DOM tree, and we have a parent widget."""
        if self.isAttached():
            return
        self.attached = True
        DOM.setEventListener(self.getElement(), self)
        self.doAttachChildren()
        self.onLoad()

    def onDetach(self):
        """Called when this widget is being removed from the DOM tree of the document."""
        if not self.isAttached():
            return
        self.doDetachChildren()
        self.attached = False
        DOM.setEventListener(self.getElement(), None)

    def setLayoutData(self, layoutData):
        self.layoutData = layoutData

    def setParent(self, parent):
        """Update the parent attribute.  If the parent is currently attached to the DOM this
        assumes we are being attached also and calls onAttach()."""
        oldparent = self.parent
        self.parent = parent
        if parent == None:
            if oldparent != None and oldparent.attached:
                self.onDetach()
        elif parent.attached:
            self.onAttach()

    def removeFromParent(self):
        """Remove ourself from our parent.  The parent widget will call setParent(None) on
        us automatically"""
        if hasattr(self.parent, "remove"):
            self.parent.remove(self)

    def getID(self):
        """Get the id attribute of the associated DOM element."""
        return DOM.getAttribute(self.getElement(), "id")

    def setID(self, id):
        """Set the id attribute of the associated DOM element."""
        DOM.setAttribute(self.getElement(), "id", id)


