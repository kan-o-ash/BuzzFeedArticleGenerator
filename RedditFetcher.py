import praw
import requests
import json
import re

class RedditFetcher:
  
  def fetchComments(self, thread_url):
    r = praw.Reddit('test')
    submission = r.get_submission(url=thread_url)
    self.title = submission.title
    return submission.comments

  def getTopComments(self, thread_url, limit=10):
    comments = self.fetchComments(thread_url)
    comments = comments[:limit if len(comments) > limit else len(comments)-1]

    comments_sorted = sorted(comments, key=lambda object1: object1.score, reverse=True)

    return comments_sorted
  
  def generateTitle(self, thread_url):
    r = praw.Reddit('test')
    submission = r.get_submission(url=thread_url)
    title = submission.title
    return title

  def analyzeTitle(self, text):
    url = "https://services.open.xerox.com/bus/op/fst-nlp-tools/PartOfSpeechTaggingString?inputtext=text&language=text"
    # data = {'inputtext': text, 'language': 'text'}
    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # r = requests.post(url, data=json.dumps(data), headers=headers)
    r = requests.get(url)
    print vars(r)

  def isQualityPost(self, comment, maxCommentLength, minScore):
    #Algorithm to determine if a post is good enough to use
    return ((len(comment.body) < maxCommentLength) & (comment.score > minScore)) 

#TODO:Create list entries by decreasing constraints, until enough entries are chosen
