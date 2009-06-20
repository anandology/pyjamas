#!/usr/bin/env python

class Service:
    def echo(self, msg):
        return msg

    def reverse(self, msg):
        return msg[::-1]

    def uppercase(self, msg):
        return msg.upper()

    def lowercase(self, msg):
        return msg.lower()


if __name__ == '__main__':
    # this is if JSONService.py is run as a CGI
    from jsonrpc.cgihandler import handleCGIRequest
    handleCGIRequest(Service())
else:
    # this is if JSONService.py is run from mod_python:
    # rename .htaccess.mod_python to .htaccess to activate,
    # and restart Apache2
    from jsonrpc.apacheServiceHandler import handler 
