import urllib2, json

class GIFFY:

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
        print str(e)
        return ""
    return content

  def getTopKeyword(self, keywords):
    # print sorted(keywords, cmp=lambda x,y: x[1]>y[1])
    max = 0
    top = None
    for item in keywords:
      if item[1] > max:
        max = item[1]
        top = item[0]

    return top

  def findGIF(self, keywords):
    """ return gif_url matching keywords """
    top_keyword = self.getTopKeyword(keywords)
    url = "http://api.giphy.com/v1/gifs/search?q=%s&api_key=dc6zaTOxFJmzC" %top_keyword
    resp = json.loads(self.getResponse(url))

    return resp['data'][0]['images']['original']['url']


  def addGIF(self, item):
    # TO DO
    pass
