class WordleKB:
	def __init__(self, display, xpos, ypos, width, height, the_word):
		self._key_pos = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
		#self._key_pos = ["ABCDEFGHIJ", "KLMNOPQRST", "UVWXYZ"]
		self._top_row_keys = [WordleTile(…) ]
		self._middle_row_keys = []
		self._bottom_row_keys = []
		self._keys = [[], [], []]
		self._correct_letters = []
		self._incorrect_letters = []
	
	def rasterize(self):
		# displays the KB on the screen
		pass
		
