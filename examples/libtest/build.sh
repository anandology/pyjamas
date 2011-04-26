#!/bin/sh
../../bin/pyjsbuild --no-compile-inplace --strict --dynamic '^I18N[.].*.._..' $@ LibTest `find I18N -name ??_??.py`
