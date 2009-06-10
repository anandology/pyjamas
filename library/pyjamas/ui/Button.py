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
from __pyjamas__ import JS
from pyjamas import DOM

from pyjamas.ui.ButtonBase import ButtonBase

class Button(ButtonBase):

    def __init__(self, html=None, listener=None):
        """
        Create a new button widget.

        @param html: Html content (e.g. the button label); see setHTML()
        @param listener: A new click listener; see addClickListener()

        """
        ButtonBase.__init__(self, DOM.createButton())
        self.adjustType(self.getElement())
        self.setStyleName("gwt-Button")
        if html:
            self.setHTML(html)
        if listener:
            self.addClickListener(listener)

    def adjustType(self, button):
        JS("""
        if (button.type == 'submit') {
            try { button.setAttribute("type", "button"); } catch (e) { }
        }
        """)

    def click(self):
        """
        Simulate a button click.
        """
        self.getElement().click()


