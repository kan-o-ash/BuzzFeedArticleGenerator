import praw
import requests
import json
import re
from collections import OrderedDict
import indicoio
import operator
indicoio.config.api_key = '783b213a056b15affaef0fc6200cc4e2'

class RedditFetcher:
  def getThreads(self, numThreads):
    r = praw.Reddit('test')
    subreddit = r.get_subreddit('askreddit')
    return subreddit.get_hot(limit=numThreads)
  
  def fetchComments(self, thread_url):
    r = praw.Reddit('test')
    submission = r.get_submission(url=thread_url)
    self.title = submission.title
    return submission.comments

  def getTopComments(self, thread_url, limit):
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
    notTooLong = len(comment.body) < maxCommentLength
    isPopularPost = comment.score > minScore

    return notTooLong & isPopularPost

  def gatherAllEntries(self, totalEntries, myUrl):
    entries = {}
    coms =  self.getTopComments(myUrl, 50)

    #initial threshold for choice
    minScore = 2000
    maxLength = 50

    while len(entries) < totalEntries:
        for com in coms:
            if len(entries) > totalEntries:
                break
            if (self.isQualityPost(com, maxLength, minScore) & (com.name not in entries)):
                entries[com.name] = com
        if ((minScore < 0) & (maxLength > 505)):
            break
        minScore -= 250
        maxLength += 50
    return entries

  def getKeywords(self, text):
	keywords = {}
	keywords = indicoio.keywords(text)
	sorted_keywords = sorted(keywords.items(), key=operator.itemgetter(0))
	return sorted_keywords

	
