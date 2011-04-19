#!/bin/sh
# you will need to read the top level README, and run boostrap.py
# and buildout in order to make pyjsbuild

options="$*"
#if [ -z $options ] ; then options="-O";fi
for f in events graffle raphael_showcase spinner test ; do
	../../bin/pyjsbuild --print-statements $options $f
done
