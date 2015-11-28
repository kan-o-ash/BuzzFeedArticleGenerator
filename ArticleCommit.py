from pymongo import MongoClient

class ArticleCommit(object):

    def __init__(self):
        client = MongoClient(host='127.0.0.1', port=3001)

        self.articles_collection = client.meteor.articles

    def qualityArticle(self, article, min_amount):
        if len(article.content) > min_amount :
            return True
        else :
            return False

    def commit(self, article, min_amount):
        if not self.qualityArticle(article, min_amount):
            return

        article_dict = article.__dict__

        self.articles_collection.insert_one(article_dict)
