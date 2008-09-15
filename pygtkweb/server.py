#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Copyright 2007 Lluís Pàmies i Juárez and contributors
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

import sys
import os
from os.path import join, dirname, basename
from optparse import OptionParser
from jsonrpc import SimpleServiceHandler
import mimetypes
import wsgiserver
import inspect
import builder

class PyjamasExternalHandler:
    def call(self, module, function, args):
        try:
            mod = __import__(module)
            res = getattr(mod, function)(*args)
            return res
        except Exception,e:
            print e
    
    def methods(self, module):
        mod = __import__(module)
        members = inspect.getmembers(mod)
        methods = []
        for member in members:
            if inspect.ismethod(member[1]) or inspect.isfunction(member[1]):
                methods.append(member[0])
        return methods

class PyjamasObjectHandler(SimpleServiceHandler):
    def __init__(self, service):
        self.sendData =[]
        SimpleServiceHandler.__init__(self, service, messageDelimiter='\n')
    
    def send(self, data):
        self.sendData.append(data)
        
    def handle(self, environ, start_response):
        try:
            contLen=int(environ['CONTENT_LENGTH'])
            data = environ['wsgi.input'].read(contLen)
        except:
            print 'No content received'
        
        self.handlePartialData(data) 
        start_response('200 OK', [('Content-Type','text/plain')])
        response, self.sendData = self.sendData, []
        return response
        
class PyGtkServer:
    def __init__(self, file_name, temp_dir):
        self.temp_dir = temp_dir
        builder.app_library_dirs.append(dirname(file_name))
        builder.build(file_name, output=temp_dir, notfound_callback=self._translator_callback)
        print 'You access to the application following this link: http://localhost:9000/app/index.html'
        self._start_server()
    
    def _translator_callback(self, translator, node, attrs):
        if node.name in translator.external_modules:
            if translator.imported_modules.count('PyExternalMod')==0:
                translator.imported_modules.append('PyExternalMod')
            print >>translator.output, "var %s= _PyExternalMod_PyjamasExternalModule([\"%s\"],{});"%(node.name,node.name)
            return node.name+'.'+'.'.join(attrs)
        else:
            return None

    def _start_server(self):
        obj_handler = PyjamasObjectHandler(PyjamasExternalHandler())
        wsgi_apps = [('/app', self._serve_application_code),
                     ('/obj', obj_handler.handle)
                    ]

        server = wsgiserver.CherryPyWSGIServer(('', 9000), wsgi_apps, server_name='localhost')

        try:
            server.start()
        except KeyboardInterrupt:
            server.stop()

    def _serve_application_code(self, environ, start_response):
        filename = os.path.join(self.temp_dir, '.'+environ['PATH_INFO'])
       
        if os.path.exists(filename):
            mtype, entype = mimetypes.guess_type(filename)
            start_response('200 OK', [('Content-type',mtype)])
            return [line for line in open(filename, 'r')]
        else:
            start_response('404 NOT FOUND', [('Content-type','text/html')])
            return ['<b>Error:</b> File not found !']


def main():
    parser = OptionParser(usage = "./server.py pygtk_app.py", version = "0.0.1")
    parser.add_option("-t", "--temp", dest="temp",
                                      help="directory to store the temporal files")
    parser.set_defaults(temp="temp")
    (options, args) = parser.parse_args()
    if len(args) != 1: parser.error("incorrect number of arguments")

    server = PyGtkServer(args[0], options.temp)

if __name__=='__main__':
    main()
