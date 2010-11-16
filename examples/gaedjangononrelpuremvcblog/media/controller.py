"""
By Scott Scites <scott.scites@railcar88.com>
Copyright(c) 2010 Scott Scites, Some rights reserved.
"""

from puremvc.patterns.command import SimpleCommand
from model import PostRemoteProxy
from view import HomeMediator
from view import WriteMediator
from view import EditMediator


class StartupCommand(SimpleCommand):
    def execute(self, note):
        self.facade.registerProxy(PostRemoteProxy())
        main_panel = note.getBody()
        self.facade.registerMediator(HomeMediator
                (main_panel.home_panel))
        self.facade.registerMediator(WriteMediator
                (main_panel.write_panel))
        self.facade.registerMediator(EditMediator
                (main_panel.edit_panel))


class GetPostsCommand(SimpleCommand):
    def execute(self, note):
        facade = self.facade
        postProxy = facade.retrieveProxy(PostRemoteProxy.NAME)
        postProxy.retrieve_posts()
