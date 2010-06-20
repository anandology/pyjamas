import web
from JsonHandler import *

urls = (
    '/json', 'Wiki'
    )

class Wiki(JsonHandler):

    def find_one(self, name):
        try:
            f = open("wikipages/%s.txt" % name)
            text = f.read()
            f.close()
            return {'name': name, 'content': text}
        except:
            return {'name':name, 
                    'content':'Nothing here... yet'}

    def insert(self, name, content):
        f = open("wikipages/%s.txt" % name, "w")
        f.write(content)
        f.close()
        return 'ok'

app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__":
    import os
    os.mkdir('wikipages')
    app.run()
