from RedditCrawler import RedditCrawler 
from GenerateArticle import GenerateArticle
from ArticleCommit import ArticleCommit
from Article import Article

import time

class Controller:
    def createArticle(self, url, min_amount, threshold):
        crawler = RedditCrawler()
        article = crawler.getArticle(url)

        gen = GenerateArticle()
        gen.generate(article, threshold)

        interface = ArticleCommit()
        interface.commit(article, min_amount)

    def daily_run(self, limit, min_amount, threshold):
        crawler = RedditCrawler()
        dailyTopURLs = crawler.getURLDailyTop(limit)

        for url in dailyTopURLs :
            self.createArticle(url, min_amount, threshold)

    def weekly_run(self, limit, min_amount, threshold):
        crawler = RedditCrawler()
        weeklyTopURLs = crawler.getURLWeeklyTop(limit)

        for url in weeklyTopURLs :
            self.createArticle(url, min_amount, threshold)

    def monthly_run(self, limit, min_amount, threshold):
        crawler = RedditCrawler()
        monthlyTopURLs = crawler.getURLMonthlyTop(limit)

        for url in monthlyTopURLs :
            self.createArticle(url, min_amount, threshold)

