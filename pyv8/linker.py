import os

from pyjs import linker
from pyjs import util

PLATFORM='pyv8'

APP_TEMPLATE = """
var $wnd = new Object();
$wnd.document = new Object();
var $doc = $wnd.document;
var $moduleName = "%(app_name)s";
var $pyjs = new Object();
var $p = null;
$pyjs.__modules__ = {};
$pyjs.modules = {};
$pyjs.modules_hash = {};
$pyjs.available_modules = %(available_modules)s;
$pyjs.loaded_modules = {};
$pyjs.options = new Object();
$pyjs.options.set_all = function (v) {
    $pyjs.options.arg_ignore = v;
    $pyjs.options.arg_count = v;
    $pyjs.options.arg_is_instance = v;
    $pyjs.options.arg_instance_type = v;
    $pyjs.options.arg_kwarg_dup = v;
    $pyjs.options.arg_kwarg_unexpected_keyword = v;
    $pyjs.options.arg_kwarg_multiple_values = v;
};
$pyjs.options.set_all(true);
$pyjs.trackstack = [];
$pyjs.track = {module:'__main__', lineno: 1};
$pyjs.trackstack.push($pyjs.track);
$pyjs.__last_exception_stack__ = null;
$pyjs.__last_exception__ = null;

/*
 * prepare app system vars
 */
$pyjs.platform = 'pyv8';
$pyjs.appname = '%(app_name)s';
$pyjs.loadpath = './';

pyv8_load(%(module_files)s);

pyv8_load(%(js_lib_files)s);

/* late static js libs */

%(late_static_js_libs)s


//try {
    $p = $pyjs.loaded_modules['pyjslib'];
    $p('pyjslib');
    $pyjs.__modules__.pyjslib = $p['pyjslib']
    $pyjs.loaded_modules['pyjslib'].___import___('%(app_name)s', '%(app_name)s', '__main__');
//} catch(exception)
//{
//    var fullMessage = exception.name + ': ' + exception.message;
//    var uri = exception.fileName;
//    //var stack = exception.stack;
//    var line = exception.lineNumber;
//    fullMessage += "\\n at " + uri + ": " + line;
//    print (fullMessage );
//    //print (stack.toString() );
//}
"""

def tostrlist(l):
    l = map(lambda x: "'%s'" % x, l)
    return "[%s]" % ', '.join(l)

class PyV8Linker(linker.BaseLinker):
    """PyV8 linker, which links together files by using the
    load function of the spidermonkey shell."""

    # we derive from mozilla
    platform_parents = {
        PLATFORM:['mozilla', 'array_extras']
        }

    def __init__(self, *args, **kwargs):
        kwargs['platforms'] = [PLATFORM]
        super(PyV8Linker, self).__init__(*args, **kwargs)

    def visit_start(self):
        super(PyV8Linker, self).visit_start()
        self.js_libs.append('_pyjs.js')
        self.merged_public = set()

    def merge_resources(self, dir_name):
        """find the absolute paths of js includes"""
        if not self.js_libs or dir_name in self.merged_public:
            return
        public_folder = os.path.join(dir_name, 'public')
        if not os.path.isdir(public_folder):
            return
        for i, js_lib in enumerate(self.js_libs):
            p = os.path.join(public_folder, js_lib)
            if os.path.isfile(p):
                self.js_libs[i] = p

    def visit_end(self):

        def static_code(libs, msg = None):
            code = []
            for lib in libs:
                fname = lib
                if not os.path.isfile(fname):
                    fname = os.path.join(self.output, lib)
                if not os.path.isfile(fname):
                    raise RuntimeError('File not found %r' % lib)
                if fname[len_ouput_dir:] == self.output:
                    name = fname[len_ouput_dir:]
                else:
                    name = os.path.basename(lib)
                if not msg is None:
                    code.append("/* start %s: %s */" % (msg, name))
                f = file(fname)
                code.append(f.read())
                if not msg is None:
                    code.append("/* end %s */" % (name,))
                self.remove_files[fname] = True
                fname = fname.split('.')
                if fname[-2] == '__%s__' % platform_name:
                    del fname[-2]
                    fname = '.'.join(fname)
                    if os.path.isfile(fname):
                        self.remove_files[fname] = True
            return "\n".join(code)

        done = self.done[PLATFORM]

        # locals - go into template via locals()
        module_files=tostrlist(done)
        #print "module_files", module_files
        js_lib_files=tostrlist(self.js_libs)
        early_static_js_libs=str(self.js_libs)[1:-1]
        late_static_js_libs = [] + self.late_static_js_libs
        late_static_js_libs = static_code(late_static_js_libs, "javascript lib")

        app_name = self.top_module
        available_modules = self.visited_modules[PLATFORM]

        self.out_file_mod = os.path.join(self.output, self.top_module + '.js')
        out_file = open(self.out_file_mod , 'w')
        out_file.write(APP_TEMPLATE % locals())
        out_file.close()
        
add_linker_options = linker.add_linker_options