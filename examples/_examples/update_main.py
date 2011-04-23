#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

head = os.path.dirname(__file__)
if not head:
    head = '.'
examples = os.path.abspath(head)
while os.path.split(examples)[1].lower() != 'examples':
    examples = os.path.split(examples)[0]
    if not examples:
        raise ValueError("Cannot determine examples directory")

paths = os.listdir('.')
paths.sort()
for path in paths:
    if not os.path.isdir(path):
        continue
    mainpy = os.path.join(path, '__main__.py')
    if not os.path.exists(mainpy):
        continue
    tpl = open(os.path.join(examples, '_examples', 'template', '__main__.static.tpl')).read()
    data = open(mainpy, 'r').read()
    i = data.find(tpl[:80])
    if i < 0:
        raise ValueError("Cannot find template start in '%s'" % mainpy)
    data = data[:i] + tpl
    open(mainpy, 'w').write(data)
