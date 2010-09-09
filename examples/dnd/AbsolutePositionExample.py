#"""
#* Copyright 2009 Fred Sauer
#*
#* Licensed under the Apache License, Version 2.0 (the "License"); you may not
#* use this file except in compliance with the License. You may obtain a copy of
#* the License at
#*
#* http:#www.apache.org/licenses/LICENSE-2.0
#*
#* Unless required by applicable law or agreed to in writing, software3
#* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#* License for the specific language governing permissions and limitations under
#* the License.
#"""


from pyjamas.ui.AbsolutePanel import AbsolutePanel

from pyjamas.dnd import PickupDragController
from pyjamas.dnd.drop import AbsolutePositionDropController


"""*
* {@link com.allen_sauer.gwt.dnd.client.drop.AbsolutePositionDropController}
* example.
"""

# XXX must import Example class - it provides e.g.the createDraggable function
class AbsolutePositionExample(Example):
    
    CSS_DEMO_ABSOLUTE_POSITION_EXAMPLE = "demo-AbsolutePositionExample"
    
    def __init__(self, dragController):

        Example.__init__(self, dragController)
        self.addStyleName(self.CSS_DEMO_ABSOLUTE_POSITION_EXAMPLE)
        
        # use the drop target as this composite's widget
        positioningDropTarget = AbsolutePanel()
        positioningDropTarget.setPixelSize(400, 200)
        self.setWidget(positioningDropTarget)
        
        # instantiate our drop controller
        self.absposdc = AbsolutePositionDropController(positioningDropTarget)
        dragController.registerDropController(self.absposdc)
    
    
    def getDescription(self):
        return "Draggable widgets can be placed anywhere on the gray drop target."

    
    def getInvolvedClasses(self):
        return [AbsolutePositionExample, AbsolutePositionDropController]
    
    
    def onInitialLoad(self):
        self.absposdc.drop(self.createDraggable(), 10, 30)
        self.absposdc.drop(self.createDraggable(), 60, 8)
        self.absposdc.drop(self.createDraggable(), 190, 60)
    


