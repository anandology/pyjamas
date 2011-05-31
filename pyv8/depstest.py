#!/usr/bin/env python
"""
Tool to generate dependency tree for given module and test each dependency
"""

import os
import sys
from tempfile import mkdtemp
from optparse import OptionParser
from os.path import join, dirname, basename, abspath, pathsep, sep
from pyv8run import (PyV8Linker, translator, PLATFORM, pyjs,
                     add_linker_options,
                     PyV8, Global)
from pyjs.translator import translate
from pyjs.linker import module_path
from collections import defaultdict
import json

class DepsJSON(json.JSONEncoder):
    def default(self, o):
        return o.export_json()

class Module(object):
    def __init__(self, name, file, deps, mods):
        self.name = name
        if file.startswith(pyjs.pyjspth):
            file = file[len(pyjs.pyjspth):]
            if file[0] == '/':
                file = file[1:]
        self.file = file
        self.deps = list(deps)
        self.rdeps = list()
        self.mods = mods
        self.distance = -1
        self.result = False
        self.error = ''
        self.source = ''
        
    def __repr__(self):
        return "<module '{0.name}' from '{0.file}'>".format(self)
        
    def paint(self, dist=0, parent=None):
        if parent and not parent.name in self.rdeps:
            self.rdeps.append(parent.name)
        if self.distance < 0 or self.distance > dist:
            self.distance = dist
            for dep in self.deps:
                if not dep in self.rdeps:
                    self.mods[dep].paint(self.distance + 1, self)
                    
    def export(self):
        return ("{0.name}\t{0.file}\t{0.distance}\t"
                "{0.deps}\t{0.rdeps}\t{0.result}\t{0.error!r}\n".format(self))
    
    def export_json(self):
        return dict(name=self.name,
                    file=self.file,
                    deps=self.deps,
                    rdeps=self.rdeps,
                    distance=self.distance,
                    source=self.source,
                    error=self.error,
                    result=self.result)
                    
    
    def set_result(self, r):
        err = ''
        if isinstance(r, Exception):
            err = str(r)
            r = r.__class__.__name__
        self.result = r
        self.error = err
        
    def set_source(self, stdlib_sources):
        if self.file.startswith('stdlib'):
            if self.name in stdlib_sources:
                self.source = stdlib_sources[self.name]
            elif self.name.split('.')[0] in stdlib_sources:
                self.source = stdlib_sources[self.name.split('.')[0]]
        elif self.file[0] != '/':
            self.source = 'pyjs'
        else:
            self.source = 'other'
    
    def __cmp__(self, a):
        return self.distance.__cmp__(a.distance)

def main():
    usage = """
    usage: %prog [ options ] [ module_name ]
    """
    parser = OptionParser(usage = usage)
    translator.add_compile_options(parser)
    add_linker_options(parser)
    options, args = parser.parse_args()
    if len(args) < 1:
        raise Exception("Should specify module, see --help")
    mod = args[0]
    if sep in mod:
        pyjs.path[0:0] = [dirname(abspath(mod))]
        mod = basename(mod)
    if '.' in mod:
        mod = mod.split('.')[0]
        
    translator_arguments = translator.get_compile_options(options)
    out = mkdtemp(prefix='pyjs_depstest')
    compiler=translator.import_compiler(options.internal_ast)
    pyjs.path[0:0] = [join(pyjs.pyjspth, 'stdlib')]
    pyjs.path.append(join(pyjs.pyjspth, 'pyjs', 'src'))
    linker = DepsExport([mod], output=out,
                        platforms=[PLATFORM],
                        path=pyjs.path,
                        compiler=compiler,
                        translator_arguments=translator_arguments)
    linker() 
    
    mod_src = dict(map(
        lambda x: x.strip().split(':'),
        open(join(pyjs.pyjspth, 'stdlib', 'modules_sources')).readlines())
                   )
    
    mods = {}
    mods[mod] = Module(mod, args[0], linker._file_deps[None], mods)
    for fn, mn in linker._file_to_module.iteritems():
        mods[mn] = Module(mn, fn, linker._file_deps[fn], mods)
        mods[mn].set_source(mod_src)
    if not 'pyjslib' in mods[mod].deps:
        mods[mod].deps.append('pyjslib')
    
    mods[mod].paint()
    nf2 = defaultdict(set)
    for nf, rdeps in linker._not_found.iteritems():
        if not nf.split('.')[0] in mods:
            nf2[nf.split('.')[0]].update(
                map(lambda x: linker._file_to_module[x], rdeps))
    
    for nf, rdeps in nf2.iteritems():
        print "Not found {} depended by {}".format(nf, list(rdeps))
    for m in mods:
        linker = DepsTestLinker([m], output=out,
                                platforms=[PLATFORM],
                                path=pyjs.path,
                                compiler=compiler,
                                translator_arguments=translator_arguments)
        mods[m].set_result(test_dependency(linker))
    
    outf = open('{}.deps'.format(mod), 'w')
    for m in sorted(mods.values()):
        outf.write(m.export())
    outf.close()
    print "Exported dependency tree to {}.deps".format(mod)
    
    outf = open('{}.deps.json'.format(mod), 'w')
    outf.write(DepsJSON().encode(mods.values()))
    outf.close()

