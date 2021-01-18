from django.contrib import admin

# Register your models here.
from .models import Article, Tag, Instrument, Comment

admin.site.register(Tag)
admin.site.register(Instrument)
admin.site.register(Article)
admin.site.register(Comment)