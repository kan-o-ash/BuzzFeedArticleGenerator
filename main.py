from meteorInterface import meteorInterface
from RedditFetcher import RedditFetcher

'''interface_obj = meteorInterface()

title = "16 best euphemisms for sex that you don't know"
content = [
  {'body': """Coffee.
Me and a girl I dated always agreed that sex in the morning was better than coffee so thats what we started calling it. And occasionally when we were leaving outings with friends one of us would ask "Do we need to stop and get coffee filters?" And everyone just gave us funny looks.
""", 'gif_url': 'https://media.giphy.com/media/HEgG7AcV99tyE/giphy.gif'}
  ]

print interface_obj.insertByContent(title, content)
'''
interface_obj = meteorInterface()

myobj = RedditFetcher()
submissions = myobj.getThreads(1)

for sub in submissions:
    content = []
    comments = myobj.gatherAllEntries(10, sub.url)
    for key in comments:
        #print str(comments[key].body)
        content.append({'body': comments[key].body, 'gif_url':'', 'keywords': myobj.getKeywords(comments[key].body), 'score': comments[key].score})
    interface_obj.insertByContent(sub.title, content)
 
