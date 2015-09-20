from RedditFetcher import RedditFetcher

myobj = RedditFetcher()
myurl = "https://www.reddit.com/r/AskReddit/comments/3ljl8s/if_money_was_no_object_what_would_you_do_all_day/"
#myurl = "https://www.reddit.com/r/AskReddit/comments/2sbi17/what_do_insanely_poor_people_buy_that_ordinary/"
coms = myobj.getTopComments(myurl)

for com in coms:
  if myobj.isQualityPost(com, 300, 500):
    print com.score, com.body

#title = myobj.generateTitle(myurl)
#print title

#myobj.analyzeTitle("What do you think when you hear Australia?")

print vars(com)
