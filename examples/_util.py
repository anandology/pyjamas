# -*- coding: utf-8 -*-


import sys
import os
import subprocess


ENV = None
PATH = None
TARGETS = None


def _find_python():
    if sys.version_info.major == 2 and sys.executable and os.path.isfile(sys.executable):
        return sys.executable
    for python in ('python2', 'python2.7', 'python2.6'):
        try:
            subprocess.call([python, '-c', '"raise SystemExit"'])
            return python
        except OSError:
            pass
    return 'python'


def _find_pyjsbuild(path):
    lim = 2
    while lim > 0:
        path = os.path.join(path, '..')
        boot = os.path.join(path, 'bootstrap.py')
        if os.path.isfile(boot):
            path = os.path.abspath(path)
            boot = os.path.abspath(boot)
            break
        lim = lim - 1
    if lim == 0:
        raise RuntimeError('Unable to locate pyjamas root.')
    pyjsbuild = os.path.join(path, 'bin', 'pyjsbuild')
    # Bootstrap on test failure; attempts to fix a couple issues at once
    null = open(os.devnull, 'wb')
    try:
        if subprocess.call(['python', pyjsbuild], stdout=null, stderr=subprocess.STDOUT) > 0:
            raise OSError
    except OSError:
        subprocess.call(['python', boot], stdout=null, stderr=subprocess.STDOUT)
    null.close()
    return pyjsbuild


def _process_environ():
    return dict([
        (k[5:], v[:])
        for k, v in os.environ.items()
        if k.startswith('PYJS')
    ])


def _process_opts(args):
    opts = {}
    possible = ('downloads',)
    for name in possible:
        for flag in ('yes', 'no'):
            opt = '--{0}-{1}'.format(name, flag)
            if opt in args:
                args.remove(opt)
                opts[opt] = flag
    return opts


def _process_args(args):
    return {'ARG_PYJSBUILD': args or ['-O']}


def setup(path, targets):
    for target in targets:
        if not os.path.isfile(os.path.join(path, target)):
            raise TypeError('Target `{0}` does not exist.'.format(target))
    global ENV, PATH, TARGETS
    args = sys.argv[1:]
    ENV = {}
    ENV.update(_process_environ())
    ENV.update(_process_opts(args))
    ENV.update(_process_args(args))
    ENV.setdefault('BIN_PYTHON', _find_python())
    ENV.setdefault('BIN_PYJSBUILD', _find_pyjsbuild(path))
    ENV['DIR_EXAMPLE'] = path
    PATH = path
    TARGETS = targets


def translate():
    for target in TARGETS:
        cmd = [ENV['BIN_PYTHON'], ENV['BIN_PYJSBUILD'], ' '.join(ENV['ARG_PYJSBUILD']), target]
        e = subprocess.Popen(cmd, cwd=PATH)
        ret = e.wait()
