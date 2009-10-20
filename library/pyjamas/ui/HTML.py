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

from Label import Label
from pyjamas.ui import Event

class HTML(Label):

    def __init__(self, html=None, wordWrap=True, element=None, **kwargs):
        if not kwargs.has_key('StyleName'): kwargs['StyleName']="gwt-HTML"
        if html: kwargs['HTML'] = html
        kwargs['WordWrap'] = wordWrap
        if element is None:
            element = DOM.createDiv()
        self.setElement(element)
        Label.__init__(self, **kwargs)
        self.sinkEvents(Event.ONCLICK | Event.MOUSEEVENTS)

    def getHTML(self):
        return DOM.getInnerHTML(self.getElement())

    def setHTML(self, html):
        DOM.setInnerHTML(self.getElement(), html)

Factory.registerClass('pyjamas.ui.HTML', HTML)

