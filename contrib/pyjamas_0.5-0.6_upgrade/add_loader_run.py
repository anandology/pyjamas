#!/usr/bin/env python
#
# appends onModuleLoad thingy onto application
# pyjamas 0.5 no longer automatically calls onModuleLoad
#

import sys

txt = open(sys.argv[1] + ".py", "r").read()

f = open(sys.argv[1] + ".py", "w")

# assume that app has __main__ as last bit.

f.write("""
from pyjamas import loader
%s
    loader.run()
""" % txt)

f.close()

