#!/usr/bin/env python
# Copyright (C) 2010 Sujan Shakya, suzan.shakya@gmail.com

# compile the pyjs application with 3 options. This will reduce the
# output size to 85%.

# pyjsbuild Hello.py --no-print-statements --no-bound-methods \
#                    --no-operator-funcs

# Make sure to export COMPILER=/path/to/google/compiler
# Then run this script. This will reduce the output size to 50%.

# pyjscompressor.py output

import re, os, sys, commands

MERGE_SCRIPTS = re.compile('</script>\s*(?:<!--.*?-->\s*)*<script(?:(?!\ssrc).)*?>', re.DOTALL)
SCRIPT = re.compile('<script(?:(?!\ssrc).)*?>(.*?)</script>', re.DOTALL)

def compile(js_file, js_output_file, html_file=''):
    # SIMPLE_OPTIMIZATIONS has some problem with Opera, so we'll use
    # WHITESPACE_ONLY for opera
    if 'opera' in html_file:
        level = 'WHITESPACE_ONLY'
    else:
        level = 'SIMPLE_OPTIMIZATIONS'
    stderr = '2> /dev/null' if os.name == 'posix' else ''
    error = os.system('java -jar $COMPILER --compilation_level %s '
        ' --js %s --js_output_file %s %s' % \
                (level, js_file, js_output_file, stderr))
    if error:
        raise Exception, 'Error occurred while compiling %s' % js_file

def compress_css(css_file):
    sys.stdout.write('Compressing %-40s' % css_file)
    sys.stdout.flush()
    css_output_file = 'temp/%s.ccss' % os.path.basename(css_file)
    f = open(css_file)
    css = f.read()
    
    css = re.sub(r"\s+([!{};:>+\(\)\],])", r"\1", css)
    css = re.sub(r"([!{}:;>+\(\[,])\s+", r"\1", css)
    css = re.sub(r"\s+", " ", css)
        
    f = open(css_output_file, 'w')
    f.write(css)
    f.close()
    print '%4.1f%%' % getcompression(getsize(css_file),getsize(css_output_file))
    os.rename(css_output_file, css_file)
    os.system('rm -f temp/*')

def compress_js(js_file):
    sys.stdout.write('Compressing %-40s' % js_file)
    sys.stdout.flush()
    js_output_file = 'temp/%s.cjs' % os.path.basename(js_file)
    
    compile(js_file, js_output_file)
    
    print '%4.1f%%' % getcompression(getsize(js_file), getsize(js_output_file))
    os.rename(js_output_file, js_file)
    os.system('rm -f temp/*')

def compress_html(html_file):
    sys.stdout.write('Compressing %-40s' % html_file)
    sys.stdout.flush()
    js_file = 'temp/pyjs%d.js'
    js_output_file = 'temp/pyjs%d.cjs'
    html_output_file = 'temp/compiled.html'
    
    f = open(html_file)
    html = f.read()
    f.close()
    
    # remove comments betn <script> and merge all <script>
    html = MERGE_SCRIPTS.sub('', html)
    
    # now extract the merged scripts
    template = '<!--compiled-js-%d-->'
    scripts = []
    def script_repl(matchobj):
        scripts.append(matchobj.group(1))
        return '<script type="text/javascript">%s</script>' % template % \
                             (len(scripts)-1)
    html = SCRIPT.sub(script_repl, html)
    
    # save js files in temp dir and compile them with simple optimizations
    for i, script in enumerate(scripts):
        f = open(js_file % i, 'w')
        f.write(script)
        f.close()
        compile(js_file % i, js_output_file % i, html_file)
    
    # now write all compiled js back to html file
    for i in xrange(len(scripts)):
        f = open(js_output_file % i)
        script = f.read()
        f.close()
        html = html.replace(template % i, script)
    
    f = open(html_output_file, 'w')
    f.write(html)
    f.close()

    print '%4.1f%%'%getcompression(getsize(html_file),getsize(html_output_file))
    os.rename(html_output_file, html_file)
    os.system('rm -f temp/*')

def compress(path):
    ext = os.path.splitext(path)[1]
    if ext == '.css':
        compress_css(path)
    elif ext == '.js':
        compress_js(path)
    elif ext == '.html':
        compress_html(path)

def getsize(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        output = commands.getoutput('du -s %s' % dir)
        return int(output.split()[0]) * 1024

def getcompression(p_size, n_size):
    return n_size / float(p_size) * 100

def compress_all(path):
    if not os.environ.has_key('COMPILER'):
        sys.exit('environment variable COMPILER is not defined.\n'
                 'In bash, export '
                 'COMPILER=/home/me/google/compiler/compiler.jar')
    
    if not os.path.exists('temp'):
        os.makedirs('temp')
    
    print '%17s %45s' % ('Files', 'Compression')
    p_size = getsize(path)
    
    if os.path.isfile(path):
        compress(path)
    else:
        for root, dirs, files in os.walk(path):
            if 'temp' in root:
                continue
            for file in files:
                compress(os.path.join(root, file))
        n_size = getsize(path)
    
    n_size = getsize(path)
    compression = getcompression(p_size, n_size)
    
    os.system('rm -rf temp')
    sizes = "Initial size: %.1fKB  Final size: %.1fKB" % \
            (p_size/1024., n_size/1024.)
    print '%s %s' % (sizes.ljust(51), "%4.1f%%" % compression)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage python pyjs_compressor.py pyjamas_output_dir')
    else:
        dir = sys.argv[1]
        compress_all(dir)

