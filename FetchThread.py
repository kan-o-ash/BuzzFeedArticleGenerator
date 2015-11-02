import praw
from Article import Article
from Item import Item

class FetchThread(object):

	# Main method used to get thread details from Reddit
	def getArticle(self, url):
		sub = self.red_api.get_submission(url=url)

		title = sub.title
		url = url
		score = sub.score

		items = []
		for idx in range(len(sub.comments)-1):
			com = sub.comments[idx]
			item = Item(com.body, com.score)
			items.append(item)
		
		self.article = Article(title, url, score, items)

		return self.article

	def __init__(self):
		self.red_api = praw.Reddit('BuzzFeedBot')
		pass