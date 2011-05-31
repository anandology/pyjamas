#!/usr/bin/env python
"""
Generate stdlib/ from pyjs/lib, /usr/lib/python and pypy/lib
"""

import os
import sys
import shutil
from os.path import join, dirname, basename, abspath, exists, isdir
from optparse import OptionParser

root_path = dirname(abspath(__file__))
pyjslib_path = join(root_path, 'pyjs', 'src', 'pyjs', 'lib')
dest_path = join(root_path, 'stdlib')

pyjslib_excludes = ['output']
pypy_excludes = ['site-packages']
cpython_excludes = ['site-packages', 'lib-dynload', 'test']

mod_src = {}
def copy_libs(dest, src, src_name, excludes):
    for p in os.listdir(src):
        if isdir(join(src, p)):
            mod_name = p
        elif p.endswith('.py'):
            mod_name = p.split('.')[0]
        else:
            continue
        
        if (not exists(join(dest, mod_name)) and 
            not exists(join(dest, mod_name + '.py')) and
            not mod_name in excludes):
            if isdir(join(src, p)):
                shutil.copytree(join(src, p), join(dest, p))
            else:
                shutil.copy2(join(src, p), join(dest, p))
            mod_src[mod_name] = src_name
            

def main():
    parser = OptionParser()
    parser.add_option(
        "--pypy",
        dest="pypy",
        help="Path to PyPy libraries")
    parser.add_option(
        "--cpython",
        dest="cpython",
        help="Path to CPython libraries")
    
    options, args = parser.parse_args()
    if not options.cpython:        
        cpython_path = dirname(os.__file__)
    else:
        cpython_path = options.cpython
    
    pypy_path = options.pypy
    
    print ("Exporting data from:\n"
           "PyJS lib: {0}\nPyPy lib: {2}\nCPython lib: {1}\n".
           format(pyjslib_path, cpython_path, pypy_path))
    
    if exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)
    
    copy_libs(dest_path, pyjslib_path, 'pyjs', pyjslib_excludes)
    if pypy_path:
        copy_libs(dest_path, pypy_path, 'pypy', pypy_excludes)
    copy_libs(dest_path, cpython_path, 'cpython', cpython_excludes)
    f_mod_src = open(join(dest_path, 'modules_sources'), 'w')
    for mod, src in mod_src.iteritems():
        f_mod_src.write("{}:{}\n".format(mod, src))
    f_mod_src.close()
        
    
if __name__ == '__main__':
    main()