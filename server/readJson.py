import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
import django
django.setup()
from articles.models import Article


def readContent():
    articles = []
    with open('content_api.json') as f:
        data = json.load(f)
    for article in data['results']:
        articleToSave = Article()
        articleToSave.authorByLine = article['byline']
        articleToSave.body = article['body']
        articleToSave.publishDate = article['publish_at'].split('T')[0]
        articleToSave.headline = article['headline']
        articleToSave.promo = article['promo']
        articleToSave.relatedInstruments = article['instruments']
        articleToSave.disclosure = article['disclosure']
        articleToSave.tags = article['tags']
        articleToSave.save()
    print('test')


if __name__ == '__main__':
    readContent()
#python manage.py shell < script.py
