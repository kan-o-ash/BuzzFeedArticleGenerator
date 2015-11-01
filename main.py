from meteorInterface import meteorInterface
from RedditFetcher import RedditFetcher
from GIFFY import GIFFY

interface_obj = meteorInterface()

myobj = RedditFetcher()
submissions = myobj.getThreads(30)

for sub in submissions:
  content = []
  comments = myobj.gatherAllEntries(10, sub.url)
  for key in comments:
    #print str(comments[key].body)
    body = comments[key].body
    keywords = myobj.getKeywords(comments[key].body)
    
    gif_obj = GIFFY()
    gif_url = gif_obj.findGIF(keywords)
    content.append({'body': body,
                    'gif_url': gif_url,
                    'keywords': keywords,
                    'score': comments[key].score
                  })

  interface_obj.insertByContent(sub.title, content)

