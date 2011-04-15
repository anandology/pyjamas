import pyjd

from BrowserDetect import BrowserDetect

if __name__ == '__main__':
    pyjd.setup("./BrowserDetect.html")
    app = BrowserDetect()
    app.onModuleLoad()
    pyjd.run()
