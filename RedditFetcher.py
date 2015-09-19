import praw

class RedditFetcher:
  
  def fetchComments(self, thread_url):
    r = praw.Reddit('test')
    submission = r.get_submission(url=thread_url)
    self.title = submission.title
    return submission.comments

  def getTopComments(self, thread_url, limit=30):
    comments = self.fetchComments(thread_url)
    comments = comments[:len(comments)-1]

    comments_sorted = sorted(comments, key=lambda object1: object1.score, reverse=True)

    return comments_sorted