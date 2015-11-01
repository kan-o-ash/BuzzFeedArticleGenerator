
from FetchThread import FetchThread
from GenerateArticle import GenerateArticle
from CommitArticle import CommitArticle
from Article import Article


class Controller:
	def run(self):
		fetcher = FetchThread()
		article = fetcher.getArticle("https://www.reddit.com/r/AskReddit/comments/3qynmv/you_gain_the_ability_to_put_a_30s_waiting_period/")

		gen = GenerateArticle()
		gen.generate(article)

		print vars(article)

mycontroller = Controller()
mycontroller.run()