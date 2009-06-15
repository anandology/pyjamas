#!/bin/sh
options="$*"
if [ -z $options ] ; then options="-O";fi
../../bin/pyjsbuild $* TestRect.py
options="$*"
if [ -z $options ] ; then options="-O";fi
../../bin/pyjsbuild $* TestDict.py
