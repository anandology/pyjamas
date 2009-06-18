#!/bin/sh
options="$*"
if [ -z $options ] ; then options="-O";fi
../../bin/pyjsbuild $options TestRect.py
options="$*"
if [ -z $options ] ; then options="-O";fi
../../bin/pyjsbuild $options TestDict.py
