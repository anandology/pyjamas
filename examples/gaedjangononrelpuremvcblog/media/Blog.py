"""
By Scott Scites <scott.scites@railcar88.com>
Copyright(c) 2010 Scott Scites, Some rights reserved.
"""
import pyjd

from puremvc.patterns.facade import Facade
from controller import StartupCommand
from controller import GetPostsCommand
from components import PyJsApp


class AppFacade(Facade):

    STARTUP = "startup"

    ADD_POST = "addPost"
    EDIT_POST = "editPost"
    DELETE_POST = "deletePost"

    GET_POSTS = "getPosts"
    POSTS_RETRIEVED = "postsRetrieved"
    EDIT_CANCELED = "editCanceled"

    VIEW_WRITE_POST = "viewWritePost"
    VIEW_EDIT_POST = "viewEditPost"
    POST_REMOTE_FAILURE = "postRemoteFailure"
    POST_REMOTE_NONE = "postRemoteNone"
    POST_ADDED = "postAdded"
    POST_EDITED = "postEdited"
    POST_DELETED = "postDeleted"

    def __init__(self):
        self.initializeFacade()

    @staticmethod
    def getInstance():
        return AppFacade()

    def initializeFacade(self):
        super(AppFacade, self).initializeFacade()

        self.initializeController()
        """
        Registers commands.
        """
    def initializeController(self):
        super(AppFacade, self).initializeController()
        (super(AppFacade, self).registerCommand
                (AppFacade.STARTUP, StartupCommand))
        (super(AppFacade, self).registerCommand
                (AppFacade.GET_POSTS, GetPostsCommand))

if __name__ == '__main__':
    pyjd.setup("./public/Blog.html")
    app = AppFacade.getInstance()
    pyjs_app = PyJsApp()
    app.sendNotification(AppFacade.STARTUP, pyjs_app.app_frame)
    app.sendNotification(AppFacade.GET_POSTS, pyjs_app.app_frame)
    pyjd.run()
