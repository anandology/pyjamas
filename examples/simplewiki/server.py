import web
from JsonHandler import *
import pymongo

urls = (
    '/json', 'Wiki'
    )

class Wiki(JsonHandler):
    def __init__(self):
        connection = pymongo.Connection()
        self.pages = connection.wiki.pages

    def find_one(self, name):
        p = self.pages.find_one({'name':name})
        if p:
            # unfortunatly, we have to delete the id because
            # it's not serializable
            del p['_id']
            return p
        else:
            return {'name':name, 
                    'content':'Nothing here... yet'}

    def insert(self, name, content):
        self.pages.update({'name':name},
                {'$set':{'content':content}},
                upsert=True)
        return 'ok'

app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__": app.run()
