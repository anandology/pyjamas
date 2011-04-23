from django.db import models
from django.utils.encoding import smart_str

class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(max_length=255, null=False)
    def __str__(self):
        return smart_str(self.title)
