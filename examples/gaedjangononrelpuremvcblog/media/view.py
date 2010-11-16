"""
By Scott Scites <scott.scites@railcar88.com>
Copyright(c) 2010 Scott Scites, Some rights reserved.
"""

from puremvc.patterns.mediator import Mediator
import model
import Blog


class HomeMediator(Mediator):
    NAME = "HomeMediator"
    post_remote_proxy = None

    def __init__(self, viewComponent):
        super(HomeMediator, self).__init__(HomeMediator.NAME, viewComponent)
        self.viewComponent.mediator = self
        self.post_remote_proxy = self.facade.retrieveProxy(model.PostRemoteProxy.NAME)
        self.viewComponent.write_button.addClickListener(self.on_write_click)
        self.viewComponent.edit_hidden_button.addClickListener(self.on_edit_click)
        self.viewComponent.delete_hidden_button.addClickListener(self.on_delete_click)

    def listNotificationInterests(self):
        return [Blog.AppFacade.POSTS_RETRIEVED,
                Blog.AppFacade.POST_ADDED,
                Blog.AppFacade.POST_EDITED,
                Blog.AppFacade.POST_DELETED,
                Blog.AppFacade.EDIT_CANCELED]

    def handleNotification(self, note):
        note_name = note.getName()
        if note_name == Blog.AppFacade.POSTS_RETRIEVED:
            self.update_posts()
        if note_name == Blog.AppFacade.POST_ADDED:
            self.clear_update_posts()
        if note_name == Blog.AppFacade.POST_EDITED:
            self.clear_update_posts()
        if note_name == Blog.AppFacade.POST_DELETED:
            self.clear_update_posts()
        if note_name == Blog.AppFacade.EDIT_CANCELED:
            self.clear_hidden_id()

    def clear_update_posts(self):
        self.clear_posts()
        self.clear_hidden_id()
        self.update_posts()

    def clear_posts(self):
        self.viewComponent.remove(self.viewComponent.contents)

    def clear_hidden_id(self):
        self.viewComponent.edit_hidden_button.setID("")
        self.viewComponent.delete_hidden_button.setID("")

    def update_posts(self):
        posts = self.post_remote_proxy.get_reversed_posts()
        self.viewComponent.update_posts(posts)

    def on_write_click(self):
        self.sendNotification(Blog.AppFacade.VIEW_WRITE_POST)

    def is_click_id_set(self, sender_id):
        if sender_id == "" or sender_id == None:
            return False
        return True

    def on_edit_click(self, sender=None):
        if self.is_click_id_set(sender.getID()):
            self.sendNotification(Blog.AppFacade.VIEW_EDIT_POST, sender.getID())

    def on_delete_click(self, sender=None):
        if self.is_click_id_set(sender.getID()):
            key = sender.getID()
            post_id = key.replace("delete_", "")
            self.post_remote_proxy.delete_remote_post(post_id)


class WriteMediator(Mediator):
    NAME = "WriteMediator"
    post_remote_proxy = None

    def __init__(self, viewComponent):
        super(WriteMediator, self).__init__(WriteMediator.NAME, viewComponent)
        self.viewComponent.mediator = self
        self.post_remote_proxy = self.facade.retrieveProxy(model.PostRemoteProxy.NAME)
        self.viewComponent.post_button.addClickListener(self.add_post)
        self.viewComponent.cancel_button.addClickListener(self.on_close)

    def listNotificationInterests(self):
        return [Blog.AppFacade.VIEW_WRITE_POST]

    def handleNotification(self, note):
        note_name = note.getName()
        if note_name == Blog.AppFacade.VIEW_WRITE_POST:
            self.view_write_post(self)

    def view_write_post(self, event):
        self.viewComponent.clear_write_panel()
        self.viewComponent.dialog.show()
        self.viewComponent.post_title.setFocus(True)

    def on_close(self, event):
        self.viewComponent.dialog.hide()

    def validate_add(self):
        error_message = ""
        title = self.viewComponent.post_title.getText()
        if title == "":
            self.viewComponent.post_title.setFocus(True)
            return ("Title is a required field", title, content)
        content = self.viewComponent.post_content.getText()
        if content == "":
            self.viewComponent.post_content.setFocus(True)
            return ("Content is a required field", title, content)
        if len(content) > 255:
            self.viewComponent.post_content.setFocus(True)
            return ("Post body must be less than 256 characters. It is " + str(len(content)), title, content)
        return (error_message, title, content)

    def add_post(self, event):
        error_message, title, content = self.validate_add()
        if len(error_message) > 0:
            (self.viewComponent.
                error_message_label.
                setText(error_message))
            return
        title = self.viewComponent.post_title.getText()
        content = self.viewComponent.post_content.getText()
        self.post_remote_proxy.add_remote_blog_post(title, content)
        self.on_close()


class EditMediator(Mediator):
    NAME = "EditMediator"
    edit_remote_proxy = None

    def __init__(self, viewComponent):
        super(EditMediator, self).__init__(EditMediator.NAME, viewComponent)
        self.viewComponent.mediator = self
        self.edit_remote_proxy = self.facade.retrieveProxy(model.PostRemoteProxy.NAME)
        self.viewComponent.edit_button.addClickListener(self.edit_post)
        self.viewComponent.edit_cancel_button.addClickListener(self.on_edit_close)

    def listNotificationInterests(self):
        return [Blog.AppFacade.VIEW_EDIT_POST]

    def handleNotification(self, note):
        note_name = note.getName()
        note_body = note.getBody()
        if note_name == Blog.AppFacade.VIEW_EDIT_POST:
            self.view_edit_post(note_body)

    def view_edit_post(self, post_key):
        self.viewComponent.clear_edit_panel()
        self.viewComponent.edit_dialog.show()
        post_id = post_key.replace("edit_", "")
        post = self.edit_remote_proxy.get_post(post_id)
        self.viewComponent.edit_title.setText(post.title)
        self.viewComponent.edit_title.setFocus(True)
        self.viewComponent.edit_content.setText(post.content)
        self.viewComponent.edit_hidden_key.setValue(post_id)

    def validate_edit(self):
        error_message = ""
        key = self.viewComponent.edit_hidden_key.getValue()
        if key == "":
            return ("Cannot update without a post identifier", key, title, content)
        title = self.viewComponent.edit_title.getText()
        if title == "":
            self.viewComponent.edit_title.setFocus(True)
            return ("Title is a required field", key, title, content)
        content = self.viewComponent.edit_content.getText()
        if content == "":
            self.viewComponent.edit_content.setFocus(True)
            return ("Content is a required field", key, title, content)
        if len(content) > 255:                                                                                                               
            self.viewComponent.edit_content.setFocus(True)                                                                                   
            return ("Post body must be less than 255 characters. It is " + str(len(content)), key, title, content)
        return (error_message, key, title, content)

    def on_edit_close(self, event):
        self.viewComponent.edit_dialog.hide()
        self.sendNotification(Blog.AppFacade.EDIT_CANCELED)

    def edit_post(self, event):
        error_message, key, title, content = self.validate_edit()
        if len(error_message) > 0:
            (self.
                viewComponent.
                error_message_label.
                setText(error_message))
            return
        self.edit_remote_proxy.edit_remote_blog_post(key, title, content)
        self.on_edit_close()
