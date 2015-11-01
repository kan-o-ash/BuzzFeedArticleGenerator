class GenerateArticle:

	def processTitle(self, article):
		return title

	def goodComment(self, item):

		return True

	def processComments(self, item):
		final_items = []

		for item in article.items:
			if goodComment(item):
				final_items.append(item)

		article.items = final_items
		

	def addGifs(self, article):
		pass

	def generate(self, article):
		processComments(article)

		addGifs(article)

		processTitle(article)

		return 