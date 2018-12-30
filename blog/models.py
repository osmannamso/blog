from django.db import models
from django.db.models import F

import datetime
# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200, default='')
    click_icon = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.name)

class Topic(models.Model):
    name = models.CharField(max_length=30)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Article(models.Model):
    title = models.CharField(max_length=50)
    description =  models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=datetime.datetime)
    author_id = models.IntegerField()
    img_url = models.CharField(max_length=200)
    helpful = models.BooleanField(default=False)
    seen = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def AddSeen(self, id):
        self.objects.filter(id=id).update(seen=F('seen') + 1)

    def __str__(self):
        return str(self.title)