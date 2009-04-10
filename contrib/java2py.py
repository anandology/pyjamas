#!/usr/bin/env python
""" Use this to help speed up manual conversion of e.g. GWT Java to e.g.
    Pyjamas python
"""

import sys

def countspaces(txt):
    count = 0
    while count < len(txt) and txt[count] == ' ':
        count += 1
    return count
def java2pythonlinebyline(txt):
    if txt.find('if (') >= 0:
        txt = txt.replace('if (', 'if ')
        txt = txt.replace(') {', ':')
    elif txt.find('class ') >= 0 and txt.endswith("{"):
        txt = txt.replace('{', ':')
    elif txt.find('while (') >= 0:
        txt = txt.replace('while (', 'while ')
        txt = txt.replace(') {', ':')
    elif txt.find('for (') >= 0:
        txt = txt.replace('for (', 'for ')
        txt = txt.replace(') {', ':')
    count = countspaces(txt)
    if txt[count:].startswith("}"):
        txt = count * ' ' + txt[count+1:]

    if txt[count:].startswith("protected ") >= 0:
        txt = txt.replace("protected ", "")
    if txt[count:].startswith("public ") >= 0:
        txt = txt.replace("public ", "")
    if txt[count:].startswith("private ") >= 0:
        txt = txt.replace("private ", "")
    if txt[count:].startswith("static ") >= 0:
        txt = txt.replace("static ", "")
    if txt[count:].startswith("final ") >= 0:
        txt = txt.replace("final ", "")
    return txt

def reindent(txt):
    """ reindents according to { and } braces.  strips all whitespace,
        possibly not smartest thing to do.  oh well.
    """
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
    txt = txt.replace("<>", '!=')
    txt = txt.replace("null", 'None')
    txt = txt.replace("true", 'True')
    txt = txt.replace("false", 'False')
    txt = txt.replace("//", '#')
    txt = txt.replace("this.", 'self.')
    txt = txt.replace("else if", 'elif')
    txt = txt.replace("new ", '')
    l = txt.split("\n")
    l = map(java2pythonlinebyline, l)
    txt = txt.replace("}", '')
    return '\n'.join(l)

if __name__ == "__main__":
    fname = sys.argv[1]
    f = open(fname + ".java", "r")
    txt = java2python(f.read())
    f.close()

    f = open(fname + ".py", "w")
    f.write(txt)
    f.close()

