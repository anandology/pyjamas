#!/usr/bin/env python
""" Use this to help speed up manual conversion of e.g. GWT Java to e.g.
    Pyjamas python

    TODO: in java2pythonlinebyline and redofunctions, identify a list
    of variables and functions, and do replace "variable" with "self.variable"
"""

import sys
import string

def countspaces(txt):
    count = 0
    while count < len(txt) and txt[count] == ' ':
        count += 1
    return count

def java2pythonlinebyline(txt):
    if txt.find('if (') >= 0:
        txt = txt.replace('if (', 'if ')
        txt = txt.replace('!', 'not ')
        txt = txt.replace('not =', '!=') # whoops
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
        # TODO: check if "class" in current line, add class name
        # otherwise assume last word of line is variable
        txt = txt.replace("protected ", "")
    if txt[count:].startswith("public ") >= 0:
        # TODO: check if "class" in current line, add class name
        # otherwise assume last word of line is variable
        txt = txt.replace("public ", "")
    if txt[count:].startswith("private ") >= 0:
        # TODO: check if "class" in current line, add class name
        # otherwise assume last word of line is variable e.g.
        # private final Area >>>targetArea<<<;
        txt = txt.replace("private ", "")
    if txt[count:].startswith("static ") >= 0:
        txt = txt.replace("static ", "")
    if txt[count:].startswith("final ") >= 0:
        txt = txt.replace("final ", "")
    if txt.endswith(";"):
        txt = txt[:-1]
    if txt.endswith(" :"):
        txt = txt[:-2] + ":"

    return txt

def redofunctions(txt):
    if not txt.endswith("{"):
        return txt
    lbr = txt.find("(")
    rbr = txt.find(") {")
    if lbr == -1 or rbr == -1 or lbr > rbr:
        return txt
    count = countspaces(txt)
    pre = txt[count:lbr]
    args = txt[lbr+1:rbr]

    pre = map(string.strip, pre.split(' '))
    if len(pre) == 1: # assume it's a constructor
        pre = '__init__'
    elif len(pre) == 2:
        pre = pre[-1] # drop the first word (return type)
    else:
        error # deliberately cause error - investigate 3-word thingies!

    args = map(string.strip, args.split(','))
    newargs = []
    for arg in args:
        if arg == '':
            continue
        arg = map(string.strip, arg.split(' '))
        if len(arg) == 2:
            newargs.append(arg[1]) # drop first word (arg type)
        else:
            print pre, args, arg
            error # deliberately cause error - find out why arg no type
    if count != 0:
        # assume class not global function - add self
        newargs = ['self'] + newargs
    newargs = ', '.join(newargs)
    return "%sdef %s(%s):" % (count*' ', pre, newargs)

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
    txt = txt.replace("!= None", 'is not None')
    txt = txt.replace("== None", 'is None')
    txt = txt.replace("throw ", 'raise ')
    txt = txt.replace("true", 'True')
    txt = txt.replace("false", 'False')
    txt = txt.replace("//", '#')
    txt = txt.replace("this.", 'self.')
    txt = txt.replace("else if", 'elif')
    txt = txt.replace("new ", '')
    l = txt.split("\n")
    l = map(java2pythonlinebyline, l)
    l = map(redofunctions, l)
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

