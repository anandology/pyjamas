import translator
import os
import sys
import util
import logging
import pyjs


if pyjs.pyjspth is None:
    LIB_PATH = os.path.join(os.path.dirname(__file__), 'lib')
    BUILTIN_PATH = os.path.join(os.path.dirname(__file__), 'builtin')
else:
    LIB_PATH = os.path.join(pyjs.pyjspth, "pyjs", "src", "pyjs", "lib")
    BUILTIN_PATH = os.path.join(pyjs.pyjspth, "pyjs", "src", "pyjs", "builtin")

_path_cache= {}
def module_path(name, path):
    global _path_cache
    k = (name, tuple(sorted(path)))
    if k in _path_cache:
        return _path_cache[k]
    candidates = []
    tail = []
    packages = {}
    modules = {}
    if name.endswith('.js'):
        parts = [name]
    else:
        parts = name.split('.')
    for pn in parts:
        tail.append(pn)
        for p in path:
            cp = os.path.join(*([p] + tail))
            if os.path.isdir(cp) and os.path.exists(
                os.path.join(cp, '__init__.py')):
                packages['.'.join(tail)] = os.path.join(cp, '__init__.py')
            elif os.path.exists(cp + '.py'):
                modules['.'.join(tail)] = cp + '.py'
            elif pn.endswith('.js') and os.path.exists(cp):
                modules['.'.join(tail)] = cp
    res = None
    if modules:
        assert len(modules)==1
        res = modules.get(name)
        if not res and '.'.join(name.split('.')[:-1]) not in modules:
            raise RuntimeError, "Module %r not found" % name

    elif packages:
        res = packages[sorted(packages)[-1]]
        if not packages.has_key(name):
            return None
    _path_cache[k] = res
    return res

