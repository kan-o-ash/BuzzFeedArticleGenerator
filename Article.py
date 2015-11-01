
class Article:
	def __init__(self, title, url, score, items=None) :
		self.title = title
		self.original_url = url
		self.score = score
		self.items = items or []

	def getItem(self, idx):
		pass

	def addItem(self, item):
		pass

	def getNumEntries(self):
		pass

	def getMoreEntries(self):
		pass

