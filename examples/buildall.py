#!/usr/bin/env python
import os
import sys

options = " ".join(sys.argv[1:])
if not options:
    options = "-O"
for pyjsbuild in [\
                  '../bin/pyjsbuild.py', '../bin/pyjsbuild',
                  None
                 ]:
    if os.path.exists(pyjsbuild):
        break
if not pyjsbuild:
    sys.stderr.write("Cannot find pyjsbuild")
    sys.exit(1)

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
                        os.system("python ../%s %s %s" % (pyjsbuild, options, f))
                        #raw_input('Press any key')
        os.chdir("..")