class BaseLinker(object):

    platform_parents = {}

    def __init__(self, top_module, output='output',
                 debug=False, 
                 js_libs=[], static_js_libs=[], early_static_js_libs=[], late_static_js_libs=[], dynamic_js_libs=[],
                 early_static_app_libs = [],
                 platforms=[], path=[],
                 translator_arguments={},
                 compile_inplace=False):
        self.js_path = os.path.abspath(output)
        self.path = path + [LIB_PATH]
        self.platforms = platforms
        self.top_module = top_module
        self.output = os.path.abspath(output)
        self.js_libs = list(js_libs)
        self.static_js_libs = list(static_js_libs)
        self.early_static_js_libs = list(early_static_js_libs)
        self.late_static_js_libs = list(late_static_js_libs)
        self.dynamic_js_libs = list(dynamic_js_libs)
        self.early_static_app_libs = list(early_static_app_libs)
        self.translator_arguments = translator_arguments
        self.compile_inplace = compile_inplace
        self.top_module_path = None

    def __call__(self):
        self.visited_modules = {}
        self.done = {}
        self.dependencies = {}
        self.visit_start()
        for platform in [None] + self.platforms:
            self.visit_start_platform(platform)
            old_path = self.path
            self.path = [BUILTIN_PATH, LIB_PATH]
            self.visit_modules(['pyjslib'], platform)
            self.path = old_path
            self.visit_modules([self.top_module], platform)
            self.visit_end_platform(platform)
        self.visit_end()

    def visit_modules(self, module_names, platform=None):
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

        for mn in all_names:
            p = module_path(mn, self.path)
            if not p:
                continue
                raise RuntimeError, "Module %r found. Dep of %r" % (
                    mn, self.dependencies)
            if mn==self.top_module:
                self.top_module_path = p
            override_paths=[]
            if platform:
                for pl in self.platform_parents.get(platform, []) + [platform]:
                    override_path = module_path('__%s__.%s' % (pl, mn),
                                                self.path)
                    # prevent package overrides
                    if override_path and not override_path.endswith('__init__.py'):
                        override_paths.append(override_path)
            self.visit_module(p, override_paths, platform, module_name=mn)

    def visit_module(self, file_path, overrides, platform,
                     module_name):
        dir_name, file_name = os.path.split(file_path)
        if (     not file_name.endswith('.js')
             and file_name.split('.')[0] != module_name.split('.')[-1]
           ):
            if file_name == "__init__.py":
                if os.path.basename(dir_name) != module_name.split('.')[-1]:
                    return
            else:
                return
        self.merge_resources(dir_name)
        if platform and overrides:
            plat_suffix = '.__%s__' % platform
        else:
            plat_suffix = ''
        if self.compile_inplace:
            mod_part, extension = os.path.splitext(file_path)
            out_file = '%s%s.js' % (mod_part, plat_suffix)
        else:
            out_file = os.path.join(self.output, 'lib',
                                    '%s%s.js' % (module_name, plat_suffix))
        if out_file in self.done.get(platform, []):
            return
        
        # translate if
        #  -    no platform
        #  - or if we have an override
        #  - or the module is used in an override only
        if (   platform is None
            or (platform and overrides)
            or (out_file not in self.done.get(None,[]))
           ):
            if file_name.endswith('.js'):
                fp = open(out_file, 'w')
                fp.write("/* start javascript include: %s */\n" % file_name)
                fp.write(open(file_path, 'r').read())
                fp.write("$pyjs.loaded_modules['%s'] = function ( ) {return null;};\n" % file_name)
                fp.write("/* end %s */\n" % file_name)
                deps = []
                self.dependencies[out_file] = deps
            else:
                logging.info('Translating module:%s platform:%s out:%r' % (
                    module_name, platform or '-', out_file))
                deps, js_libs = translator.translate([file_path] +  overrides,
                                            out_file,
                                            module_name=module_name,
                                            **self.translator_arguments)
                self.dependencies[out_file] = deps
                for path, mode, location in js_libs:
                    if mode == 'default':
                        if self.multi_file:
                            mode = 'dynamic'
                        else:
                            mode = 'static'
                    if mode == 'dynamic':
                        self.dynamic_js_libs.append(path)
                    elif mode == 'static':
                        if location == 'early':
                            self.early_static_js_libs.append(path)
                        elif location == 'middle':
                            self.static_js_libs.append(path)
                        elif location == 'late':
                            self.late_static_js_libs.append(path)
                        else:
                            raise RuntimeError, "Unknown js lib location: %r" % location
                    else:
                        raise RuntimeError, "Unknown js lib mode: %r" % mode

                if '.' in module_name:
                    for i, dep in enumerate(deps):
                        if module_path(dep, path=[dir_name]):
                            deps[i] = '.'.join(module_name.split('.')[:-1] + [dep])
        else:
            deps = self.dependencies[out_file]
        if out_file not in self.done.setdefault(platform, []):
            self.done[platform].append(out_file)
        if module_name not in self.visited_modules.setdefault(platform, []):
            self.visited_modules[platform].append(module_name)
        if deps:
            self.visit_modules(deps, platform)

    def merge_resources(self, dir_name):
        """gets a directory path for each module visited, this can be
        used to collect resources e.g. public folders"""
        pass

    def visit_start(self):
        if not os.path.exists(self.output):
            os.mkdir(self.output)
        if not self.compile_inplace:
            lib_dir = os.path.join(self.output, 'lib')
            if not os.path.exists(lib_dir):
                os.mkdir(lib_dir)

    def visit_start_platform(self, platform):
        pass

    def visit_end_platform(self, platform):
        pass

    def visit_end(self):
        pass


def add_linker_options(parser):
    parser.add_option("-o", "--output", dest="output", default='output',
                      help="directory to which the app should be written")

    parser.add_option("-j", "--include-js", dest="js_includes",
                      action="append", default=[],
                      help="javascripts to load into the same frame as the rest of the script")
    parser.add_option("-I", "--library_dir", dest="library_dirs",
                      default=[],
                      action="append", help="additional paths appended to PYJSPATH")



