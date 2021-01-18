import json
import random
from django.contrib.staticfiles.storage import staticfiles_storage
from articles.models import Article, Instrument, Tag
from django.utils.text import slugify

class ContentService:
    def __init__(self):
        self.first = ''
        self.articleList = []
        self.readContent()
        self.getArticles()

    def getArticles(self):
        articles = []
        for article in Article.objects.all():
            if not article.uuid == self.first.uuid:
                articles.append(article)
        self.articleList = random.sample(articles, 3)


    def readContent(self):
        with open(staticfiles_storage.path('content_api.json'), encoding="utf-8") as f:
            data = json.load(f)

        for article in data['results']:
            if not Article.objects.filter(uuid=article['uuid']).exists():
                newArticle = Article()
                newArticle.authorByLine=article['byline']
                newArticle.body = article['body']
                newArticle.publishDate = article['publish_at'].split('T')[0]
                newArticle.headline = article['headline']
                newArticle.promo = article['promo']
                newArticle.disclosure = article['disclosure']
                newArticle.uuid = article['uuid']
                newArticle.slug = slugify(article['headline'])

                for img in article['images']:
                    if img['featured']:
                        newArticle.featuredImage = img['url']

                for ins in article['instruments']:
                    newArticle.save()
                    if Instrument.objects.filter(instrumentId=ins['instrument_id']).exists():
                        newArticle.relatedInstruments.add(Instrument.objects.get(instrumentId=ins['instrument_id']))
                    else:
                        i = Instrument()
                        i.instrumentId = ins['instrument_id']
                        i.companyName = ins['company_name']
                        i.symbol = ins['symbol']
                        i.exchange = ins['exchange']
                        i.save()
                        newArticle.relatedInstruments.add(i)

                for tag in article['tags']:
                    newArticle.save()
                    if Tag.objects.filter(uuid=tag['uuid']).exists():
                        newArticle.tags.add(Tag.objects.get(uuid=tag['uuid']))
                    else:
                        t = Tag()
                        t.uuid = tag['uuid']
                        t.tagName = tag['name']
                        t.tagSlug = tag['slug']
                        t.tagTypeName = tag['tag_type']['name']
                        t.tagTypeSlug = tag['tag_type']['slug']
                        t.save()
                        newArticle.tags.add(t)
                newArticle.save()
            for tag in article['tags']:
                if self.first == '' and tag['slug']=='10-promise':
                    self.first = Article.objects.get(uuid=article['uuid'])