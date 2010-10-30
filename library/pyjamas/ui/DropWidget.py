# Copyright (C) 2010 Jim Washington
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


from pyjamas import Factory
from pyjamas.dnd import html5_dnd
from pyjamas.dnd.DNDHelper import dndHelper
from pyjamas.ui.Widget import Widget
from pyjamas.ui.DropHandler import DropHandler


class DropWidget(Widget, DropHandler):
    """
        Mix-in class for a drop-target widget
    """
    def __init__(self, **kw):
        if (not hasattr(self, 'attached')) or kw:
            Widget.__init__(self, **kw)
        self.html5_dnd = html5_dnd
        DropHandler.__init__(self)
        self.addDropListener(self)
        if not self.html5_dnd:
            dndHelper.registerTarget(self)

Factory.registerClass('pyjamas.ui.DropWidget', 'DropWidget', DropWidget)

