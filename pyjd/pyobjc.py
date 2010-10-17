# example code for starting off with a web browser in pyobjc

from PyObjCTools import NibClassBuilder, AppHelper
import WebKit
from Foundation import *
from AppKit import *

NibClassBuilder.extractClasses("MainMenu")

# class defined in MainMenu.nib
class MyObject(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSObject
    # The following outlets are added to the class:
    # url
    # webview

    def loadURL_(self, sender):
        urlString = self.url.stringValue()
        url = NSURL.URLWithString_(urlString)
        request = NSURLRequest.requestWithURL_(url)
        self.webview.mainFrame().loadRequest_(request)
        
if __name__ == "__main__":
    AppHelper.runEventLoop()

