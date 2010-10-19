from django.shortcuts import render_to_response
from jsonrpc import *
from gaedjangononrelpuremvcblog.post.models import Post

service = JSONRPCService()

def index(request):
    return render_to_response('index.html')

@jsonremote(service)
def get_post(request, num):
    post = Post.objects.get(id=num)
    return [(str(post.pk), str(post.title), str(post.content))]

@jsonremote(service)
def get_posts(request):
    return [(str(post.pk), str(post.title), str(post.content)) for post in Post.objects.all()]

@jsonremote(service)
def update_post(request, key, title, content):
    post = Post.objects.get(id=key)
    post = map_remote_post_to_local_post(title, content, post)
    post.save()
    return get_post(request, post.pk) 

@jsonremote(service)
def add_post(request, title, content):
    post = Post()
    post = map_remote_post_to_local_post(title, content, post)
    post.save()
    return get_post(request, post.pk)

def map_remote_post_to_local_post(title, content, post):
    post.title = title
    post.content= content
    return post

@jsonremote(service)
def delete_post(request, num):
	post = Post.objects.get(id=num)
	post.delete()
	return num
