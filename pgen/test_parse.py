import os
import sys
import traceback
from lib2to3.pgen2.parse import Parser
from lib2to3.pgen2.driver import Driver
#from parse_tables import Grammar
from lib2to3.pgen2.driver import load_grammar
g = load_grammar("Grammar.txt")

from astpprint import getAststr, printAst
from lib2to3 import pytree

from lib2to3.compiler.transformer import Transformer

#g = Grammar()

import compiler
import parser

def compare_compilers(fname):

    path, fname_out = os.path.split(fname)

    #file = open(fname)
    #s = parser.suite(file.read())
    #print "tuple", s.totuple()

    try:
        x1 = compiler.parseFile(fname)
        ys1 = getAststr(x1)
    except SyntaxError:
        ys1 = traceback.format_exc(limit=0)
        

    d = Driver(g )

    try:
        x = d.parse_file(fname)
        t = Transformer()
        y = t.compile_node(x)
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

