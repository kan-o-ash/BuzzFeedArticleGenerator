class Item:
	
	def __init__(self, text, score=None, gif_url="", original_url=""):
		self.score = score
		self.text = text
		self.gif_url = gif_url or ""
		self.original_url = original_url or ""

