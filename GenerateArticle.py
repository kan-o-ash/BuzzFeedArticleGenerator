from GifFinder import GifFinder
import re

class GenerateArticle(object):

    def processTitle(self, article):
        return

    def goodComment(self, item, threshold):
            return item.has_key('gif_url') and item['gif_keywordCertainty'] > threshold

    def removeEditText(self, item):
        if item['edited']:
            cleaned = re.sub(r'edit:.*', "", item['text'], flags=re.IGNORECASE)
            item['text'] = cleaned
        return item

    def processItems(self, article, threshold):
        final_items = []

        for item in article.content:
            item = self.removeEditText(item)
            if self.goodComment(item, threshold):
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

    def generate(self, article, threshold):
        self.addGifs(article)
        self.processItems(article, threshold)
        article.setURL()
        self.processTitle(article)
