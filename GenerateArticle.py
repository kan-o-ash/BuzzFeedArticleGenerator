from GifFinder import GifFinder
import re

class GenerateArticle(object):

    def processTitle(self, article):
        return

    def goodComment(self, item):
            return item.has_key('gif_url') and item['gif_keywordCertainty'] > 0.20

    def removeEditText(self, item):
        if item['edited']:
            cleaned = re.sub(r'edit:.*', "", item['text'], flags=re.IGNORECASE)
            item['text'] = cleaned
        return item

    def processItems(self, article):
        final_items = []

        for item in article.content:
            item = self.removeEditText(item)
            if self.goodComment(item):
                final_items.append(item)

        article.content = final_items

    def addGifs(self, article):
        gif = GifFinder()
        for idx, item in enumerate(article.content):
            gifData = gif.getGifDataForText(item['text'])

            if gifData:
                item['gif_url'] = gifData['gifURL']
                item['gif_keyword'] = gifData['gifKeyword']
                item['gif_keywordCertainty'] = gifData['keywordCertainty']

    def generate(self, article):
        self.addGifs(article)
        self.processItems(article)
        article.setURL()
        self.processTitle(article)
