"""
    Horizontal Split Panel: Left and Right layouts with a movable splitter.

/*
 * Copyright 2008 Google Inc.
 * Copyright 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
 * Copyright 2010 Rich Newpol <rich.newpol@gmail.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License") you may not
 * use this file except in compliance with the License. You may obtain a copy
 * of the License at
 *
 * http:#www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */
"""
from pyjamas.ui.SplitPanel import SplitPanel
from pyjamas import Factory


class HorizontalSplitPanel(SplitPanel):
    def __init__(self, **kwargs):
        # call base constructor
        SplitPanel.__init__(self, vertical=False, **kwargs)

    def setLeftWidget(self, leftWidget):
        self.setWidget(0, leftWidget)

    def getLeftWidget(self):
        return self.getWidget(0)

    def setRightWidget(self, rightWidget):
        self.setWidget(1, rightWidget)

    def getRightWidget(self):
        return self.getWidget(1)

Factory.registerClass('pyjamas.ui.HorizontalSplitPanel',
                        'HorizontalSplitPanel',
                        HorizontalSplitPanel)
