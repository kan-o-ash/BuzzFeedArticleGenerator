class CommitArticle(object):

	def qualityArticle(self, article):

		return True

	def process(self, article):
		if not qualityArticle(article):
			return

		MeteorInterface.commit(article)