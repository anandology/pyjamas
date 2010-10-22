#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import subprocess

import _util


head = os.path.dirname(__file__)
examples = [
    example
    for example in os.listdir(head)
        if os.path.isfile(os.path.join(head, example, '__main__.py'))
            and not example.startswith('_')
]

env = os.environ.copy()
env.setdefault('PYJS_BIN_PYTHON', _util._find_python())
env.setdefault('PYJS_BIN_PYJSBUILD', _util._find_pyjsbuild(head))

for example in examples:
    header = ''.ljust(10, '-') + ' Building {0} '
    header = header.format(example.upper()).ljust(69, '-') + '\n'
    sys.stdout.write(header)
    sys.stdout.flush()
    e = subprocess.Popen([env['PYJS_BIN_PYTHON'], os.path.join(head, example)] + sys.argv[1:], env=env)
    e.wait()
