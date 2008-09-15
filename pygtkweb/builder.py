#!/usr/bin/env python

import sys
import os
import compiler
from os.path import join, dirname, basename

sys.path.append(join(dirname(__file__), "../pyjs"))
import pyjs

app_platforms = ['ie6', 'opera', 'safari', 'moz', 'oldmoz']
app_library_dirs = ["../library/builtins", "../library", "../addons"]

def read_boilerplate(filename):
    return open(join(dirname(__file__), "boilerplate", filename)).read()

def create_output_dir(output):
    if os.path.exists(output) and not os.path.isdir(output):
        print >>sys.stderr, "Output destination %s exists and is not a directory" % output
        return
    if not os.path.isdir(output):
        try:
            print "Creating output directory"
            os.mkdir(output)
        except StandardError, e:
            print >>sys.stderr, "Exception creating output directory %s: %s" % (output, e)

def create_file(boiler, out_dir, out_name, dict=None):
    o = open(join(out_dir, out_name), 'w')
    b = read_boilerplate(boiler)
    if dict==None:
        print >>o, b
    else:
        print >>o, b % dict
    o.close()

def build(py_app_name, output="temp", notfound_callback=None):
    if py_app_name[-3:]==".py":
        app_name = basename(py_app_name[:-3])
    else:
        app_name = basename(py_app_name)

    create_output_dir(output)
    create_file('style.css',output,'style.css')
    create_file('index.html',output,'index.html',{'app_name':app_name})

    for platform in app_platforms:
        fname = app_name+'_'+platform+'.html'
        print 'Creating ',fname+'...',
        t = pyjs.Translator(app_library_dirs, notfound_callback=notfound_callback, platform=platform)
        app_code = t.translate(app_name)
        create_file('app.html',output,fname,{'app_code':app_code})
        print 'ok!'
