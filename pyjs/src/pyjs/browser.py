import os
from pyjs import linker
from pyjs import translator
from pyjs import util
from cStringIO import StringIO
from optparse import OptionParser
import pyjs

AVAILABLE_PLATFORMS = ('IE6', 'Opera', 'OldMoz', 'Safari', 'Mozilla')

if pyjs.pyjspth is None:
    BOILERPLATE_PATH = os.path.join(os.path.dirname(__file__), 'boilerplate')
else:
    BOILERPLATE_PATH = os.path.join(pyjs.pyjspth, 'pyjs', 'src','pyjs', 'boilerplate')

APP_HTML_TEMPLATE = """\
<html>
<!-- auto-generated html - you should consider editing and
adapting this to suit your requirements
-->
<head>
<meta name="pygwt:module" content="%(modulename)s">
%(css)s
<title>%(title)s</title>
</head>
<body bgcolor="white">
<script language="javascript" src="%(bootstrap_file)s"></script>
<iframe id='__pygwt_historyFrame' style='width:0;height:0;border:0'></iframe>
</body>
</html>
"""

class BrowserLinker(linker.BaseLinker):

    # parents are specified in most-specific last
    platform_parents = {
        'mozilla':['browser', 'array_extras'],
        'ie6':['browser'],
        'safari':['browser', 'array_extras'],
        'oldmoz':['browser', 'array_extras'],
        'opera':['browser', 'array_extras'],
        }

    def __init__(self, *args, **kwargs):
        self.multi_file = kwargs.pop('multi_file', False)
        self.cache_buster = kwargs.pop('cache_buster', False)
        self.bootstrap_file = kwargs.pop('bootstrap_file', 'bootstrap.js')
        super(BrowserLinker, self).__init__(*args, **kwargs)

    def visit_start(self):
        super(BrowserLinker, self).visit_start()
        self.boilerplate_path = None
        self.early_static_app_libs.append('_pyjs.js')
        #self.js_libs.append('_pyjs.js')
        self.merged_public = set()
        self.app_files = {}
        self.renamed_libs = {}

    def visit_end_platform(self, platform):
        if not platform:
            return
        if self.cache_buster:
            import hashlib
            # rename the files to their hashed equivalents
            renamed = []
            for p in self.done[platform]:
                if p in self.renamed_libs:
                    new_p = self.renamed_libs[p]
                else:
                    f = open(p)
                    md5 = hashlib.md5(f.read()).hexdigest()
                    f.close()
                    name, ext = os.path.splitext(p)
                    new_p = name + '.' + md5 + ext
                    os.rename(p, new_p)
                    self.renamed_libs[p] = new_p
                renamed.append(new_p)
            self.done[platform] = renamed
        self.app_files[platform] = self._generate_app_file(platform)

    def visit_end(self):
        html_output_filename = os.path.join(self.output, self.top_module + '.html')
        if not os.path.exists(html_output_filename):
            # autogenerate
            self._create_app_html(html_output_filename)
        self._create_nocache_html()

    def merge_resources(self, dir_name):
        if not dir_name in self.merged_public:
            public_folder = os.path.join(dir_name, 'public')
            if os.path.exists(public_folder) and os.path.isdir(public_folder):
                util.copytree_exists(public_folder,
                                     self.output)
                self.merged_public.add(dir_name)
        for libs in [self.js_libs, self.dynamic_js_libs,
                     self.static_js_libs, self.early_static_js_libs, self.late_static_js_libs]:
            for lib in libs:
                if not lib in self.merged_public:
                    for path in self.path:
                        if os.path.exists(lib) and os.path.isfile(lib):
                            util.copy_exists(lib, os.path.join(self.output, os.path.basename(lib)))
                            self.merged_public.add(lib)
                            break

    def find_boilerplate(self, name):
        if not self.top_module_path:
            raise RuntimeError('Top module not found %r' % self.top_module)
        if not self.boilerplate_path:
            self.boilerplate_path = [BOILERPLATE_PATH]
            module_bp_path = os.path.join(
                os.path.dirname(self.top_module_path), 'boilerplate')
            if os.path.isdir(module_bp_path):
                self.boilerplate_path.insert(0, module_bp_path)
        for p in self.boilerplate_path:
            bp =  os.path.join(p, name)
            if os.path.exists(bp):
                return bp
        raise RuntimeError("Boilerplate not found %r" % name)

    def read_boilerplate(self, name):
        f = file(self.find_boilerplate(name))
        res = f.read()
        f.close()
        return res

    def _generate_app_file(self, platform):
        # TODO: cache busting
        template = self.read_boilerplate('all.cache.html')
        name_parts = [self.top_module, platform, 'cache.html']
        done = self.done[platform]
        len_ouput_dir = len(self.output)+1

        app_name = self.top_module
        platform_name = platform.lower()
        dynamic = 0,
        app_headers = ''
        available_modules = self.visited_modules[platform]
        early_static_app_libs = [] + self.early_static_app_libs
        static_app_libs = []
        dynamic_app_libs = []
        dynamic_js_libs = [] + self.dynamic_js_libs
        static_js_libs = [] + self.static_js_libs
        early_static_js_libs = [] + self.early_static_js_libs
        late_static_js_libs = [] + self.late_static_js_libs
        dynamic_modules = []

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
            return "\n".join(code)

        def js_modname(path):
            return 'js@'+os.path.basename(path)+'.'+hashlib.md5(path).hexdigest()

        if self.multi_file:
            dynamic_js_libs += [m for m in list(self.js_libs) if not m in static_js_libs]
            dynamic_app_libs = [m for m in done if not m in early_static_app_libs]
        else:
            static_js_libs += [m for m in list(self.js_libs) if not m in dynamic_js_libs]
            static_app_libs = [m for m in done if not m in early_static_app_libs]

        import hashlib
        dynamic_modules = available_modules + [js_modname(lib) for lib in dynamic_js_libs]
        available_modules += early_static_app_libs + dynamic_modules
        if len(dynamic_modules) > 0:
            dynamic_modules = "['" + "','".join(dynamic_modules) + "']"
        else:
            dynamic_modules = "[]"
        appscript = """<script type="text/javascript" src="%(path)s"></script>"""
        jsscript = """<script type="text/javascript" src="%(path)s" onload="$pyjs.script_onload('%(modname)s')" onreadystatechange="$pyjs.script_onreadystate('%(modname)s')"></script>"""
        dynamic_app_libs = '\n'.join([appscript % {'path': lib[len_ouput_dir:]} for lib in dynamic_app_libs])
        dynamic_js_libs = '\n'.join([jsscript % {'path': lib, 'modname': js_modname(lib)} for lib in dynamic_js_libs])
        early_static_app_libs = static_code(early_static_app_libs)
        static_app_libs = static_code(static_app_libs)
        early_static_js_libs = static_code(early_static_js_libs, "javascript lib")
        static_js_libs = static_code(static_js_libs, "javascript lib")
        late_static_js_libs = static_code(late_static_js_libs, "javascript lib")

        file_contents = template % locals()
        if self.cache_buster:
            import hashlib
            md5 = hashlib.md5(file_contents).hexdigest()
            name_parts.insert(2, md5)
        out_path = os.path.join(self.output, '.'.join((name_parts)))

        out_file = file(out_path, 'w')
        out_file.write(file_contents)
        out_file.close()
        return out_path

    def _create_nocache_html(self):
        # nocache
        template = self.read_boilerplate('home.nocache.html')
        out_path = os.path.join(self.output, self.top_module + ".nocache.html")
        select_tmpl = """O(["true","%s"],"%s");\n"""
        script_selectors = StringIO()
        for platform in self.platforms:
            cache_html = os.path.basename(self.app_files[platform])
            sel = select_tmpl % (platform, cache_html)
            script_selectors.write(sel)
        out_file = file(out_path, 'w')
        out_file.write(template % dict(
            app_name = self.top_module,
            script_selectors = script_selectors.getvalue()
            ))
        out_file.close()

    def _create_app_html(self, file_name):
        """ Checks if a base HTML-file is available in the PyJamas
        output directory.
        If the HTML-file isn't available, it will be created.

        If a CSS-file with the same name is available
        in the output directory, a reference to this CSS-file
        is included.

        If no CSS-file is found, this function will look for a special
        CSS-file in the output directory, with the name
        "pyjamas_default.css", and if found it will be referenced
        in the generated HTML-file.
        """

        # if html file in output directory exists, leave it alone.
        if os.path.exists(file_name):
            return 0
        if os.path.exists(
            os.path.join(self.output, self.top_module + '.css' )):
            css = "<link rel='stylesheet' href='" + self.top_module + ".css'>"
        elif os.path.exists(
            os.path.join(self.output, 'pyjamas_default.css' )):
            css = "<link rel='stylesheet' href='pyjamas_default.css'>"
        else:
            css = ''

        title = 'PyJamas Auto-Generated HTML file ' + self.top_module

        base_html = APP_HTML_TEMPLATE % {'modulename': self.top_module,
                                         'title': title, 'css': css,
                                         'bootstrap_file': self.bootstrap_file,
                                        }

        fh = open (file_name, 'w')
        fh.write  (base_html)
        fh.close  ()
        return 1

