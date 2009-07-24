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
import sys
if sys.platform not in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from __pyjamas__ import doc

from pyjamas import DOM
from pyjamas import Window

from pyjamas.ui.AbsolutePanel import AbsolutePanel

rootPanels = {}

class RootPanelCls(AbsolutePanel):
    def __init__(self, element=None):
        AbsolutePanel.__init__(self)
        if element is None:
            element = self.getBodyElement()

        self.setElement(element)
        self.onAttach()

    def getBodyElement(self):
        return doc().body

    @classmethod
    def get(cls, id=None):
        """

        """
        if rootPanels.has_key(id):
            return rootPanels[id]

        element = None
        if id:
            element = DOM.getElementById(id)
            if not element:
                return None

        if len(rootPanels) < 1:
            cls.hookWindowClosing()

        panel = RootPanel(element)
        rootPanels[id] = panel
        return panel

    @classmethod
    def hookWindowClosing(cls):
        Window.addWindowCloseListener(cls)

    @classmethod
    def onWindowClosed(cls):
        for panel in rootPanels.itervalues():
            panel.onDetach()

    @classmethod
    def onWindowClosing(cls):
        return None

def RootPanel(element=None):
    if isinstance(element, str):
        return RootPanelCls().get(element)
    return RootPanelCls(element)

