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

from pyjamas.ui.Widget import Widget

class Composite(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.widget = None

    def initWidget(self, widget):
        if self.widget is not None:
            return

        widget.removeFromParent()
        self.setElement(widget.getElement())

        self.widget = widget
        widget.setParent(self)

    def isAttached(self):
        if self.widget:
            return self.widget.isAttached()
        return False

    def onAttach(self):
        #print "Composite.onAttach", self
        self.widget.onAttach()
        DOM.setEventListener(self.getElement(), self);

        self.onLoad()

    def onDetach(self):
        self.widget.onDetach()

    def setWidget(self, widget):
        self.initWidget(widget)

    def onBrowserEvent(self, event):
        #print "Composite onBrowserEvent", self, event
        self.widget.onBrowserEvent(event)

