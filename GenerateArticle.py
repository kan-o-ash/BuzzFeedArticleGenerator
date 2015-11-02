class GenerateArticle(object):

	def processTitle(self, article):
		return

	def goodComment(self, item):
		return True

	def processComments(self, article):
		final_items = []

		for item in article.items:
			if self.goodComment(item):
				final_items.append(item)

		article.items = final_items
		

	def addGifs(self, article):
		for idx, item in enumerate(Article.items):
			GIFFY.addGIF(item)
			Article.items[idx] = item


	def generate(self, article):
		self.processComments(article)

		# addGifs(article)

		self.processTitle(article)

		return
