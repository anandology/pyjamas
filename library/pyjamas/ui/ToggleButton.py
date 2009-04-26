# Copyright Pyjamas Team
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from pyjamas.ui.CustomButton import CustomButton

class ToggleButton (CustomButton):
    """
    A ToggleButton is a stylish stateful button which allows the
    user to toggle between UP and DOWN states.
    
    CSS: .gwt-ToggleButton-
    up/down/up-hovering/down-hovering/up-disabled/down-disabled
    {.html-face}
    """
    STYLENAME_DEFAULT = "gwt-ToggleButton"
    
    
    def __init__(self, upImageText = None, downImageText=None, handler = None):
        """
        Constructor for ToggleButton.
        """
        CustomButton.__init__(self, upImageText, downImageText, handler)
        self.setStyleName(self.STYLENAME_DEFAULT)

    
    def onClick(self):
        self.toggleDown()
        CustomButton.onClick(self)
    
