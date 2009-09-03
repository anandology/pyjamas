#!/bin/sh
../../bin/pyjsbuild --dynamic '^I18N[.].*.._..' $@ LibTest `find I18N -name ??_??.py`
