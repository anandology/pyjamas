"""
* Copyright 2008 Google Inc.
* Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
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


from pyjamas.ui.Composite import Composite


"""*
* Simple abstract class for defining a demo for
* GWTCanvasDemo. Demos should involve a single
* canvas only which is shared amongst all other
* demos in the suite.
*
*"""
class SimpleCanvasDemo:

    def __init__(self, theCanvas):
        self.height = 400
        self.width = 400
        self.canvas = theCanvas
        self.controls = None

    def getControls(self):
        if self.controls is None:
            self.createControls()

        return self.controls


    def getName(self):
        return self.demoName


