#!/usr/bin/env python
""" Use this to help speed up manual conversion of e.g. GWT Java to e.g.
    Pyjamas python
"""

import sys

def java2pythonlinebyline(txt):
    if txt.find('if (') >= 0:
        txt = txt.replace('if (', 'if ')
        txt = txt.replace(') {', ':')
    return txt

def reindent(txt):
    res = ''
    indent = 0
    for l in txt.split("\n"):
        l = l.strip()
        if l.startswith("}"):
            indent -= 1
        res += '    ' * indent + l + "\n"
        if l.endswith("{"):
            indent += 1
    return res

def java2python(txt):
    txt = reindent(txt)
    txt = txt.replace("/*", '"""')
    txt = txt.replace("*/", '"""')
    txt = txt.replace("//", '#')
    txt = txt.replace("this.", 'self.')
    l = txt.split("\n")
    l = map(java2pythonlinebyline, l)
    return '\n'.join(l)

if __name__ == "__main__":
    fname = sys.argv[1]
    f = open(fname + ".java", "r")
    txt = java2python(f.read())
    f.close()

    f = open(fname + ".py", "w")
    f.write(txt)
    f.close()

