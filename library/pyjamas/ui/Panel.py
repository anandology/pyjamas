# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
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
from __pyjamas__ import console
from pyjamas import Factory
from pyjamas import DOM

from Widget import Widget

class PanelBase(object):

    def add(self):
        raise Exception("This panel does not support no-arg add()")

    def addIndexedItem(self, index, child):
        self.add(child)

    def remove(self, widget):
        pass

    def clear(self):
        """ use this method, due to list changing as it's being iterated.
            also, it's possible to use this method even
        """
        children = []
        for child in self.__iter__():
            children.append(child)

        print "clear children", children

        for child in children:
            self.remove(child)

    def doAttachChildren(self):
        for child in self:
            child.onAttach()

    def doDetachChildren(self):
        for child in self:
            child.onDetach()

    def getWidgetCount(self):
        return len(self.getChildren())

    def getWidget(self, index):
        return self.getChildren()[index]

    def getWidgetIndex(self, child):
        return self.getChildren().index(child)

    def getChildren(self):
        return self.children # assumes self.children: override if needed.

    def __iter__(self):
        return self.getChildren().__iter__()

    def setWidget(self, index, widget):
        """ Replace the widget at the given index with a new one
        """
        existing = self.getWidget(index)
        if existing:
            self.remove(existing)
        self.insert(widget, index)

class Panel(PanelBase, Widget):
    def __init__(self, **kwargs):
        self.children = []
        PanelBase.__init__(self)
        Widget.__init__(self, **kwargs)

    def disown(self, widget):
        if widget.getParent() != self:
            console.error("widget %o is not a child of this panel %o", widget, self)
        else:
            element = widget.getElement()
            widget.setParent(None)
            parentElement = DOM.getParent(element)
            if parentElement:
                DOM.removeChild(parentElement, element)

    def adopt(self, widget, container):
        if container:
            widget.removeFromParent()
            DOM.appendChild(container, widget.getElement())
        widget.setParent(self)


Factory.registerClass('pyjamas.ui.Panel', 'Panel', Panel)

