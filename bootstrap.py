#!/usr/bin/python

""" simple creation of two commands, customised for your specific system.
    windows users get a corresponding batch file.  yippeeyaiyay.
"""
pyjsbuild = """#!%s

pyjspth = r'%s'

import os
import sys
sys.path[0:0] = [
  r'%s',
  ]

import pyjs
pyjs.path += [os.path.join(pyjspth, 'library'),
os.path.join(pyjspth, 'library', 'builtins'),
os.path.join(pyjspth, 'addons'),
]
sys.argv.extend(['-D', pyjspth])

import pyjs.build

if __name__ == '__main__':
    pyjs.build.main()
"""

pyjscompile = """#!%s

pyjspth = r'%s'

import os
import sys
sys.path[0:0] = [
  r'%s',
  ]

import pyjs
pyjs.path += [os.path.join(pyjspth, 'library')]

if __name__ == '__main__':
    pyjs.main()
"""

pyjdinit = """
pyjdinitpth = r'%s'

import os
import sys
import ConfigParser

sys.path += [os.path.join(pyjdinitpth, 'library')]

cp = os.environ.get('HOME', '.')
cp = os.path.join(cp, ".pyjd")
cp = os.path.join(cp, "pyjdrc")
cfg = ConfigParser.ConfigParser()
try:
    cfg.read(cp)
    try:
        engine = cfg.get('gui', 'engine')
    except ConfigParser.NoOptionError:
        engine = 'hulahop'
except:
    engine = 'hulahop'
if engine == 'pywebkitgtk':
    from pywebkitgtk import *
elif engine == 'hulahop':
    from hula import *
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

def make_cmd(prefix, pth, pyjspth, cmdname, txt):

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
    f.write(txt % (sys.executable, pyjspth, pth))
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

    pyjspth = pth
    if len(sys.argv) == 3:
        prefix = sys.argv[2]
    elif len(sys.argv) == 4:
        prefix = sys.argv[3]
        pyjspth = sys.argv[2]
    else:
        prefix = "."

    make_cmd(prefix, pth, pyjspth, "pyjsbuild", pyjsbuild)
    make_cmd(prefix, pth, pyjspth, "pyjscompile", pyjscompile)

    # create pyjd/__init__.py
    pyjdinitpth = os.path.join("pyjd", "__init__.py")
    f = open(pyjdinitpth, "w")
    f.write(pyjdinit % pyjspth)
    f.close()
