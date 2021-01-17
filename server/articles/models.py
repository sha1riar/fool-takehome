from django.db import models

# Create your models here.

class Tag(models.Model):
    uuid = models.UUIDField()
    tagName = models.CharField(max_length=40)
    tagSlug = models.CharField(max_length=40)
    tagTypeName = models.CharField(max_length=40)
    tagTypeSlug = models.CharField(max_length=40)


class Instrument(models.Model):
    instrumentId = models.IntegerField()
    companyName = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    exchange = models.CharField(max_length=50)
    openPrice = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    currentPrice = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    change = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    changePercent = models.DecimalField(decimal_places=2, max_digits=10, null=True)


class Article(models.Model):
    uuid = models.UUIDField()
    authorByLine = models.CharField(max_length=30)
    body = models.TextField()
    publishDate = models.DateField()
    headline = models.CharField(max_length=100)
    promo = models.CharField(max_length=100)
    relatedInstruments = models.ManyToManyField(Instrument)
    disclosure = models.TextField()
    tags = models.ManyToManyField(Tag)
    featuredImage = models.URLField()
    slug = models.SlugField()