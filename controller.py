from FetchThread import FetchThread
from GenerateArticle import GenerateArticle
from ArticleCommit import ArticleCommit
from Article import Article

import time

class Controller:
    def createArticle(self, url):
        fetcher = FetchThread()
        article = fetcher.getArticle(url)

        gen = GenerateArticle()
        gen.generate(article)

        interface = ArticleCommit()
        interface.commit(article)


    def run(self):
        url = "https://www.reddit.com/r/AskReddit/comments/3qynmv/you_gain_the_ability_to_put_a_30s_waiting_period/"
        
        self.createArticle(url)

mycontroller = Controller()
mycontroller.run()
