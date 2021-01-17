from django.shortcuts import render
from .contentService import ContentService

# Create your views here.
def homepage_view(request):
    cs = ContentService()
    context = {
        'firstArticle': cs.first,
        'articleList': cs.articleList
    }
    return render(request, "home.html", context)