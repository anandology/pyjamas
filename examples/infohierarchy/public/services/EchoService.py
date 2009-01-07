#!/usr/bin/env python

import os
from string import split, strip

def get_directory_info(prefix, pth, recursive):
    res = []
    for p in os.listdir(pth):
        if p != '.' and p != '..':
            subp = os.path.join(pth, p)
            p = os.path.join(prefix, p)
            if recursive and os.path.isdir(subp):
                res.append([p, get_directory_info(prefix, subp, 1)])
            else:
                res.append([p, None])
    return res

class Service:
    def index(self, dirname, recursive):
        """ return list of directory, including indicating whether each
            path is a directory or not
        """
        pth = os.path.join(os.getcwd(), "structure")
        pth = os.path.join(pth, dirname)
        res = get_directory_info(dirname, pth, recursive)
        return res

    def get_rightpanel_datanames(self, fname):
        pth = os.path.join(os.getcwd(), "data")
        pth = "%s/%s" % (pth, fname)
        return get_directory_info(fname, pth, 0)

    def get_rightpanel_data(self, fname):
        pth = os.path.join(os.getcwd(), "data")
        pth = "%s/%s" % (pth, fname)
        f = open(pth)
        res = []
        for l in f.readlines():
            l = l.strip()
            if not l:
                continue
            cidx = l.find(":")
            if cidx == -1:
                continue
            location = l[:cidx].strip()
            location = location.split(",")
            if not len(location) == 2:
                continue
            location = map(strip, location)
            [x, y] = map(int, location)
            data = l[cidx+1:].lstrip()

            res.append([x, y, data])

        return res

    def get_midpanel_data(self, fname):
        pth = os.path.join(os.getcwd(), "structure")
        pth = "%s/%s" % (pth, fname)
        f = open(pth)
        res = []
        for l in f.readlines():
            l = l.strip()
            if not l:
                continue
            l = l.split(":")
            if not len(l) == 2:
                continue
            l = map(strip, l)
            res.append(l)

        return res

    def uppercase(self, msg):
        return msg.upper()

    def lowercase(self, msg):
        return msg.lower()


from jsonrpc.cgihandler import handleCGIRequest

handleCGIRequest(Service())

