import pyjd
import time
import os
import gtk

def setup(uri):
    
    # create the browser-engine window, start loading the URL
    pyjd.setup(uri)
    while 1:
        if pyjd.is_loaded():
            return
        pyjd.run(one_event=True)

def run():
    pyjd.run()
