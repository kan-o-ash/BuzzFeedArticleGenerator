from RedditFetcher import RedditFetcher

myobj = RedditFetcher()
myurl = "https://www.reddit.com/r/AskReddit/comments/2sbi17/what_do_insanely_poor_people_buy_that_ordinary/"
coms = myobj.getTopComments(myurl)

for com in coms:
  print com.score, com

print vars(com)