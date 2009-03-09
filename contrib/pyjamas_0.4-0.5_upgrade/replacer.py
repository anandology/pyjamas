#!/usr/bin/env python

import sys
import os

def rewritefile(p):
    f = open(p)
    res = ''
    searchfor = "from pyjamas.ui import "
    sl = len(searchfor)
    for l in f.readlines():
        if l.startswith(searchfor):
            mods = l[sl:-1]
            l = ''
            for modname in mods.split(","):
                modname = modname.strip()
                if modname.startswith("Has") and modname.endswith("Alignment"):
                    l += "from pyjamas.ui import %s\n" % (modname)
                else:
                    l += "from pyjamas.ui.%s import %s\n" % (modname, modname)
        res += l
    f = open(p, "w")
    f.write(res)
    f.close()

for p in os.listdir("."):
    if p.endswith(".py"):
        rewritefile(p)


