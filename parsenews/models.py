from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.TextField()
    link = models.TextField()
    nid = models.TextField()
    published = models.TextField()
    summary = models.TextField()

 
    def __str__(self):
        return self.title

