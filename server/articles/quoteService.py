import json
from django.contrib.staticfiles.storage import staticfiles_storage


class Price:
    currentPrice = 0
    openPrice = 0
    change = 0
    changePercent = 0


class QuoteService:
    def __init__(self):
        self.quotes = {}
        self.readQuotes()

    def readQuotes(self):
        with open(staticfiles_storage.path('quotes_api.json'), encoding="utf-8") as f:
            data = json.load(f)

        for quote in data:
            p = Price()
            p.openPrice = quote['OpenPrice']['Amount']
            p.currentPrice = quote['CurrentPrice']['Amount']
            p.change = quote['Change']['Amount']
            p.changePercent = quote['PercentChange']['Value']
            self.quotes[quote['InstrumentId']] = p

    def getQuote(self, instrumentId):
        return self.quotes[instrumentId]