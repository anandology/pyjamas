#!/usr/bin/env python
# -*- coding: utf-8 -*-


TARGETS = [
    'Hello.py',
]


def prepare():
    '''Prepare example for translation before util.setup() is called'''
    pass


def translate():
    '''Translate example'''
    util.translate()


def finalize():
    '''Cleanup example'''
    pass


#####################################
# ---------- DO NOT EDIT ---------- #
#####################################


import sys
import os


head = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(head, '..'))
import _util as util
sys.path.pop(0)

prepare()
util.setup(head, TARGETS)
translate()
finalize()
