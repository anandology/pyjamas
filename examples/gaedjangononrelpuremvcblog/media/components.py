"""
By Scott Scites <scott.scites@railcar88.com>
Copyright(c) 2010 Scott Scites, Some rights reserved.
"""

from pyjamas.ui.Hidden import Hidden
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.AbsolutePanel import AbsolutePanel
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.Label import Label
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HTML import HTML
from pyjamas import Window


class PyJsApp(object):

    app_frame = None

    def __init__(self):
        self.app_frame = AppFrame()


class AppFrame(object):

    edit_panel = None
    home_panel = None
    write_panel = None

    def __init__(self):
        self.panel = AbsolutePanel()
        self.edit_panel = EditPanel(self)
        self.home_panel = HomePanel(self)
        self.write_panel = WritePanel(self)
        self.panel.add(self.edit_panel)
        self.panel.add(self.home_panel)
        self.panel.add(self.write_panel)
        RootPanel().add(self.panel)


class EditPanel(AbsolutePanel):

    def __init__(self, key, title, content):
        AbsolutePanel.__init__(self)
        self.edit_header = Label("Edit a Post", StyleName="header_label")
        self.edit_title_label = Label("Title:")
        self.edit_title = TextBox()
        self.edit_title.setMaxLength(255)
        self.edit_content = TextArea()
        self.edit_content.setVisibleLines(2)
        self.edit_button = Button("Save")
        self.edit_cancel_button = Button("Cancel")
        self.edit_hidden_key = Hidden()
        self.error_message_label = Label("", StyleName="error_message_label")
        edit_contents = VerticalPanel(StyleName="Contents", Spacing=4)
        edit_contents.add(self.edit_header)
        edit_contents.add(self.edit_title_label)
        edit_contents.add(self.edit_title)
        edit_contents.add(self.edit_content)
        edit_contents.add(self.edit_button)
        edit_contents.add(self.edit_cancel_button)
        edit_contents.add(self.error_message_label)
        edit_contents.add(self.edit_hidden_key)
        self.edit_dialog = DialogBox(glass=True)
        self.edit_dialog.setHTML('<b>Blog Post Form</b>')
        self.edit_dialog.setWidget(edit_contents)
        left = (Window.getClientWidth() - 900) / 2 + Window.getScrollLeft()
        top = (Window.getClientHeight() - 600) / 2 + Window.getScrollTop()
        self.edit_dialog.setPopupPosition(left, top)
        self.edit_dialog.hide()

    def clear_edit_panel(self):
        self.edit_title.setText("")
        self.edit_content.setText("")
        self.error_message_label.setText("")


class HomePanel(AbsolutePanel):

    def __init__(self, parent):
        AbsolutePanel.__init__(self)
        self.home_header = Label("Blogjamas", StyleName="header_label")
        self.write_button = Button("Write a Post")
        self.edit_hidden_button = Button("", StyleName="hidden_button")
        self.delete_hidden_button = Button("", StyleName="hidden_button")
        self.add(self.home_header)
        self.add(self.write_button)
        self.add(self.edit_hidden_button)
        self.add(self.delete_hidden_button)

    def update_posts(self, posts):
        self.contents = VerticalPanel(Spacing=1)
        for i in range(len(posts)):
            self.divider = HTML("----------------------------------------------------")
            self.contents.add(self.divider)
            self.post_title = Label(posts[i].title, StyleName="title_label")
            self.contents.add(self.post_title)
            self.post_content = Label(posts[i].content, StyleName="content_label")
            self.contents.add(self.post_content)
            self.edit_button = Button("Edit")
            self.edit_button.setID("edit_" + posts[i].post_id)
            self.edit_button.addClickListener(self.show_edit_box)
            self.contents.add(self.edit_button)
            self.delete_button = Button("Delete")
            self.delete_button.setID("delete_" + posts[i].post_id)
            self.delete_button.addClickListener(self.delete_post)
            self.contents.add(self.delete_button)
        self.add(self.contents)

    def show_edit_box(self, sender):
        self.edit_hidden_button.setID(sender.getID())
        self.edit_hidden_button.click(self)

    def delete_post(self, sender):
        self.delete_hidden_button.setID(sender.getID())
        self.delete_hidden_button.click(self)


class WritePanel(AbsolutePanel):

    def __init__(self, parent):
        AbsolutePanel.__init__(self)
        self.post_header = Label("Write a Post", StyleName="header_label")
        self.post_write_title_label = Label("Title:")
        self.post_title = TextBox()
        self.post_content = TextArea()
        self.post_button = Button("Post")
        self.cancel_button = Button("Cancel")
        self.error_message_label = Label("", StyleName="error_message_label")
        contents = VerticalPanel(StyleName="Contents", Spacing=4)
        contents.add(self.post_header)
        contents.add(self.post_write_title_label)
        contents.add(self.post_title)
        contents.add(self.post_content)
        contents.add(self.post_button)
        contents.add(self.cancel_button)
        contents.add(self.error_message_label)
        self.dialog = DialogBox(glass=True)
        self.dialog.setHTML('<b>Blog Post Form</b>')
        self.dialog.setWidget(contents)
        left = (Window.getClientWidth() - 900) / 2 + Window.getScrollLeft()
        top = (Window.getClientHeight() - 600) / 2 + Window.getScrollTop()
        self.dialog.setPopupPosition(left, top)
        self.dialog.hide()

    def clear_write_panel(self):
        self.post_title.setText("")
        self.post_content.setText("")
        self.error_message_label.setText("")
