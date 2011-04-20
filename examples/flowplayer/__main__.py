#!/usr/bin/env python
# -*- coding: utf-8 -*-


TARGETS = {
    'fp.py': dict(options=[
        '--output=html',
    ]),
}


PACKAGE = {
    'title': 'FlowPlayer',
    'desc': 'Use of flash component flowplayer',
}


def setup(targets):
    '''Setup example for translation, MUST call util.setup(targets).'''
    util.setup(targets)


def translate():
    '''Translate example, MUST call util.translate().'''
    util.translate()


def install(package):
    '''Install and cleanup example module. MUST call util.install(package)'''
    util.install(package)


##---------------------------------------##
# --------- (-: DO NOT EDIT :-) --------- #
##---------------------------------------##


import sys
import os


head = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(head, '..'))
from _examples import util
sys.path.pop(0)

util.init(head)

setup(TARGETS)
translate()
install(PACKAGE)
