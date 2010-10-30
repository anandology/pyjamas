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
from pyjamas.dnd import html5_dnd, makeDraggable, DNDHelper
from pyjamas.ui.MouseListener import MouseHandler
from pyjamas.ui.DragHandler import DragHandler
from pyjamas.ui.Widget import Widget

if not html5_dnd:
    dndHelper = DNDHelper.dndHelper

class DragWidget(Widget, DragHandler, MouseHandler):
    """
        Mix-in class for a draggable widget.
        Override DragHandler on*** methods to enable drag behavior.

        create


    """
    def __init__(self, **kw):
        if (not hasattr(self, 'attached')) or kw:
            Widget.__init__(self, **kw)
        self.html5_dnd = html5_dnd
        self.makeDraggable()
        if self.html5_dnd:
            DragHandler.__init__(self)
            self.addDragListener(self)
        else:
            MouseHandler.__init__(self)
            self.addMouseListener(dndHelper)

    def makeDraggable(self):
        makeDraggable(self)


class DragContainer(DragWidget):
    """
    mixin providing drag handlers for contained draggables
    events bubble up to here.  event.target will be the actual draggable

    This class is the same as dragWidget, but does to make itself draggable.
    """
    def makeDraggable(self):
        pass


Factory.registerClass('pyjamas.ui.DragWidget', 'DragWidget', DragWidget)
Factory.registerClass('pyjamas.ui.DragWidget', 'DragContainer', DragContainer)
