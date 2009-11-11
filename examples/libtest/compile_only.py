#!/usr/bin/python
import sys
sys.path.insert(0, '../../pyv8')
import pyv8run
if "LibTest" not in sys.argv:
    sys.argv.append("LibTest")
pyv8run.build_script()
