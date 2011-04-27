#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
head = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(head))
import compile
sys.path.pop(0)
oldpath = os.getcwd()
os.chdir(head)
compile.main()
os.chdir(oldpath)
del(oldpath)


TARGETS = {
    'Showcase.py': dict(
        path='src',
    )
}


PACKAGE = {
    'title': 'showcase',
    'desc': 'Showcase example',
}


def setup(targets):
    '''Setup example for translation, MUST call util.setup(targets).'''
    util.setup(targets)


def translate():
    '''Translate example, MUST call util.translate().'''
    #util.translate()
    pass


def install(package):
    '''Install and cleanup example module. MUST call util.install(package)'''
    util.install(package)


##---------------------------------------##
# --------- (-: DO NOT EDIT :-) --------- #
##---------------------------------------##


import sys
import os


examples = head = os.path.abspath(os.path.dirname(__file__))
while os.path.split(examples)[1].lower() != 'examples':
    examples = os.path.split(examples)[0]
    if not examples:
        raise ValueError("Cannot determine examples directory")
sys.path.insert(0, os.path.join(examples))
from _examples import util
sys.path.pop(0)

util.init(head)

setup(TARGETS)
translate()
install(PACKAGE)
