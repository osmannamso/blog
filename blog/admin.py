from django.contrib import admin
from .models import Theme, Topic, Article
# Register your models here.
admin.site.register(Topic)
admin.site.register(Theme)
admin.site.register(Article)