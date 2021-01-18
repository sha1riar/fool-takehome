from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Instrument
from .quoteService import QuoteService
from .forms import CommentForm

# Create your views here.
def article_full_view(request, date, slug):
    object = Article.objects.get(publishDate=date, slug=slug)
    stocks = getStocksDetail(object.relatedInstruments.all())

    if request.method == 'POST':
        commentForm = CommentForm(data=request.POST)
        if commentForm.is_valid():
            newComment = commentForm.save(commit=False)
            newComment.article = object
            newComment.save()
    else:
        commentForm = CommentForm()

    context = {
        'authorByLine': object.authorByLine,
        'body': object.body,
        'publishDate': object.publishDate,
        'headline': object.headline,
        'promo': object.headline,
        'disclosure': object.disclosure,
        'relatedStocks': stocks,
        'form': commentForm,
        'comments': object.comments.all()
    }

    return render(request, "article.html", context)

def article_list_View(request, instrumentId):
    i = Instrument.objects.get(instrumentId=instrumentId)
    articleQ = Article.objects.filter(relatedInstruments=i)
    articleList =[]
    for article in articleQ:
        articleList.append(article)
    context = {
        'articleList': articleList
    }

    return render(request, "article_list.html", context)

def getStocksDetail(relatedInstruments):
    qs = QuoteService()
    stocks=[]
    for stock in relatedInstruments:
        stockPrice = qs.getQuote(stock.instrumentId)
        stock.currentPrice = stockPrice.currentPrice
        stock.openPrice = stockPrice.openPrice
        stock.change = stockPrice.change
        stock.changePercent = round(stockPrice.changePercent,2)
        stocks.append(stock)
    return stocks