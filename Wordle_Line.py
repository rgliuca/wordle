
class WordleLine:
	LETTERS = 5

	def __init__(self, xpos, ypos, the_word, text=""):
		# what would you do here? 
		self._x = xpos
		self._word = the_word
		self._tiles = [] # list of WordleTile, also setup each tile position
		pass

	@property
	def text(self):
		return self._text

	@text.setter
	def text(self, new_text):
		if len(new_text) != __class__.LETTERS:
			# don't implement this... 
			pass
		self._text = new_text
		# you need to do something here!
		# change the color of each tile based on the match with the word

	def rasterize(self):
		# do something with each WordleTile 
		pass


	

	
	