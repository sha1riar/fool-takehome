from django.db import models

# Create your models here.


class Article(models.Model):
    authorByLine = models.CharField(max_length=30)
    body = models.TextField()
    publishDate = models.DateField()
    headline = models.CharField(max_length=100)
    promo = models.CharField(max_length=100)
    relatedInstruments = models.JSONField()
    disclosure = models.TextField()
    tags = models.JSONField()
