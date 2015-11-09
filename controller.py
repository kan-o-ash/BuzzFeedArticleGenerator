from FetchThread import FetchThread
from GenerateArticle import GenerateArticle
from ArticleCommit import ArticleCommit
from Article import Article

import time

class Controller:
    def createArticle(self, url):
        fetcher = FetchThread()
        article = fetcher.getArticle(url)

        gen = GenerateArticle()
        gen.generate(article)

        interface = ArticleCommit()
        interface.commit(article)


    def run(self):
        """
        url = "https://www.reddit.com/r/AskReddit/comments/3qv3dy/whats_only_fun_the_first_time/"
        self.createArticle(url)
        url = "https://www.reddit.com/r/AskReddit/comments/3r2siv/what_was_your_biggest_shit_my_parents_were_right/"
        self.createArticle(url)
        url = "https://www.reddit.com/r/AskReddit/comments/3rmbnh/what_was_the_best_thing_one_person_ruined_for_the/"
        self.createArticle(url)
        url = "https://www.reddit.com/r/AskReddit/comments/3rli7o/what_is_a_completely_ridiculous_fact_that_any/"
        self.createArticle(url)
        url = "https://www.reddit.com/r/AskReddit/comments/3qraot/what_requires_a_lot_of_skill_to_master_yet_still/"
        self.createArticle(url)
        """
        url = "https://www.reddit.com/r/AskReddit/comments/3s0xv8/whats_your_tell_when_youve_had_too_much_alcohol/"
        self.createArticle(url)

mycontroller = Controller()
mycontroller.run()
