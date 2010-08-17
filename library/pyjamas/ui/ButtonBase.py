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
from pyjamas.ui.InnerHTML import InnerHTML
from pyjamas.ui.InnerText import InnerText

class ButtonBase(FocusWidget, InnerHTML, InnerText):

    _props = [("label", "Text", "Text", None),
             ("html", "HTML text", "HTML", None),
            ]

    def __init__(self, element, **kwargs):
        FocusWidget.__init__(self, element, **kwargs)

    @classmethod
    def _getProps(self):
        return FocusWidget._getProps() + InnerText._getProps() + \
               InnerHTML._getProps()

Factory.registerClass('pyjamas.ui.ButtonBase', 'ButtonBase', ButtonBase)

