#!/usr/bin/env python
# Copyright (C) 2011, Kees Bos <cornelis.bos@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create imports for gwt to import from pyjamas in stead of gwt"""

import sys
import os
import compiler
from compiler import ast


class CreateImports(object):
    verbosity = 1

    def __init__(self, srcFile, dstFile, base_directory='.'):
        self.import_names = []
        self.import_lines = []
        self.srcFile = srcFile
        self.dstFile = dstFile
        parent, module = os.path.split(srcFile)
        self.srcModule = parent.split(os.sep)
        base_depth = len(base_directory.split(os.sep))
        self.srcModule = self.srcModule[base_depth:]
        if module.lower().endswith(".py"):
            module = module[:-3]
        if module != '__init__':
            self.srcModule.append(module)

    def log(self, logname, msg, lineno):
        if lineno is None:
            lineno = ''
        else:
            lineno = "(%s) " % lineno
        if self.srcFile:
            if lineno:
                file = self.srcFile
            else:
                file = '%s ' % self.srcFile
        else:
            file = ''
        sys.stderr.write("%(file)s%(lineno)s%(logname)s: %(msg)s\n" % locals())

    def error(self, msg, lineno=None):
        self.log('ERROR', msg, lineno)

    def warning(self, msg, lineno=None):
        self.log('WARNING', msg, lineno)

    def getImportNames(self, srcFile=None, import_names=None):
        savedSrcFile = self.srcFile
        if srcFile is None:
            srcFile = self.srcFile
        else:
            self.srcFile = srcFile
        if import_names is None:
            import_names = self.import_names
        skip = False
        try:
            nodes = compiler.parseFile(srcFile).getChildNodes()[0]
        except SyntaxError, e:
            self.warning("Skipping. Syntax error: %s" % e)
            skip = True
        except:
            exc = sys.exc_info()
            self.error("Parse error %s" % (exc, ))
            raise
        if not skip:
            dict_import_names = dict([(k, True) for k in import_names])
            for node in nodes:
                ast_name = node.__class__.__name__
                method = getattr(self, "ast%s" % ast_name, None)
                if method is not None:
                    method(dict_import_names, node)
                elif self.verbosity:
                    self.warning('Skipping %s' % ast_name, node.lineno)
            import_names[:] = dict_import_names.keys()
            import_names.sort()
            self.srcFile = savedSrcFile
        return import_names

    def addNames(self, import_names, node_names):
        for names in node_names:
            if isinstance(names, basestring):
                name = names
            elif names[1] is None:
                name = names[0]
            else:
                name = names[1]
            import_names[name] = True

    def astImport(self, import_names, node):
        self.addNames(import_names, node.names)

    def astFrom(self, import_names, node):
        if not node.modname in [
            '__pyjamas__',
            '__javascript__',
        ]:
            self.addNames(import_names, node.names)

    def astAssign(self, import_names, node):
        for node in node.nodes:
            if node.flags == 'OP_ASSIGN':
                import_names[node.name] = True
            else:
                self.warning("Ignoring Assign %s" % node.flags, node.lineno)

    def astAssName(self, import_names, node):
        if node.flags == 'OP_DELETE':
            if node.name in import_names:
                del(import_names[node.name])
        else:
            self.warning("Ignoring AssName %s" % node.flags, node.lineno)

    def astClass(self, import_names, node):
        import_names[node.name] = True

    def astFunction(self, import_names, node):
        import_names[node.name] = True

    def astGlobal(self, import_names, node):
        self.addNames(import_names, node.names)

    # Now all the completely ignored asts
    def astTryExcept(self, import_names, node):
        pass

    def astIf(self, import_names, node):
        pass

    def astPrintnl(self, import_names, node):
        pass

    def astDiscard(self, import_names, node):
        pass

    def createImportLines(self, base=None, import_names=None):
        if base is None:
            base = '.'.join(self.srcModule)
        if import_names is None:
            import_names = self.import_names
        lines = []
        lines.append('from %s import (' % base)
        for name in import_names:
            lines.append('    %s,' % name)
        lines.append(')')
        self.import_lines[:] = lines
        return lines
    
    def createDestination(self, dstFile=None, import_lines=None):
        if dstFile is None:
            dstFile = self.dstFile
        if import_lines is None:
            import_lines = self.import_lines
        try:
            oldData = open(dstFile, 'r').readlines()
        except IOError, e:
            if e[0] == 2: # No such file or directory
                oldData = []
            else:
                raise
        newData = []
        if len(import_lines) > 2:
            for line in import_lines:
                newData.append("%s\n" % line)
        skip = False
        for line in oldData:
            sline = line.rstrip()
            if skip:
                if sline == ')':
                    skip = False
                continue
            if sline == import_lines[0]:
                skip = True
                continue
            newData.append(line)
        newData = "".join(newData)
        open(dstFile, 'w').write(newData)

if __name__== '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option(
        "--gwt",
        dest="gwt",
        default=False,
        action="store_true",
        help="Add all gwt imports to pyjamas",
    )
    parser.add_option(
        "--base-directory",
        dest="base_directory",
        default='.',
        help="Directory to search for files",
    )
    options, args = parser.parse_args()
    if options.gwt and len(args) > 0:
        raise ValueError("--gwt and arguments are mutually exclusive")
    if not options.gwt and len(args) == 0:
        raise ValueError("Missing src and dst file or --gwt")
    if not options.gwt:
        if len(args) != 2:
            raise ValueError("Too many arguments")
        srcFile = os.path.join(dirname, sys.argv[1])
        dstFile = os.path.join(dirname, sys.argv[2])
        ci = CreateImports(
            srcFile, 
            dstFile, 
            base_directory=options.base_directory,
        )
        ci.getImportNames()
        ci.createImportLines()
        ci.createDestination()
    else:
        gwtbase = os.path.join(options.base_directory, "gwt")
        pyjsbase = os.path.join(options.base_directory, "pyjamas")
        for dirname, subdirs, files in os.walk(gwtbase):
            if 'platform' in subdirs:
                subdirs.remove('platform')
            for f in files:
                if not f.lower().endswith(".py"):
                    continue
                srcFile = os.path.join(dirname, f)
                dstFile = srcFile.replace(gwtbase, pyjsbase)
                ci = CreateImports(
                    srcFile, 
                    dstFile, 
                    base_directory=options.base_directory,
                )
                ci.getImportNames()
                ci.createImportLines()
                ci.createDestination()
