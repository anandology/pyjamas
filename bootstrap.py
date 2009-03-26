#!/usr/bin/python

""" simple creation of two commands, customised for your specific system.
    windows users get a corresponding batch file.  yippeeyaiyay.
"""
pyjsbuild = """#!/usr/bin/python

pth = '%s'

import os
import sys
sys.path[0:0] = [
  pth,
  ]

import pyjs, sys
pyjs.path += [os.path.join(pth, 'library'),
os.path.join(pth, 'library', 'builtins'),
os.path.join(pth, 'addons'),
]
sys.argv.extend(['-D', pth])

import pyjs.build

if __name__ == '__main__':
    pyjs.build.main()
"""

pyjscompile = """
#!/usr/bin/python

pth = '%s'

import os
import sys
sys.path[0:0] = [
  pth,
  ]

import pyjs
pyjs.path += [os.path.join(pth, 'library')]

import pyjs

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

def make_cmd(pth, cmdname, txt):

    if sys.platform == 'win32':
        cmd_name = cmdname + ".py"
    else:
        cmd_name = cmdname

    cmd = os.path.join("bin", cmd_name)
    if os.path.exists(cmd):
        os.unlink(cmd)
    f = open(cmd, "w")
    f.write(txt % pth)
    f.close()

    if hasattr(os, "chmod"):
        os.chmod(cmd, 0555)

    if sys.platform == 'win32':

        cmd = os.path.join("bin", cmdname)
        batcmd = "%s.bat" % cmd
        f = open(batcmd, "w")
        f.write(batcmdtxt % cmd_name)
        f.close()

pth = os.path.abspath(os.getcwd())

make_cmd(pth, "pyjsbuild", pyjsbuild)
make_cmd(pth, "pyjscompile", pyjscompile)

