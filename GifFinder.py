import urllib2, json
import indicoio
import operator
indicoio.config.api_key = '783b213a056b15affaef0fc6200cc4e2'


class GifFinder(object):
  def __init__(self):
    pass

  def getResponse(self, url):
    try:
      response = urllib2.urlopen(url)
      content = response.read()
    except urllib2.HTTPError, e:
      if e.getcode() == 500:
        content = e.read()
      else:
        print "Error code: " + str(e)
        return ""
    return content
  
  def getKeywords(self, text):
    keywords = {}
    keywords = indicoio.keywords(text)
    # sorted_keywords = sorted(keywords.items(), key=operator.itemgetter(0))
    return keywords

  def getTopKeyword(self, keywords):
    max = 0
    top = None
    for key in keywords.keys():
      if keywords[key] > max:
        max = keywords[key]
        top = key

    return top

  def findGIF(self, word):
    """ return gif_url matching keywords """
    giffy_api_key = "dc6zaTOxFJmzC"
    url = "http://api.giphy.com/v1/gifs/search?q=%s&api_key=%s" %(word, giffy_api_key)
    resp = json.loads(self.getResponse(url))

    # BAD FORM
    return resp['data'][0]['images']['original']['url']


  def getGIF(self, text):
    # TO DO
    keywords = self.getKeywords(text)
    top_word = self.getTopKeyword(keywords)

    return self.findGIF(top_word) 


