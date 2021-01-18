from django.shortcuts import render
from .contentService import ContentService
from articles.models import Instrument

# Create your views here.
def homepage_view(request):
    cs = ContentService()
    instruments = Instrument.objects.all()
    instrumentList = []
    for i in instruments:
        instrumentList.append(i)
    context = {
        'firstArticle': cs.first,
        'articleList': cs.articleList,
        'instrumentList': instrumentList
    }
    return render(request, "home.html", context)