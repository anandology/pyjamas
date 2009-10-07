""" Pyjamas Django Forms Integration

    Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>

"""

from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Grid import Grid
from pyjamas.ui.FormPanel import FormPanel
#from pyjamas.ui.Composite import Composite
from pyjamas.log import writebr

from pyjamas.ui.TextBox import TextBox

class CharField(TextBox):
    def __init__(self, **kwargs):
        TextBox.__init__(self)
        self.max_length = kwargs.get('max_length', None)
        self.min_length = kwargs.get('min_length', None)
        self.required = kwargs.get('required', None)
        if kwargs.get('initial'):
            self.setValue(kwargs['initial'])

    def setValue(self, val):
        if val is None:
            val = ''
        self.setText(val)

class FloatField(TextBox):
    def __init__(self, **kwargs):
        TextBox.__init__(self)
        self.max_length = kwargs.get('max_length', None)
        self.min_length = kwargs.get('min_length', None)
        self.required = kwargs.get('required', None)
        if kwargs.get('initial'):
            self.setValue(kwargs['initial'])

    def setValue(self, val):
        if val is None:
            val = ''
        self.setText(val)


widget_factory = {'CharField': CharField,
                  'FloatField': FloatField
                 }

class FormDescribeGrid:

    def __init__(self, sink):
        self.sink = sink

    def onRemoteResponse(self,  response, request_info):

        method = request_info.method

        writebr(repr(response))
        writebr("%d" % len(response))
        writebr("%s" % repr(response.keys()))

        self.do_describe(response)

    def do_describe(self, fields):

        keys = fields.keys()
        self.sink.fields = keys
        for idx, fname in enumerate(fields.keys()):
            field = fields[fname]
            if self.sink.data and self.sink.data.has_key(fname):
                field['initial'] = self.sink.data[fname]
            writebr("%s %s %d" % (fname, field['label'], idx))
            field_type = field['type']
            widget_kls = widget_factory.get(field_type, CharField)
            fv = {}
            for (k, v) in field.items():
                fv[str(k)] = v
            w = widget_kls(**fv)
            self.sink.add_widget(field['label'], w)

class Form(FormPanel):

    def __init__(self, svc, **kwargs):

        if kwargs.has_key('data'):
            data = kwargs.pop('data')
        else:
            data = None
        writebr(repr(data))

        FormPanel.__init__(self, **kwargs)
        self.svc = svc
        self.grid = Grid()
        self.grid.resize(0, 2)
        self.add(self.grid)
        self.form = FormDescribeGrid(self)
        self.formsetup(data)

    def add_widget(self, description, widget):

        num_rows = self.grid.getRowCount()
        self.grid.resize(num_rows+1, 2)
        self.grid.setHTML(num_rows, 0, description)
        self.grid.setWidget(num_rows, 1, widget)

    def formsetup(self, data=None):

        if data is None:
            data = {}
        self.data = data
        writebr(repr(self.data))
        self.svc({}, {'describe': None}, self.form)

    def update_values(self, data = None):
        if data is not None:
            self.data = data

        for idx, fname in enumerate(self.fields):
            val = None
            if self.data.has_key(fname):
                val = self.sink.data[fname]
            w = self.sink.grid.getWidget(idx, 1)
            w.setValue(val)

