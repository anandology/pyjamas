"""
By Scott Scites <scott.scites@railcar88.com>
Copyright(c) 2010 Scott Scites, Some rights reserved.
"""


class PostVO(object):
    post_id = None
    title = None
    content = None

    def __init__(self, post_id=None, title=None,
            content=None):
        if post_id:
            self.post_id = post_id
        if title:
            self.title = title
        if content:
            self.content = content

    def is_empty(self):
        if self.post_id:
            return False
        if self.title:
            return False
        if self.content:
            return False
        return True
