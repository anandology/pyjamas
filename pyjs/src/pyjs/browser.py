import os
from pyjs import linker
from pyjs import translator
from pyjs import util
from cStringIO import StringIO
from optparse import OptionParser
import pyjs

AVAILABLE_PLATFORMS = ('IE6', 'Opera', 'OldMoz', 'Safari', 'Mozilla')

BOILERPLATE_PATH = os.path.join(os.path.dirname(__file__), 'boilerplate')

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
<script language="javascript" src="bootstrap.js"></script>
</body>
</html>
"""

class BrowserLinker(linker.BaseLinker):

    # we derive from mozilla
    platform_parents = {
        'mozilla':['browser'],
        'ie6':['browser'],
        'safari':['browser'],
        'oldmoz':['browser'],
        'opera':['browser']
        }

    def visit_start(self):
        super(BrowserLinker, self).visit_start()
        self.boilerplate_path = None
        self.js_libs.append('_pyjs.js')
        self.js_libs.append('sprintf.js')
        self.merged_public = set()

    def visit_end_platform(self, platform):
        if not platform:
            return
        self._generate_app_file(platform)

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

    def find_boilerplate(self, name):
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
        out_path = os.path.join(
            self.output,
            '.'.join((self.top_module, platform, 'cache.html')))
        app_code = StringIO()
        done = self.done[platform]
        for p in done:
            f = file(p)
            app_code.write(f.read())
            f.close()
        scripts = ['<script type="text/javascript" src="%s"></script>'%script \
                   for script in self.js_libs]
        app_body = '\n'.join(scripts)
        deps = []
        file_contents = template % dict(
            app_name = self.top_module,
            early_app_libs = '',
            app_libs = app_code.getvalue(),
            app_body = app_body,
            platform = platform.lower(),
            available_modules = self.visited_modules[platform],
            dynamic = 0,
            app_headers = ''
        )
        out_file = file(out_path, 'w')
        out_file.write(file_contents)
        out_file.close()

    def _create_nocache_html(self):
        # nocache
        template = self.read_boilerplate('home.nocache.html')
        out_path = os.path.join(self.output, self.top_module + ".nocache.html")
        select_tmpl = """O(["true","%%s"],"%s.%%s.cache.html");\n""" % self.top_module
        script_selectors = StringIO()
        for platform in self.platforms:
            script_selectors.write(
                select_tmpl % (platform, platform))
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
                                         'title': title, 'css': css}

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
    parser.set_defaults(output="output",
                        js_includes=[],
                        library_dirs=[],
                        platforms=(','.join(AVAILABLE_PLATFORMS))
                        )
    options, args = parser.parse_args()
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
        source_tracking=options.source_tracking,
        line_tracking=options.line_tracking,
        store_source=options.store_source)

    l = BrowserLinker(top_module,
                      output=options.output,
                      platforms=app_platforms,
                      path=pyjs.path,
                      translator_arguments=translator_arguments)
    l()
    print "Built to :", os.path.abspath(options.output)
