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

from CheckBox import CheckBox

class RadioButton(CheckBox):

    _props = [("group", "Group", "Name", None),
            ]

    def __init__(self, group=None, label=None, asHTML=False, **ka):
        ka['StyleName'] = ka.get('StyleName', "gwt-RadioButton")
        ka['Element'] = ka.get('Element', None) or DOM.createInputRadio(group)
        CheckBox.__init__(self, label, asHTML, **ka)

    @classmethod
    def _getProps(self):
        return CheckBox._getProps() + self._props


Factory.registerClass('pyjamas.ui.RadioButton', RadioButton)

