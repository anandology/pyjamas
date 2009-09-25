# Create your views here.

from jsonrpc import *
from djangowanted.wanted.models import Item, Flag, FlagType 
from django.template import loader
from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from django.http import HttpResponseRedirect, HttpResponse
import urllib

from wanted.forms import ItemForm

formsservice = FormProcessor({'itemform': ItemForm})

service = JSONRPCService()

def index(request, path=None):
    f = open("/tmp/log.txt", "a")
    f.write("path: %s\n" % str(path))
    f.write("request: %s\n" % str(request))
    path = request.GET.get('page', None)
    if path == '':
        path = 'index'
    f.write("pth: %s \n" % (path))
    if path is None:
        # workaround in history tokens: must have a query
        return HttpResponseRedirect("./?page=#index")
    p = Item.objects.get(name=path)
    f.write("page: %s \n" % (str(p)))
    f.close()
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

@jsonremote(service)
def getItem (request, num):
    try:
        item = Item.objects.get(id=num)
    except Item.DoesNotExist:
        return None
    return json_convert([item])[0]

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
    return json_convert([t])[0]

@jsonremote(service)
def deleteItem (request, num):
    t = Item.objects.get(id=num)
    t.delete()
    return num

