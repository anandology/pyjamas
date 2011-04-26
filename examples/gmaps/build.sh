#!/bin/sh
# you will need to read the top level README, and run boostrap.py
# and buildout in order to make pyjsbuild

options="$*"
#if [ -z $options ] ; then options="-O";fi
../../bin/pyjsbuild --print-statements $options MapSimple.py
../../bin/pyjsbuild --print-statements $options ControlDisableUI.py
../../bin/pyjsbuild --print-statements $options ControlOptions.py
../../bin/pyjsbuild --print-statements $options ControlSimple.py
../../bin/pyjsbuild --print-statements $options DirectionsSimple.py
../../bin/pyjsbuild --print-statements $options EventArguments.py
../../bin/pyjsbuild --print-statements $options EventClosure.py
../../bin/pyjsbuild --print-statements $options EventProperties.py
../../bin/pyjsbuild --print-statements $options EventSimple.py
../../bin/pyjsbuild --print-statements $options GeocodingSimple.py
../../bin/pyjsbuild --print-statements $options MapSimple.py
