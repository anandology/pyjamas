#!/bin/sh
# you will need to read the top level README, and run boostrap.py
# and buildout in order to make pyjsbuild

ln -s ./output ./static

options="$*"
#if [ -z $options ] ; then options="-O";fi
../../../bin/pyjsbuild --print-statements $options Wiki

