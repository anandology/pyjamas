from django.db.models import *

class Item(Model):
    name = CharField(max_length=50)
    short_description = CharField(max_length=100)
    description = TextField()
    price = IntegerField(max_length=10)
    created_date = DateField(auto_now=True, auto_now_add=True)
    updated_date = DateField(auto_now=True)

    def __unicode__(self):
        return unicode(self.description)

class FlagType(Model):
    name = CharField(max_length=50)
    description = TextField()

class Flag(Model):
    item = ForeignKey(Item)
    type = ForeignKey(FlagType)
    value = CharField(max_length=255)

class Page(Model):
	name = CharField(max_length=50)
	text = TextField()

	def __unicode__(self):
		return str(self.text)

