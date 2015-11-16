from RedditCrawler import RedditCrawler 
from GenerateArticle import GenerateArticle
from ArticleCommit import ArticleCommit
from Article import Article

import time

class Controller:
    def createArticle(self, url):
        crawler = RedditCrawler()
        article = crawler.getArticle(url)

        gen = GenerateArticle()
        gen.generate(article)

        interface = ArticleCommit()
        interface.commit(article)


    def run(self):
        crawler = RedditCrawler()
        weeklyTopURLs = crawler.getURLWeeklyTop(10)

        for url in weeklyTopURLs :
            self.createArticle(url)

mycontroller = Controller()
mycontroller.run()
