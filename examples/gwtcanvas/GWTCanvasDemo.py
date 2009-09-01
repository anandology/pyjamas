"""
* Copyright 2008 Google Inc.
*
* Licensed under the Apache License, Version 2.0 (the "License"); you may not
* use this file except in compliance with the License. You may obtain a copy of
* the License at
*
* http:#www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
* License for the specific language governing permissions and limitations under
* the License.
"""

import pyjd

from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Widget import Widget

from pyjamas.Canvas.GWTCanvas import GWTCanvas

from StaticDemo import StaticDemo
from LogoDemo import LogoDemo

"""*
* Simple demo of the GWTCanvas Widget.
*
* Selection box at top to choose demo.
* Single shared GWT Canvas in middle.
* Optional control panel at bottom for demo descriptions
* and demo UI controls
*
* Entry point classes define <code>onModuleLoad()</code>.
*
"""
class GWTCanvasDemo:


    def onModuleLoad(self):

        self.layout = HorizontalPanel()

        # Each demo will set their own dimensions, so it doesn't matter
        # what we initialize the canvas to.
        canvas = GWTCanvas(400,400)

        canvas.addStyleName("gwt-canvas")

        self.demos = []
        # Create demos
        self.demos.append(StaticDemo(canvas))
        self.demos.append(LogoDemo(canvas))
        #self.demos.append(ParticleDemo(canvas))
        #self.demos.append(GradientDemo(canvas))
        #self.demos.append(SuiteDemo(canvas))

        # Add them to the selection list box
        lb = ListBox()
        lb.setStyleName("listBox")

        for i in range(len(self.demos)):
            lb.addItem(self.demos[i].getName())

        lb.addChangeListener(self)

        # start off with the first demo
        self.currentDemo = self.demos[0]

        # Add widgets to self.layout and RootPanel
        vp = VerticalPanel()
        vp.add(lb)
        vp.add(canvas)
        self.layout.add(vp)
        if self.currentDemo.getControls() is not None:
            self.layout.add(self.currentDemo.getControls())

        RootPanel().add(self.layout)
        self.currentDemo.drawDemo()

    def onChange(self, listBox):
        choice = listBox.getSelectedIndex()
        self.swapDemo(self.demos[choice])


    """
    * Changes the current demo for the input demo
    """
    def swapDemo(self, newDemo):
        self.currentDemo.stopDemo()
        self.layout.remove(self.currentDemo.getControls())
        self.currentDemo = newDemo
        self.layout.add(self.currentDemo.getControls())
        self.currentDemo.drawDemo()

if __name__ == '__main__':
    pyjd.setup("./public/GWTCanvasDemo.html")
    app =  GWTCanvasDemo()
    app.onModuleLoad()
    pyjd.run()

