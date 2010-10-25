# -*- coding: utf-8 -*-


import sys
import os
import subprocess


ENV = None
PATH = None
TARGETS = None


PACKAGE = {
    'title': 'example',
    'desc': 'default description',
}

INDEX = {
    'example': r'''
        <hr/>
<!-- start {name} {{example.{name}._comment_end}}
        <h2 class='title'>{{example.{name}.title}}</h2>
        <h3 class='desc'>{{example.{name}.desc}}</h3>
        <ul class='demos'>
            {{example.{name}.demos}}
        </ul>
{{example.{name}._comment_start}} -->
        <h4 class='source'><a href="{name}/">source directory</a> ({name})<h4>
    ''',
    'demo': r'''
        <li class='demo'>(demo) <a href="{name}/output/{target}.html">{target}</a></li>
    ''',
}


class _e(object):

    _ident = 'example'

    _special = {
        '_comment_start': '<!--',
        '_comment_end': '-->',
    }

    def __init__(self, examples=None, **kwds):
        if examples is None:
            self._examples = kwds
        else:
            self._examples = examples
            self._examples.update(kwds)
        self._path = [self._ident]

    def __str__(self):
        try:
            curr = self._examples
            for frag in self._path[1:]:
                curr = curr[frag]
        except KeyError:
            if frag in self._special:
                curr = self._special[frag]
            else:
                curr = '{{{0}}}'.format('.'.join(self._path))
        self._path[1:] = []
        return curr

    def __getattr__(self, name):
        self._path.append(name)
        return self


def _find_python():
    if sys.version_info[0] == 2 and sys.executable and os.path.isfile(sys.executable):
        return sys.executable
    for python in ('python2', 'python2.7', 'python2.6'):
        try:
            subprocess.call([python, '-c', '"raise SystemExit"'])
            return python
        except OSError:
            pass
    return 'python'


def _list_examples():
    return [ 
        example
        for example in os.listdir(ENV['DIR_EXAMPLES'])
        if os.path.isfile(os.path.join(ENV['DIR_EXAMPLES'], example, '__main__.py'))
            and not example.startswith('_')
    ]


def _process_pyjamas(root):
    lim = 2
    while lim > 0:
        root = os.path.join(root, '..')
        boot = os.path.join(root, 'bootstrap.py')
        if os.path.isfile(boot):
            root = os.path.abspath(root)
            boot = os.path.abspath(boot)
            pyjsbuild = os.path.join(root, 'bin', 'pyjsbuild')
            break
        lim = lim - 1
    if lim == 0:
        raise RuntimeError('Unable to locate pyjamas root.')
    # Bootstrap on test failure; attempts to fix a couple issues at once
    with open(os.devnull, 'wb') as null:
        try:
            if subprocess.call(['python', pyjsbuild], stdout=null, stderr=subprocess.STDOUT) > 0:
                raise OSError
        except OSError:
            subprocess.call(['python', boot], stdout=null, stderr=subprocess.STDOUT)
        return {
            'DIR_PYJAMAS': root,
            'DIR_EXAMPLES': os.path.join(root, 'examples'),
            'BIN_PYJSBUILD': pyjsbuild,
        }


def _process_environ():
    return dict([
        (k[5:], v[:])
        for k, v in os.environ.items()
        if k.startswith('PYJS')
    ])

#FIXME
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


def init(path):
    global ENV, PATH
    args = sys.argv[1:]
    PATH = path
    ENV = {}
    ENV.update(_process_environ())
    ENV.update(_process_opts(args))
    ENV.update(_process_args(args))
    if 'BIN_PYTHON' not in ENV:
        ENV['BIN_PYTHON'] = _find_python()
    if 'DIR_PYJAMAS' not in ENV:
        ENV.update(_process_pyjamas(path))
    if 'DIR_EXAMPLES' not in ENV:
        ENV['DIR_EXAMPLES'] = os.path.dirname(path)
    ENV['NAME_EXAMPLE'] = os.path.basename(path)
    ENV['DIR_EXAMPLE'] = path


def setup(targets):
    for target in targets:
        if not os.path.isfile(os.path.join(PATH, target)):
            raise TypeError('Target `{0}` does not exist.'.format(target))
    global TARGETS
    TARGETS = targets


def translate():
    for target in TARGETS:
        cmd = [ENV['BIN_PYTHON'], ENV['BIN_PYJSBUILD'], ' '.join(ENV['ARG_PYJSBUILD']), target]
        e = subprocess.Popen(cmd, cwd=PATH)
        ret = e.wait()


def install(package=None, **packages):
    if package is not None:
        PACKAGE.update(package)
        name = ENV['NAME_EXAMPLE']
        demos = ''.join([
            INDEX['demo'].format(name=name, target=target[:-3])
            for target in TARGETS
        ])  
        example = { 
            'name': name,
            'title': PACKAGE['title'],
            'desc': PACKAGE['desc'],
            'demos': demos,
        }
        if 'OPT_PROXYINSTALL' in ENV:
            sys.stdout.write(repr(example))
            sys.stdout.flush()
            return
        packages[name] = example
    if not packages:
        raise TypeError('Nothing to install.')
    index = os.path.join(ENV['DIR_EXAMPLES'], 'index.html')
    try:
        if os.path.isfile(index):
            idx_out_fd = open(index, 'r+')
            index_orig = tpl = idx_out_fd.read()
            idx_out_fd.seek(0)
            idx_out_fd.truncate()
        else:
            idx_out_fd = open(index, 'w')
            index_orig = tpl = None
        if tpl is None or '<style>' in tpl:
            examples = ''.join([
                INDEX['example'].format(name=example)
                for example in _list_examples()
            ])
            index_tpl = os.path.join(ENV['DIR_EXAMPLES'], '_examples', 'template', 'index.html.tpl')
            with open(index_tpl, 'r') as idx_in_fd:
                tpl = idx_in_fd.read().format(examples)
        index_new = tpl.format(example=_e(packages))
    except:
        if index_orig is None:
            idx_out_fd.close()
            os.unlink(index)
        else:
            idx_out_fd.write(index_orig)
        raise
    else:
        idx_out_fd.write(index_new)
    finally:
        idx_out_fd.close()
