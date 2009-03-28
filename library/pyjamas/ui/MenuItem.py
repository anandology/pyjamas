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
from pyjamas.ui import Event

class MenuItem(UIObject):
    # also callable as:
    #   MenuItem(text, cmd)
    #   MenuItem(text, asHTML, cmd)
    #   MenuItem(text, subMenu)
    #   MenuItem(text, asHTML)
    def __init__(self, text, asHTML, subMenu=None):
        cmd = None
        if subMenu == None:
            if hasattr(asHTML, "execute"): # text, cmd
                cmd = asHTML
                asHTML = False
            elif hasattr(asHTML, "onShow"): # text, subMenu
                subMenu = asHTML
                asHTML = False
            # else: text, asHTML
        elif hasattr(subMenu, "execute"): # text, asHTML, cmd
            cmd = subMenu
            subMenu = None
        # else: text, asHTML, subMenu

        self.command = None
        self.parentMenu = None
        self.subMenu = None

        self.setElement(DOM.createTD())
        self.sinkEvents(Event.ONCLICK | Event.ONMOUSEOVER | Event.ONMOUSEOUT)
        self.setSelectionStyle(False)

        if asHTML:
            self.setHTML(text)
        else:
            self.setText(text)

        self.setStyleName("gwt-MenuItem")

        if cmd:
            self.setCommand(cmd)
        if subMenu:
            self.setSubMenu(subMenu)

    def getCommand(self):
        return self.command

    def getHTML(self):
        return DOM.getInnerHTML(self.getElement())

    def getParentMenu(self):
        return self.parentMenu

    def getSubMenu(self):
        return self.subMenu

    def getText(self):
        return DOM.getInnerText(self.getElement())

    def setCommand(self, cmd):
        self.command = cmd

    def setHTML(self, html):
        DOM.setInnerHTML(self.getElement(), html)

    def setSubMenu(self, subMenu):
        self.subMenu = subMenu

    def setText(self, text):
        DOM.setInnerText(self.getElement(), text)

    def setParentMenu(self, parentMenu):
        self.parentMenu = parentMenu

    def setSelectionStyle(self, selected):
        if selected:
            self.addStyleName("gwt-MenuItem-selected")
        else:
            self.removeStyleName("gwt-MenuItem-selected")


