# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
#
# Pyjamas Widget Factory.  register widgets with this module,
# for dynamic use in applications.  please observe namespaces.
#
# * pyjamas.ui namespace is used for widgets in library/pyjamas/ui

#from __pyjamas__ import doc

factory = {}

def registerClass(name, kls):
    global factory
    factory[name] = kls

def lookupClass(name):
    return factory[name]

def addPyjamasNameSpace():
    doc().createElementNS("urn:schemas-pyjs-org:pyjs")
    #try:
    #    ns = doc().namespaces.item("pyjs")
    #except:
    #    doc().namespaces.add("pyjsinit", "urn:schemas-pyjs-org:pyjs")
        #doc().createStyleSheet().cssText = "v\\:*{behavior:url(#default#VML);}"


