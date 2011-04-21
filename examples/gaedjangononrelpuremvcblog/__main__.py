#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

head = os.path.dirname(__file__)
puremvc = os.path.join(head, '..', 'employeeadmin')

TARGETS = {
    'Blog.py': dict(
        path='media',
        options=[
            '--library_dir',
            os.path.join(puremvc, 'PureMVC_Python_1_2', 'src'),
        ],
        downloads=[
            dict(
                url='http://puremvc.org/pages/downloads/Python/PureMVC_Python.zip',             
                dst=os.path.join(puremvc, 'PureMVC_Python.zip'),
                unzip=True,
            )
        ],
    ),
}


PACKAGE = {
    'title': 'GAE django-nonrel puremvc blog',
    'desc': 'Combines concepts from django-nonrel, puremvc and google app engine.',
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
#util.init(os.path.join(head, 'media'))

setup(TARGETS)
translate()
install(PACKAGE)
