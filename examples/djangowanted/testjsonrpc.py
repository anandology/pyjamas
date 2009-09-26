import unittest
import jsonrpclib
from pprint import pprint

class TestJsolait(unittest.TestCase):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

        self.s = jsonrpclib.ServerProxy("http://127.0.0.9/services/wanted/",
                                        verbose=0)

        self.f = jsonrpclib.ServerProxy("http://127.0.0.9/services/forms/",
                                        verbose=0)

    def item_equal(self, item, fields):
        self.assert_(item.has_key('pk'))
        print item['fields']
        for fname in fields.keys():
            v = item['fields'][fname]
            if isinstance(v, dict):
                v = v['fields']['value']
            self.assert_(v == fields[fname])

    def test_createanddeleteitem(self):
        forsale = {'name': 'a car',
                   'short_description': 'a nice car',
                   'price': 20.0,
                   'vehicletype': 'a car',
                   'numdoors': '3'
                   }
        reply = self.s.addItem(forsale)
        print reply
        item = reply["result"]
        self.item_equal(item, forsale)
        to_delete = item['pk']

        reply = self.s.getItem(to_delete)
        print reply
        item = reply["result"]
        forsale = {'name': 'a car',
                   'short_description': 'a nice car',
                   'price': 20.0,
                   'vehicletype': 'a car',
                   'numdoors': '3'
                   }
        self.item_equal(item, forsale)
        reply = self.s.deleteItem(to_delete)
        print reply

        reply = self.s.getItem(to_delete)
        print reply
        item = reply["result"]
        self.assert_(item is None)
        
    def notest_itemform(self):
        reply = self.f.itemform({}, {"describe": 
                                       ['name', 'description',
                                        'short_description',
                                        'price', 'numdoors',
                                        'vehicletype']})
        pprint(reply)

        d = {'name': 'fred', 'short_description': 'joe', 'description': 'longer', 'price': 20, 'vehicletype': 'a car', 'numdoors': '5'}
        reply = self.f.itemform(d, {"save": 
                                       ['name', 'description',
                                        'short_description',
                                        'price', 'numdoors',
                                        'vehicletype']})

        pprint(reply)

    def notest_itemformerror(self):

        d = {'name': 'fred', 'short_description': 'joe', 'description': 'longer', 'price': 20, 'vehicletype': 'a car', 'numdoors': 'x' * 101}
        reply = self.f.itemform(d, {"save": 
                                       ['name', 'description',
                                        'short_description',
                                        'price', 'numdoors',
                                        'vehicletype']})

        pprint(reply)

if __name__=="__main__":
    unittest.main()
