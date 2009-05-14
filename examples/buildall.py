#!/usr/bin/env python
import os

for d in os.listdir('.'):
    if os.path.isdir(d):
        os.chdir(d)
        for f in os.listdir("."):
            if os.path.isfile(f):
                split = f.split(".")
                if len(split) > 1:
                    name, ext = split[0], split[1]
                    
                    if name.lower() in d.lower() and ext == "py":
                        print("********** Building %s **********" % name.upper())
                        os.system("python ../../bin/pyjsbuild.py %s" % f)
                        #raw_input('Press any key')
        os.chdir("..")
