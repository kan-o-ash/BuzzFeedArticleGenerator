import praw
from Article import Article

class FetchThread(object):

    # Main method used to get thread details from Reddit
    def getArticle(self, url):
        sub = self.red_api.get_submission(url=url)

        items = []
        for idx in range(len(sub.comments)-1):
            com = sub.comments[idx]
            item = {
                'text':  com.body,
                'score': com.score
            }
            items.append(item)
        
        article = Article(sub.title, url, sub.score, items)

        return article

    def __init__(self):
        self.red_api = praw.Reddit('BuzzFeedBot')
        pass
