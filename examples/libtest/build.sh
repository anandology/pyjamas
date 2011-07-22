#!/bin/sh
../../bin/pyjsbuild --no-compile-inplace --strict --dynamic '^I18N[.].*.._..' $@ LibTest `find I18N -name ??_??.py`
# For --translator=dict
#  - disable the generator test for now (will hang forever)
#  - comment second line
#  - uncomment last line
#  - invoke with ./build.sh --translator=dict
#../../bin/pyjsbuild --no-compile-inplace --strict $@ LibTest
