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
from pyjamas import DOM
from pyjamas.dnd.DNDHelper import dndHelper
from pyjamas.ui.Widget import Widget
from pyjamas.ui.DropHandler import DropHandler
import pyjd

class DropWidget(object):
    """
    Mix-in class for a drop-target widget
    """
    pass


class Html5DropWidget(Widget, DropHandler):
    def __init__(self, **kw):
        if (not hasattr(self, 'attached')) or kw:
            Widget.__init__(self, **kw)
        DropHandler.__init__(self)
        self.addDropListener(self)


class EmulatedDropWidget(Html5DropWidget):
    def __init__(self, **kw):
        Html5DropWidget.__init__(self, **kw)
        dndHelper.registerTarget(self)


def init(is_native=None):
    global DropWidget
    if is_native is None:
        html5_dnd = hasattr(DOM.createElement('span'), 'draggable')
    else:
        html5_dnd = is_native
    if html5_dnd:
        DropWidget = Html5DropWidget
    else:
        DropWidget = EmulatedDropWidget

if pyjd.is_desktop:
    init(pyjd.native_dnd)
else:
    init(None)

Factory.registerClass('pyjamas.ui.DropWidget', 'DropWidget', DropWidget)
