# Create your views here.

from jsonrpc import *
from djangoweb.webpages.models import Page 

service = JSONRPCService()

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

