from pymongo import MongoClient

class ArticleCommit(object):

    def __init__(self):
        client = MongoClient(host='127.0.0.1', port=3001)

        self.articles_collection = client.meteor.articles

    def qualityArticle(self, article):
        if len(article.items) > 10 :
            return True
        else :
        return False

    def commit(self, article):
        if not self.qualityArticle(article):
            return

        article_dict = article.__dict__

        self.articles_collection.insert_one(article_dict)
