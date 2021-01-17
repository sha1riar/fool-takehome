from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from .quoteService import QuoteService

# Create your views here.
def article_full_view(request, date, slug):
    object = Article.objects.get(publishDate=date, slug=slug)

    qs = QuoteService()
    stocks=[]
    for stock in object.relatedInstruments.all():
        stockPrice = qs.getQuote(stock.instrumentId)
        stock.currentPrice = stockPrice.currentPrice
        stock.openPrice = stockPrice.openPrice
        stock.change = stockPrice.change
        stock.changePercent = round(stockPrice.changePercent,2)
        stocks.append(stock)
    context = {
        'authorByLine': object.authorByLine,
        'body': object.body,
        'publishDate': object.publishDate,
        'headline': object.headline,
        'promo': object.headline,
        'disclosure': object.disclosure,
        'relatedStocks': stocks
    }

    return render(request, "article.html", context)
