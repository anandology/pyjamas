
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn, ForkingMixIn
import sys
import os
import cgi
import mimetypes
import shutil
import urlparse
import posixpath
import urllib

class Server:
    
    def __init__(self):
        server_address = ('', 8080)
        httpd = TestHTTPServer(server_address, TestRequestHandler)
        httpd.serve_forever()


class TestHTTPServer(ThreadingMixIn, HTTPServer):
    pass
    
    
class TestRequestHandler(BaseHTTPRequestHandler):
    
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        self.protocol_version = 'HTTP/1.1'
        
    def do_GET(self):
        self.handle_data()
        
    def do_POST(self):
        self.form = cgi.FieldStorage(
                        fp=self.rfile,
                        headers=self.headers,
                        environ={'REQUEST_METHOD':'POST',
                                 'CONTENT_TYPE':self.headers['Content-Type'],
                                     },
                        keep_blank_values=True,
                        strict_parsing=False)
        self.handle_data()
        
    def handle_data(self):
        if self.path == '/':
            p = '/html/swfu.html'
        elif self.path.endswith('upload.html'):
            self.handleUpload()
            return
        else:
            p = self.path
        path = self.translate_path(p)
        if not os.path.exists(path):
            p = '/html'+p
            path = self.translate_path(p)
        ctype = self.guess_type(path)
        try:
            f = open(path)
        except IOError:
            print 'File not found %s' % path
            self.send_error(404, 'File not found')
            return
        self.send_response(200)
        self.send_header('Content-type', ctype)
        self.send_header('Last-Modified', self.date_time_string())
        self.end_headers()
        self.copyfile(f, self.wfile)
        f.close()
    
    def handleUpload(self):
        self.send_response(200)
        self.end_headers()
        fileitem = self.form['Filedata']
        filename = os.path.basename(fileitem.filename)
        filepath = os.path.join(os.getcwd(), 'upload', filename)
        f = open(filepath, 'wb', 10000)
        def fbuffer(f, chunk_size=10000):
            while True:
                chunk = f.read(chunk_size)
                if not chunk: break
                yield chunk
        for chunk in fbuffer(fileitem.file):
            f.write(chunk)
        f.close()
        self.wfile.write('Upload done')
        return
            
    def translate_path(self, path):
        path = path.decode('utf-8')
        path = urlparse.urlparse(path)[2]
        path = posixpath.normpath(urllib.unquote(path))
        words = path.split('/')
        words = filter(None, words)
        path = os.getcwd()
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir): continue
            path = os.path.join(path, word)
        return path
    
    def copyfile(self, source, outputfile):
        shutil.copyfileobj(source, outputfile)
        
    def guess_type(self, path):
        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        ext = ext.lower()
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        else:
            return self.extensions_map['']

    if not mimetypes.inited:
        mimetypes.init() # try to read system mime.types
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'application/octet-stream', # Default
        })

    
if __name__ == '__main__':
    Server()
    