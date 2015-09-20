from RedditFetcher import RedditFetcher

myobj = RedditFetcher()
myurl = "https://www.reddit.com/r/AskReddit/comments/3hpxbx/what_is_cool_to_be_good_at_yet_uncool_to_be/"
#myurl = "https://www.reddit.com/r/AskReddit/comments/3ljl8s/if_money_was_no_object_what_would_you_do_all_day/"
#myurl = "https://www.reddit.com/r/AskReddit/comments/2sbi17/what_do_insanely_poor_people_buy_that_ordinary/"
#coms = myobj.getTopComments(myurl, 10)
#for com in coms:
#  if myobj.isQualityPost(com, 300, 500):
#    print com.score, com.body

#title = myobj.generateTitle(myurl)
#print title

#myobj.analyzeTitle("What do you think when you hear Australia?")

entries = myobj.gatherAllEntries(10, myurl)

for key in entries:
    print entries[key].score, entries[key].body
#print vars(com)
