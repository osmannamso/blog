from django.db import models
import datetime
# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Topic(models.Model):
    name = models.CharField(max_length=30)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Type(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    clickIcon = models.CharField(max_length=200)

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
    seen = models.IntegerField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)