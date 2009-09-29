""" Pyjamas Django Forms Integration

    Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>

"""

from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Composite import Composite
from pyjamas.log import writebr

from pyjamas.ui.TextBox import TextBox

class CharField(TextBox):
    def __init__(self, **kwargs):
        TextBox.__init__(self)
        self.max_length = kwargs.get('max_length', None)
        self.min_length = kwargs.get('min_length', None)
        self.required = kwargs.get('required', None)
        if kwargs.get('initial'):
            self.setText(kwargs['initial'])

widget_factory = {'CharField': CharField}

class FormDescribeGrid:

    def __init__(self, grid):
        self.grid = grid

    def onRemoteResponse(self,  response, request_info):

        method = request_info.method

        writebr(repr(response))
        writebr("%d" % len(response))
        writebr("%s" % repr(response.keys()))

        self.do_describe(response)

    def do_describe(self, fields):

        keys = fields.keys()
        self.grid.resize(len(keys), 2)
        for idx, fname in enumerate(fields.keys()):
            field = fields[fname]
            writebr("%s %s %d" % (fname, field['label'], idx))
            field_type = field['type']
            widget_kls = widget_factory.get(field_type, CharField)
            w = widget_kls(**field)
            self.grid.setHTML(idx, 0, field['label'])
            self.grid.setWidget(idx, 1, w)

class Form(Composite):

    def __init__(self, svc, **kwargs):

        Composite.__init__(self, **kwargs)
        self.svc = svc
        self.grid = Grid()
        self.initWidget(self.grid)
        self.describe = FormDescribeGrid(self.grid)
        self.svc({}, {'describe': None}, self.describe)

