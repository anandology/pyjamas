# Picasaweb/gdata access using pyjamas demo
#
# Copyright (C) 2011 James Hedley (jameskhedley@gmail.com)
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
#
# Distributed as part of pyjamas (http://pyjs.org)

import pyjd # dummy in pyjs
from Photos import Photos
from pyjamas.ui.RootPanel import RootPanel


class PicasaWeb:
    def onModuleLoad(self):
        self.photos=Photos() 
        RootPanel().add(self.photos)
    

if __name__ == '__main__':
    # for pyjd, set up a web server and load the HTML from there:
    # this convinces the browser engine that the AJAX will be loaded
    # from the same URI base as the URL, it's all a bit messy...
    pyjd.setup("public/PicasaWeb.html")
    app = PicasaWeb()
    app.onModuleLoad()
    pyjd.run()

