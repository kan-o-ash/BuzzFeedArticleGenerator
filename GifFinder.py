import urllib2, json
import indicoio
import operator
import giphypop

indicoio.config.api_key = '783b213a056b15affaef0fc6200cc4e2'
giffy_api_key = "dc6zaTOxFJmzC"

class GifFinder(object):
    def __init__(self):
        pass

    def getResponse(self, url):
        try:
            response = urllib2.urlopen(url)
            content = response.read()
        except urllib2.HTTPError, e:
            print "Error code: " + str(e)
            if e.getcode() == 500:
                content = e.read()
        else:
            return ""
        return content
  
    def getKeywords(self, text):
        return indicoio.keywords(text)

    def getTopKeyword(self, keywords):
        max = 0
        top = None
        for key in keywords.keys():
            if keywords[key] > max:
                max = keywords[key]
                top = key

        top_keyword = {}
        top_keyword['keyword'] = top
        top_keyword['certainty'] = max
        return top_keyword

    def findGIF(self, word):
        """ return gif_url matching keywords """
    
        g = giphypop.Giphy()
        g.api_key = giffy_api_key
     
        imgs = [x for x in g.search(term=word, limit=1)]
        if len(imgs):
            return imgs[0].media_url
        else:
            return 0 

    def getGifDataForText(self, text):
        # TO DO
        keywords = self.getKeywords(text)
        top_keyword = self.getTopKeyword(keywords)
        keyword = top_keyword['keyword']
        certainty = top_keyword['certainty']

        gifData = {}
        gifData['gifURL'] = self.findGIF(keyword)
        gifData['gifKeyword'] = keyword
        if gifData['gifURL'] == 0:
            gifData['keywordCertainty'] = 0
        else:
            gifData['keywordCertainty'] = certainty

        return gifData
