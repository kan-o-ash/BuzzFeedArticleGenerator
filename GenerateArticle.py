from GifFinder import GifFinder

class GenerateArticle(object):

    def processTitle(self, article):
        return

    def goodComment(self, item):
        return True

    def processComments(self, article):
        final_items = []

        for item in article.content:
            if self.goodComment(item):
                final_items.append(item)

        article.content = final_items
        

    def addGifs(self, article):
        gif = GifFinder()
        for idx, item in enumerate(article.content):
            item['gif_url'] = gif.getGifForText(item['text'])

    def generate(self, article):
        self.processComments(article)

        self.addGifs(article)

        self.processTitle(article)

        return
