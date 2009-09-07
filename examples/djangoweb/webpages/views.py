# Create your views here.

from jsonrpc import *
from djangoweb.webpages.models import Page 
from django.template import loader
from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from django.http import HttpResponseRedirect, HttpResponse
import urllib

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
    p = Page.objects.get(name=path)
    f.write("page: %s \n" % (str(p)))
    f.close()
    args = {'title': p.name,
            'noscript': p.text
            }
    context_instance=RequestContext(request)
    context_instance.autoescape=False
    try:
        template = Page.objects.get(name='index.html')
    except Page.DoesNotExist:
        template = None
    if not template:
        return render_to_response('index.html', args, context_instance)
    tpl = loader.get_template_from_string(template)
    context_instance.update(args)
    tpl = tpl.render(context_instance)
    return HttpResponse(tpl)

@jsonremote(service)
def getPage (request, num):
	return json_convert([Page.objects.get(id=num)])

@jsonremote(service)
def getPageByName (request, name):
	return json_convert([Page.objects.get(name=name)])

@jsonremote(service)
def getPages (request):
	return json_convert(Page.objects.all())

@jsonremote(service)
def updatePage (request, item):
	t = Page.objects.get(id=item['id'])
	t.name = item['name']
	t.text = item['text']
	t.save()
	return getPages(request)

@jsonremote(service)
def addPage (request, item):
	t = Page()
	t.name = item['name']
	t.text = item['text']
	t.save()
	return getPages(request)

@jsonremote(service)
def deletePage (request, num):
	t = Page.objects.get(id=num)
	t.delete()
	return getPages(request)

