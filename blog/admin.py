from django.contrib import admin
from .models import Theme, Topic, Article, Type
# Register your models here.
admin.site.register(Topic)
admin.site.register(Theme)
admin.site.register(Article)
admin.site.register(Type)