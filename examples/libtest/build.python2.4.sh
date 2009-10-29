#!/bin/sh
python2.4 ../../bin/pyjsbuild --internal-ast --dynamic \
          '^I18N[.].*.._..' $@ LibTest `find I18N -name ??_??.py`