def test_dependency(linker):
    res = True
    g = Global()
    ctxt = PyV8.JSContext(g)
    g.__context__ = ctxt    
    try:
        linker()
        fp = open(linker.out_file_mod, 'r')
        txt = fp.read()
        fp.close()
        ctxt.enter()
        x = ctxt.eval(txt)
    except Exception, e:
        res = e
    finally:
        if ctxt.entered:
            ctxt.leave()    
    return res

_deps_cache = {}

class DepsTestLinker(PyV8Linker):
    def __init__(self, *args, **kw):
        PyV8Linker.__init__(self, *args, **kw)
        self.translator_func = self._translator_func
    
    def _translator_func(self, platform, file_names, out_file, module_name,
                         translator_args, incremental):
        if out_file in _deps_cache:
            return _deps_cache[out_file]
        
        deps, js_libs = translate(self.compiler,
                                  file_names,
                                  out_file,
                                  module_name,
                                  **translator_args)
        _deps_cache[out_file] = (deps, js_libs)
        return deps, js_libs    

class DepsExport(PyV8Linker):
    def __init__(self, *args, **kw):
        PyV8Linker.__init__(self, *args, **kw)
        self.translator_func = self._translator_func
        self._file_to_module = {}
        self._file_deps = defaultdict(set)
        self._not_found = defaultdict(set)
    
    def _translator_func(self, platform, file_names, out_file, module_name,
                         translator_args, incremental):
        kw = dict(self.translator_arguments)
        kw['list_imports'] = True
        deps, js_libs = translate(self.compiler,
                                  file_names,
                                  out_file,
                                  module_name,
                                  **kw)
        return deps, js_libs
    
    def visit_modules(self, module_names, platform=None, parent_file = None):
        prefix = ''
        all_names = []
        for mn in module_names:
            if not mn.endswith(".js"):
                prefix = ''
                for part in mn.split('.')[:-1]:
                    pn = prefix + part
                    prefix = pn + '.'
                    if pn not in all_names:
                        all_names.append(pn)
            all_names.append(mn)
        paths = self.path
        parent_base = None
        abs_name = None
        if not parent_file is None:
            for p in paths:
                if parent_file.find(p) == 0 and p != parent_file:
                    parent_base = p
                    abs_name = os.path.split(parent_file)[0]
                    abs_name = '.'.join(abs_name[len(parent_base)+1:].split(os.sep))

        for mn in all_names:
            p = None
            if abs_name:
                p = module_path(abs_name + '.' + mn, [parent_base])
                if p:
                    mn = abs_name + '.' + mn
            if not p:
                p = module_path(mn, paths)
            if not p:
                self._not_found[mn].add(parent_file)
                continue
                raise RuntimeError, "Module %r not found. Dep of %r" % (
                    mn, self.dependencies)
            if mn==self.top_module:
                self.top_module_path = p
            override_paths=[]
            if platform:
                for pl in self.platform_parents.get(platform, []) + [platform]:
                    override_path = module_path('__%s__.%s' % (pl, mn),
                                                paths)
                    # prevent package overrides
                    if override_path and not override_path.endswith('__init__.py'):
                        override_paths.append(override_path)
            self._file_to_module[p] = mn
            self._file_deps[parent_file].add(mn)
            self.visit_module(p, override_paths, platform, module_name=mn)
    
if __name__ == '__main__':
    main()

