class XULrunnerHackCallback:
    def __init__(self, htr, mode, user, pwd, url, postData=None, handler=None,
                        return_xml=0, content_type='text/plain charset=utf8'):
        print "XMLHttpRequest using xulrunner hack callback", mode, url
        self.htr = htr
        self.mode = mode
        self.user = user
        self.pwd = pwd
        self.url = url
        self.postData = postData
        self.handler = handler
        self.return_xml = return_xml
        self.content_type = content_type

        pyjd.add_timer_queue(self.callback)

class HTTPRequest:
    # also callable as: asyncPost(self, url, postData, handler)
    def asyncPost(self, user, pwd, url, postData=None, handler=None,
                        return_xml=0, content_type='text/plain charset=utf8'):
        if postData is None:
            return XULrunnerHackCallback(self, 'POST',
                                     None, None, user, pwd, url,
                                      return_xml, content_type)
        return XULrunnerHackCallback(self, 'POST',
                                 user, pwd, url, postData, handler,
                                 return_xml, content_type)

    # also callable as: asyncGet(self, url, handler)
    def asyncGet(self, user, pwd, url=None, handler=None,
                        return_xml=0, content_type='text/plain charset=utf8'):
        if url is None:
            return XULrunnerHackCallback(self, 'GET', None, None, user,
                                         handler=pwd,
                                         return_xml=return_xml, 
                                         content_type=content_type)
        return XULrunnerHackCallback(self, 'GET', user, pwd, url,
                                     handler=handler, 
                                     return_xml=return_xml, 
                                     content_type=content_type)

