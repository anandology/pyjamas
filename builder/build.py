#!/usr/bin/env python

import sys
import os
import shutil
from os.path import join, dirname, basename
from optparse import OptionParser

sys.path.append(join(dirname(__file__), "../pyjs"))
import pyjs


usage = """
  usage: %prog [options] <application name>

This is the command line builder for the pyjamas project, which can be used to 
build Ajax applications from Python.
For more information, see the website at http://pyjamas.pyworks.org/
"""

# GWT1.2 Impl  | GWT1.2 Output         | Pyjamas 0.2 Platform | Pyjamas 0.2 Output
# -------------+-----------------------+----------------------+----------------------
# IE6          | ie6                   | IE6                  | ie6
# Opera        | opera                 | Opera                | opera
# Safari       | safari                | Safari               | safari
# --           | gecko1_8              | Mozilla              | mozilla
# --           | gecko                 | OldMoz               | oldmoz
# Standard     | all                   | (default code)       | all
# Mozilla      | gecko1_8, gecko       | --                   | --
# Old          | safari, gecko, opera  | --                   | --

version = "%prog pyjamas version 2006-08-19"
app_platforms = ['IE6', 'Opera', 'OldMoz', 'Safari', 'Mozilla']
app_library_dirs = ["../library/builtins", "../library", "../addons"]


def read_boilerplate(filename):
    return open(join(dirname(__file__), "boilerplate", filename)).read()


def copy_boilerplate(filename, output_dir):
    filename = join(dirname(__file__), "boilerplate", filename)
    shutil.copy(filename, output_dir)


# taken and modified from python2.4
def copytree_exists(src, dst, symlinks=False):
    if not os.path.exists(src):
        return
    
    names = os.listdir(src)
    try:
        os.mkdir(dst)
    except:
        pass

    errors = []
    for name in names:
        if name.startswith('.svn'):
            continue

        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree_exists(srcname, dstname, symlinks)
            else:
                shutil.copy2(srcname, dstname)
        except (IOError, os.error), why:
            errors.append((srcname, dstname, why))
    if errors:
        print errors


def build(app_name, output="output", js_includes=()):
    dir_public = "public"

    print "Building '%(app_name)s' to output directory '%(output)s'" % locals()

    # check the output directory
    if os.path.exists(output) and not os.path.isdir(output):
        print >>sys.stderr, "Output destination %s exists and is not a directory" % output
        return
    if not os.path.isdir(output):
        try:
            print "Creating output directory"
            os.mkdir(output)
        except StandardError, e:
            print >>sys.stderr, "Exception creating output directory %s: %s" % (output, e)

    # Check that the app_name file exists
    py_app_name = app_name[:]
    if py_app_name[-2:] != "py":
        py_app_name = app_name + ".py"
    if app_name[-3:] == ".py":
        app_name = app_name[:-3]
    app_basename = basename(app_name)
    
    if not os.path.isfile(py_app_name):
        print >>sys.stderr, "Could not find %s" % py_app_name
        return

    ## public dir
    print "Copying: public directory"
    copytree_exists(dir_public, output)

    ## AppName.html - can be in current or public directory
    html_input_filename = app_name + ".html"
    html_output_filename = join(output, basename(html_input_filename))
    if os.path.isfile(html_input_filename):
        if not os.path.isfile(html_output_filename) or os.path.getmtime(html_input_filename) > os.path.getmtime(html_output_filename):
            try:
                shutil.copy(html_input_filename, html_output_filename)
            except:
                print >>sys.stderr, "Warning: Missing module HTML file %s" % html_input_filename
    
            print "Copying: %(html_input_filename)s" % locals()

    ## pygwt.js
    
    print "Copying: pygwt.js"

    pygwt_js_template = read_boilerplate("pygwt.js")
    pygwt_js_output = open(join(output, "pygwt.js"), "w")
    
    print >>pygwt_js_output, pygwt_js_template
    
    pygwt_js_output.close()

    ## Images
    
    print "Copying: Images and History"
    copy_boilerplate("corner_dialog_topleft_black.png", output)
    copy_boilerplate("corner_dialog_topright_black.png", output)
    copy_boilerplate("corner_dialog_bottomright_black.png", output)
    copy_boilerplate("corner_dialog_bottomleft_black.png", output)
    copy_boilerplate("corner_dialog_edge_black.png", output)
    copy_boilerplate("corner_dialog_topleft.png", output)
    copy_boilerplate("corner_dialog_topright.png", output)
    copy_boilerplate("corner_dialog_bottomright.png", output)
    copy_boilerplate("corner_dialog_bottomleft.png", output)
    copy_boilerplate("corner_dialog_edge.png", output)
    copy_boilerplate("tree_closed.gif", output)
    copy_boilerplate("tree_open.gif", output)
    copy_boilerplate("tree_white.gif", output)
    copy_boilerplate("history.html", output)
    
    ## AppName.nocache.html
    
    print "Creating: %(app_basename)s.nocache.html" % locals()
    
    home_nocache_html_template = read_boilerplate("home.nocache.html")
    home_nocache_html_output = open(join(output, app_basename + ".nocache.html"), "w")
    
    print >>home_nocache_html_output, home_nocache_html_template % dict(
        app_name = app_basename,
        safari_js = "%s.Safari" % app_basename,
        ie6_js = "%s.IE6" % app_basename,
        oldmoz_js = "%s.OldMoz" % app_basename,
        moz_js = "%s.Mozilla" % app_basename,
        opera_js = "%s.Opera" % app_basename,
    )
    
    home_nocache_html_output.close()

    ## all.cache.html

    all_cache_html_template = read_boilerplate("all.cache.html")

    parser = pyjs.PlatformParser("platform")
    app_headers = ''
    app_body = '\n'.join(['<script type="text/javascript" src="%s"></script>'%script for script in js_includes])

    for platform in app_platforms:
        all_cache_name = "%s.%s.cache.html" % (app_basename, platform)
        print "Creating: " + all_cache_name

        parser.setPlatform(platform)
        app_translator = pyjs.AppTranslator(app_library_dirs, parser)
        app_libs = app_translator.translateLibraries(['pyjslib'])
        app_code = app_translator.translate(app_name)
        all_cache_html_output = open(join(output, all_cache_name), "w")
        
        print >>all_cache_html_output, all_cache_html_template % dict(
            app_name = app_basename,
            app_libs = app_libs,
            app_code = app_code,
            app_body = app_body,
            app_headers = app_headers
        )
        
        all_cache_html_output.close()

    ## Done.
    
    print "Done. You can run your app by opening '%(html_output_filename)s' in a browser" % locals()

def main():
    global app_library_dirs
    global app_platforms
    parser = OptionParser(usage = usage, version = version)
    parser.add_option("-o", "--output", dest="output",
        help="directory to which the webapp should be written")
    parser.add_option("-j", "--include-js", dest="js_includes", action="append",
        help="javascripts to load into the same frame as the rest of the script")
    parser.add_option("-I", "--library_dir", dest="library_dirs", action="append",
        help="paths to search for python modules")
    parser.add_option("-P", "--platforms", dest="platforms",
        help="platforms to build for, comma-seperated")
    parser.set_defaults(output = "output", js_includes=[], library_dirs=[], platforms=(','.join(app_platforms)))
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    
    app_library_dirs += options.library_dirs
    if options.platforms:
       app_platforms = options.platforms.split(',')
    build(args[0], options.output, options.js_includes)


if __name__ == "__main__":
    main()

