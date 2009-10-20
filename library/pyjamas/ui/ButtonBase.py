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
from pyjamas import DOM
from pyjamas import Factory
from FocusWidget import FocusWidget

class ButtonBase(FocusWidget):

    def __init__(self, element, **kwargs):
        FocusWidget.__init__(self, element, **kwargs)

    def getHTML(self):
        return DOM.getInnerHTML(self.getElement())

    def getText(self):
        return DOM.getInnerText(self.getElement())

    def setHTML(self, html):
        DOM.setInnerHTML(self.getElement(), html)

    def setText(self, text):
        DOM.setInnerText(self.getElement(), text)

Factory.registerClass('pyjamas.ui.ButtonBase', ButtonBase)

