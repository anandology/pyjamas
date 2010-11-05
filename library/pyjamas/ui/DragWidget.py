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
from pyjamas.ui.Widget import Widget
from pyjamas.ui.MouseListener import MouseHandler
from pyjamas.ui.DragHandler import DragHandler
from pyjamas.dnd import makeDraggable, DNDHelper
import pyjd

class DragWidget(object):
    """
        Mix-in class for a draggable widget.
        Override DragHandler on*** methods to enable drag behavior.

        At runtime, we change the implementation based on html5
        dra-and-drop capabilities of the engine.
    """
    pass


class DragContainer(object):
    """
    mixin providing drag handlers for contained draggables
    events bubble up to here.  event.target will be the actual draggable

    This class is the same as DragWidget, but does not make itself draggable.

    At runtime, we change the implementation based on html5
    drag-and-drop capabilities of the engine.
    """
    pass


class Draggable(Widget):
    def makeDraggable(self):
        makeDraggable(self)


class Html5DragContainer(Widget, DragHandler):
    def __init__(self, **kw):
        if (not hasattr(self, 'attached')) or kw:
            Widget.__init__(self, **kw)
        DragHandler.__init__(self)
        self.addDragListener(self)


class MouseDragContainer(Widget, MouseHandler, DragHandler):
    def __init__(self, **kw):
        if (not hasattr(self, 'attached')) or kw:
            Widget.__init__(self, **kw)
        MouseHandler.__init__(self)
        self.addMouseListener(DNDHelper.dndHelper)


class Html5DragWidget(Html5DragContainer, Draggable):
    def __init__(self, **kw):
        Html5DragContainer.__init__(self, **kw)
        self.makeDraggable()


class MouseDragWidget(MouseDragContainer, Draggable):
    def __init__(self, **kw):
        MouseDragContainer.__init__(self, **kw)
        self.makeDraggable()


def init(native=None):
    global DragWidget, DragContainer
    if native is None:
        html5_dnd = hasattr(DOM.createElement('span'), 'draggable')
    else:
        html5_dnd = native
    if html5_dnd:
        DragContainer = Html5DragContainer
        DragWidget = Html5DragWidget
    else:
        DragContainer = MouseDragContainer
        DragWidget = MouseDragWidget

if pyjd.is_desktop:
    init(pyjd.native_dnd)
else:
    init()

Factory.registerClass('pyjamas.ui.DragWidget', 'DragWidget', DragWidget)
Factory.registerClass('pyjamas.ui.DragWidget', 'DragContainer', DragContainer)
