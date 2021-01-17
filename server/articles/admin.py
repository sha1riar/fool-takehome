from django.contrib import admin

# Register your models here.
from .models import Article, Tag, Instrument

admin.site.register(Tag)
admin.site.register(Instrument)
admin.site.register(Article)