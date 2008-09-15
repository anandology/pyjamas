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


from jsonrpc.cgihandler import handleCGIRequest

handleCGIRequest(Service())

