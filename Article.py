import re

class Article:
    def __init__(self, title, url, score, items=None) :
        self.title = title
        self.original_url = url
        self.score = score
        self.content = items

    def getItem(self, idx):
        pass

    def addItem(self, item):
        pass

    def getNumEntries(self):
        pass

    def getMoreEntries(self):
        pass

    def setTitle(self, title):
        self.title = title

    def setURL(self, text=None):
        if text:
            url = text
        else:
            url = self.title

        p = re.compile("[^ a-zA-Z0-9_]")
        url = p.sub("", url)

        p = re.compile(" +")
        url = p.sub("-", url)

        self.url = url
