import os
import sys
import traceback

from astpprint import getAststr, printAst

from lib2to3 import compiler as test_compiler
from lib2to3.compiler.transformer import Transformer
from lib2to3.compiler import parser as test_parser

#g = Grammar()

import compiler
import parser

def compare_compilers(fname):

    path, fname_out = os.path.split(fname)

    f = open(fname)
    txt = f.read()
    f.close()

    try:
        x1 = compiler.parseFile(fname)
        ys1 = getAststr(x1)
    except SyntaxError:
        ys1 = traceback.format_exc(limit=0)
        

    try:
        #x = test_parser.suite(txt)
        #t = Transformer()
        #y = t.compile_node(x)
        y = test_compiler.parseFile(fname)
        ys = getAststr(y)

    except SyntaxError:
        ys = traceback.format_exc(limit=1)
        #traceback.print_exc()

    if ys == ys1:
        print "passed"
        return

    print "failed."

    f = open(fname_out+".ast", "w")
    f.write(ys)
    f.close()

    f = open(fname_out+".ast.std", "w")
    f.write(ys1)
    f.close()

import sys
for arg in sys.argv[1:]:
    print "test file", arg
    try:
        compare_compilers(arg)
    except:
        print >> sys.stderr, "exception in compile of ", arg
        traceback.print_exc()
        sys.stderr.flush()

