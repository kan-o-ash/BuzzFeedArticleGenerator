import praw
from Article import Article

class RedditCrawler(object):

    # Main method used to get thread details from Reddit
    def getArticle(self, url):
        sub = self.red_api.get_submission(url=url, comment_sort='top')

        items = []
        for idx in range(len(sub.comments)-1):
            com = sub.comments[idx]
            item = {
                'text':  com.body,
                'score': com.score,
                'edited': com.edited
            }
            items.append(item)
        
        article = Article(sub.title, url, sub.score, items)

        return article

    def getURLDailyTop(self, count):
        submissions = self.red_api.get_subreddit('askreddit').get_top_from_day(limit=count)
        return [x.url for x in submissions]
    
    def getURLWeeklyTop(self, count):
        submissions = self.red_api.get_subreddit('askreddit').get_top_from_week(limit=count)
        return [x.url for x in submissions]

    def getURLMonthlyTop(self, count):
        submissions = self.red_api.get_subreddit('askreddit').get_top_from_month(limit=count)
        return [x.url for x in submissions]

    def __init__(self):
        self.red_api = praw.Reddit('BuzzFeedBot')
        pass
