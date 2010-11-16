"""
By Scott Scites <scott.scites@railcar88.com>
Copyright(c) 2010 Scott Scites, Some rights reserved.
"""

from pyjamas.JSONService import JSONProxy
from puremvc.patterns.proxy import Proxy
import vo
import Blog


class PostRemoteProxy(Proxy):
    NAME = "PostRemoteProxy"

    def __init__(self):
        super(PostRemoteProxy, self).__init__(PostRemoteProxy.NAME, [])
        self.data = []
        self.remote = DataService()

    def get_posts(self):
        return self.data

    def get_reversed_posts(self):
        return sorted(self.data, key=lambda post: post.post_id, reverse=True)

    def get_post(self, post_id):
        for i in range(len(self.data)):
            if self.data[i].post_id == post_id:
                return self.data[i]

    def add_blog_post(self, post):
        self.data.append(post)

    def update_blog_post(self, post):
        for i in range(len(self.data)):
            if self.data[i].post_id == post.post_id:
                self.data[i] = post

    def delete_post(self, post_id):
        for i in range(len(self.data)):
            if self.data[i].post_id == post_id:
                del self.data[i]
                self.sendNotification(Blog.AppFacade.POST_DELETED)
                return

    def retrieve_posts(self):
        id = self.remote.get_posts(self)
        if id < 0:
            self.sendNotification(Blog.AppFacade.POST_REMOTE_FAILURE)

    """
    Adds a given C{PostVO} to the datastore.
    """
    def add_remote_blog_post(self, title, content):
        id = self.remote.add_post(title, content, self)
        if id < 0:
            self.sendNotification(Blog.AppFacade.POST_REMOTE_FAILURE)

    def edit_remote_blog_post(self, key, title, content):
        id = self.remote.update_post(key, title, content, self)
        if id < 0:
            self.sendNotification(Blog.AppFacade.POST_REMOTE_FAILURE)

    """
    Deletes a post from the datastore by its unique key.
    """
    def delete_remote_post(self, key):
        id = self.remote.delete_post(key, self)
        if id < 0:
            self.sendNotification(Blog.AppFacade.POST_REMOTE_FAILURE)

    def onRemoteResponse(self, response, request_info):
        if request_info.method == 'get_posts':
            for post in response:
                self.add_blog_post(vo.PostVO
                    (post[0], post[1], post[2]))
            self.sendNotification(Blog.AppFacade.POSTS_RETRIEVED)
        elif request_info.method == 'add_post':
            blog_post = vo.PostVO(response[0][0], response[0][1], response[0][2])
            self.add_blog_post(blog_post)
            self.sendNotification(Blog.AppFacade.POST_ADDED, blog_post)
        elif request_info.method == 'update_post':
            post = response
            for post in response:
                self.update_blog_post(vo.PostVO(post[0], post[1], post[2]))
            self.sendNotification(Blog.AppFacade.POST_EDITED)
        elif request_info.method == 'delete_post':
            post_number = response
            self.delete_post(post_number)
        else:
            self.sendNotification(Blog.AppFacade.POST_REMOTE_NONE)

    def onRemoteError(self, code, message, request_info):
        self.sendNotification(Blog.AppFacade.POST_REMOTE_FAILURE)


class DataService(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/services/", ["add_post",
            "get_posts", "update_post", "delete_post"])
