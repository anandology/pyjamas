from django.db.models import *

class Page(Model):
	name = CharField(max_length=50)
	text = TextField()

	def __unicode__(self):
		return str(self.text)

