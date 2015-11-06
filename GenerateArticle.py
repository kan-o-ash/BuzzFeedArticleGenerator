from GifFinder import GifFinder

class GenerateArticle(object):

    def processTitle(self, article):
        return

    def goodComment(self, item):
        if item['gif_keywordCertainty'] > 0.15:
            return True
        else:
            return False

    def processComments(self, article):
        final_items = []

        for item in article.content:
            if self.goodComment(item):
                final_items.append(item)

        article.content = final_items
        

    def addGifs(self, article):
        gif = GifFinder()
        for idx, item in enumerate(article.content):
            gifData = gif.getGifDataForText(item['text'])
            item['gif_url'] = gifData['gifURL']
            item['gif_keyword'] = gifData['gifKeyword']
            item['gif_keywordCertainty'] = gifData['keywordCertainty']

    def generate(self, article):

        self.addGifs(article)

        self.processComments(article)

        self.processTitle(article)

        return
