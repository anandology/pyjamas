# Create your views here.

from jsonrpc import *
from djangowanted.wanted.models import Item, Flag, FlagType, Page
from django.template import loader
from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from django.http import HttpResponseRedirect, HttpResponse
import urllib
from copy import copy

from wanted.forms import ItemForm

formsservice = FormProcessor({'itemform': ItemForm})

service = JSONRPCService()

def index(request, path=None):
    path = request.GET.get('page', None)
    if path == '':
        path = 'index'
    if path is None:
        # workaround in history tokens: must have a query
        return HttpResponseRedirect("./?page=#index")
    try:
        p = Page.objects.get(name=path)
    except Page.DoesNotExist:
        p = None 
    if not p and path == 'index':
        return render_to_response('index.html', {'title':'', 'noscript':''})
    args = {'title': p.name,
            'noscript': p.text
            }
    context_instance=RequestContext(request)
    context_instance.autoescape=False
    try:
        template = Item.objects.get(name='index.html')
    except Item.DoesNotExist:
        template = None
    if not template:
        return render_to_response('index.html', args, context_instance)
    tpl = loader.get_template_from_string(template)
    context_instance.update(args)
    tpl = tpl.render(context_instance)
    return HttpResponse(tpl)


def _getItem (item):
    fields = copy(item._meta.get_all_field_names())
    del fields[fields.index('flag')]
    del fields[fields.index('id')]
    for f in FlagType.objects.all():
        fields.append(f.name)
        try:
            fg = Flag.objects.get(item=item.id, type=f.id)
        except Flag.DoesNotExist:
            fg = Flag()
        setattr(item, f.name, fg)
    return json_convert([item], fields=fields)[0]

@jsonremote(service)
def getItem (request, num):
    try:
        item = Item.objects.get(id=num)
    except Item.DoesNotExist:
        return None
    return _getItem(item)

@jsonremote(service)
def getItemsByName (request, name):
    return json_convert([Item.objects.filter(name=name)])

@jsonremote(service)
def getItems (request):
    return json_convert(Item.objects.all())

@jsonremote(service)
def updateItem (request, item):
    t = Item.objects.get(id=item['id'])
    t.name = item['name']
    t.text = item['text']
    t.save()
    return getItems(request)

@jsonremote(service)
def addItem (request, item):
    t = Item()
    t.name = item['name']
    t.short_description = item['short_description']
    t.price = item['price']
    t.save()
    fields = copy(t._meta.get_all_field_names())
    del fields[fields.index('flag')]
    del fields[fields.index('id')]
    for f in FlagType.objects.all():
        fields.append(f.name)
        fv = item[f.name]
        d = {'item': t.id, 'type': f.id, 'value': fv}
        try:
            fg = Flag.objects.get(item=t.id, type=f.id)
        except Flag.DoesNotExist:
            fg = Flag()
            fg.item = t
            fg.type = f
        fg.value = fv
        fg.save()
        setattr(t, f.name, fg)
    f = open("/tmp/additem.txt", "w")
    f.write("%s %s\n" % (repr(fields), repr(dir(t))))
    f.close()
    return json_convert([t], fields=fields)[0]

@jsonremote(service)
def deleteItem (request, num):
    t = Item.objects.get(id=num)
    t.delete()
    return num

