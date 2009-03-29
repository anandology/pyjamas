#!/usr/bin/python

""" simple creation of two commands, customised for your specific system.
    windows users get a corresponding batch file.  yippeeyaiyay.
"""
pyjsbuild = """#!%s

pth = '%s'

import os
import sys
sys.path[0:0] = [
  pth,
  ]

import pyjs
pyjs.path += [os.path.join(pth, 'library'),
os.path.join(pth, 'library', 'builtins'),
os.path.join(pth, 'addons'),
]
sys.argv.extend(['-D', pth])

import pyjs.build

if __name__ == '__main__':
    pyjs.build.main()
"""

pyjscompile = """#!%s

pth = '%s'

import os
import sys
sys.path[0:0] = [
  pth,
  ]

import pyjs
pyjs.path += [os.path.join(pth, 'library')]

if __name__ == '__main__':
    pyjs.main()
"""

batcmdtxt = '''@echo off
set CMD_LINE_ARGS=
:setArgs
if ""%%1""=="""" goto doneSetArgs
set CMD_LINE_ARGS=%%CMD_LINE_ARGS%% %%1
shift
goto setArgs
:doneSetArgs

python %s %%CMD_LINE_ARGS%%
'''

import os
import sys

def make_cmd(prefix, pth, cmdname, txt):

    if sys.platform == 'win32':
        cmd_name = cmdname + ".py"
    else:
        cmd_name = cmdname

    p = os.path.join(prefix, "bin")
    if not os.path.exists(p):
        os.makedirs(p)

    cmd = os.path.join("bin", cmd_name)
    cmd = os.path.join(prefix, cmd)

    if os.path.exists(cmd):
        os.unlink(cmd)
    f = open(cmd, "w")
    f.write(txt % (sys.executable, pth))
    f.close()

    if hasattr(os, "chmod"):
        os.chmod(cmd, 0555)

    if sys.platform == 'win32':

        cmd = os.path.join("bin", cmdname)
        cmd = os.path.join(prefix, cmd)
        batcmd = "%s.bat" % cmd
        f = open(batcmd, "w")
        f.write(batcmdtxt % cmd_name)
        f.close()

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        pth = sys.argv[1]
    else:
        pth = os.path.abspath(os.getcwd())

    if len(sys.argv) == 3:
        prefix = sys.argv[2]
    else:
        prefix = "."

    make_cmd(prefix, pth, "pyjsbuild", pyjsbuild)
    make_cmd(prefix, pth, "pyjscompile", pyjscompile)

