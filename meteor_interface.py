from pymongo import MongoClient

class meteorInterface:
  """ Python interface to Meteor's mongoDB database """

  def __init__(self):
    client = MongoClient(host='127.0.0.1', port=3001)

    db = client.meteor
    self.art_col = db.articles

  def createContentObj(self, arr_captions, arr_gifs):
    content = []
    for cap, gif in arr_captions, arr_gifs:
      content.append({'body': cap, 'gif_url': gif})
    return content

  def insertByContent(self, title, content):
    """ content is an array of {caption,gif_url} objects """
    self.art_col.insert({
        "title": title,
        "content": content
      })
  
  def insertByArray(self, title, arr_captions, arr_gifs):
    content = createContentObj(arr_captions, arr_gifs)

    insertByContent(title, content)

