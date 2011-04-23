# Create your views here.

from django.pimentech.network import *
from todo.models import Todo 

service = JSONRPCService()

@jsonremote(service)
def getTasks (request):
	return [(str(task),task.id) for task in Todo.objects.all()]


@jsonremote(service)
def addTask (request, taskFromJson):
	t = Todo()
	t.task = taskFromJson
	t.save()
	return getTasks(request)

@jsonremote(service)
def deleteTask (request,idFromJson):
	t = Todo.objects.get(id=idFromJson)
	t.delete()
	return getTasks(request)