def build_script():
    usage = """
    usage: %prog [options] <application module name

    This is the command line builder for the pyjamas project, which can
    be used to build Ajax applications from Python.
    For more information, see the website at http://pyjs.org/
    """
    global app_platforms
    parser = OptionParser(usage = usage)
    # TODO: compile options
    translator.add_compile_options(parser)
    linker.add_linker_options(parser)
    parser.add_option("-P", "--platforms", dest="platforms",
        help="platforms to build for, comma-separated")
    parser.add_option("-l", "--log-level", dest="log_level",
                      default=None,
                      type="int",
                      help="The python log level as an int")
    parser.add_option(
        "-m", "--multi-file", dest="multi_file",
        default=False,
        action="store_true",
        help="Include each module via a script-tag instead of writing"
              " the whole code into the main cache.html file")

    parser.add_option(
        "-c", "--cache-buster", action="store_true",
        dest="cache_buster",
        default=False,
        help="Enable browser cache-busting (MD5 hash added to output filenames)",
        )

    parser.add_option(
        "--bootstrap-file", 
        dest="bootstrap_file",
        help="Specify the bootstrap code. (Used when application html file is generated)."
        )

    parser.set_defaults(output="output",
                        js_includes=[],
                        js_static_includes=[],
                        library_dirs=[],
                        platforms=(','.join(AVAILABLE_PLATFORMS)),
                        bootstrap_file="bootstrap.js",
                        )
    options, _args = parser.parse_args()
    args = []
    for a in _args:
        if a.lower().endswith('.py'):
            args.append(a[:-3])
        else:
            args.append(a)

    if options.log_level is not None:
        import logging
        logging.basicConfig(level=options.log_level)
    if len(args) != 1:
        parser.error("incorrect number of arguments")

    top_module = args[0]
    for d in options.library_dirs:
        pyjs.path.append(os.path.abspath(d))

    if options.platforms:
       app_platforms = options.platforms.lower().split(',')
    print "Building:", top_module
    print "PYJSPATH:", pyjs.path

    translator_arguments=dict(
        debug=options.debug,
        print_statements = options.print_statements,
        function_argument_checking=options.function_argument_checking,
        attribute_checking=options.attribute_checking,
        bound_methods=options.bound_methods,
        source_tracking=options.source_tracking,
        line_tracking=options.line_tracking,
        store_source=options.store_source)

    l = BrowserLinker(top_module,
                      output=options.output,
                      platforms=app_platforms,
                      path=pyjs.path,
                      js_libs=options.js_includes,
                      translator_arguments=translator_arguments,
                      multi_file=options.multi_file,
                      cache_buster=options.cache_buster,
                      bootstrap_file=options.bootstrap_file,
                     )
    l()
    print "Built to :", os.path.abspath(options.output)
