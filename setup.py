# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

#from ez_setup import use_setuptools

#use_setuptools()

import glob
from setuptools import setup, find_packages
from setuptools.command import test
from setuptools.command.install import install

import sys
import os

install_requires = []

keyw = """\
"""

# yuk, spew, hurl.  but it works.  anyone got any better ideas?
if sys.platform == "win32":
    datadir = "share/pyjamas"
else:
    # last thing we want on unix systems is the data files ending
    # up in a random egg subdirectory, where no-one can find them.
    # windows platform, i couldn't care less where they end up but
    # it musn't be a fixed path, it must be a relative path.
    datadir = "/usr/share/pyjamas"

lib_data_files = glob.glob("library/*.py")
lib_ui_data_files = glob.glob("library/ui/*.py")
bp_data_files = glob.glob("builder/boilerplate/*")
test_files = glob.glob("pyjs/tests/*")
stub_files = glob.glob("stubs/*")
lib_data_files += glob.glob("library/*.js")
builtin_data_files = glob.glob("library/builtins/*.py")
platform_data_files = glob.glob("library/platform/*.py")
pyjamas_data_files = glob.glob("library/pyjamas/*.py")
addons_data_files = glob.glob("addons/*.py")

data_files = [(os.path.join(datadir, "library"), lib_data_files),
              (os.path.join(datadir, "library/builtins"), builtin_data_files),
              (os.path.join(datadir, "library/ui"), lib_ui_data_files),
              (os.path.join(datadir, "builder/boilerplate"), bp_data_files),
              (os.path.join(datadir, "pyjs/tests"), test_files),
              (os.path.join(datadir, "stubs"), stub_files),
              (os.path.join(datadir, "library/platform"), platform_data_files),
              (os.path.join(datadir, "library/pyjamas"), pyjamas_data_files),
              (os.path.join(datadir, "addons"), addons_data_files)
              ]

# main purpose of this function is to exclude "output" which
# could have been built by a developer.
def get_files(d):
    res = []
    for p in glob.glob(os.path.join(d, "*")):
        if not p:
            continue
        (pth, fname) = os.path.split(p)
        if fname == "output":
            continue
        if fname[-4:] == ".pyc": # ehmm.. noooo.
            continue 
        if os.path.isdir(p):
            res += get_files(p)
        else:
            res.append(p)
    return res

# ok - examples is a bit of a pain.  
for d in glob.glob("examples/*"):
    if os.path.isdir(d):
        (pth, fname) = os.path.split(d)
        expath = get_files(d)
        pth = os.path.join(os.path.join(datadir, "examples"), fname)
        #print pth, expath
        data_files.append((pth, expath))
    else:
        data_files.append((os.path.join(datadir, "examples"), [d]))

if __name__ == '__main__':
    setup(name = "Pyjamas",
        version = "0.5",
        description = "Pyjamas Widget API for Web applications, in Python",
        long_description = open('README', 'rt').read(),
        url = "http://pyjs.org",
        author = "The Pyjamas Project",
        author_email = "lkcl@lkcl.net",
        keywords = keyw,
        entry_points = {'console_scripts':[
                       'pyjsbuild=pyjs.build:main',
                       'pyjscompile=pyjs:main',
                       ]},
        packages=["pyjs"],
        install_requires = install_requires,
        data_files = data_files,
        zip_safe=False,
        license = "Apache Software License",
        platforms = ["any"],
        classifiers = [
            "Development Status :: 5 - Production/Stable",
            "Natural Language :: English",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python"
        ])

