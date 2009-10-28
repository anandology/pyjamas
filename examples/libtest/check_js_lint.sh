#!/bin/bash

./build.sh

./pyv8test.sh | grep 'Passed.*failed'

BULK=output/some_in_one.js

cat output/lib/*.js > $BULK

python -c "
import sys
sys.path.insert(0, '../../pyjs/src')
from pyjs import sm
f = file('$BULK', 'r')
bulk = f.read()
f.close()

bulk += '''
\$pyjs.loaded_modules['pyjslib'] = function () {};
\$pyjs.loaded_modules['pyjslib'].___import___ = function () {};
'''

f = file('$BULK', 'w')
f.write('load = function() {};\n')
f.write(sm.APP_TEMPLATE % {'available_modules': '[]', 'app_name':'test', 
                        'module_files': '[]', 'js_lib_files': '[]',
                        'late_static_js_libs': bulk})
f.close()
"

# get the lint from http://www.javascriptlint.com/
wine /tmp/jsl/jsl.exe -conf jsl.pyjs.conf -process $BULK

