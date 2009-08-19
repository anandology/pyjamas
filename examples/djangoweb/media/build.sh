#!/bin/sh
# you will need to read the top level README, and run boostrap.py
# and buildout in order to make pyjsbuild

rm -fr output/

options="$*"
if [ -z $options ] ; then options="-O";fi
../../../bin/pyjsbuild $options  -j public/fckeditor/fckeditor.js WebPage
