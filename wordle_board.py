class WordleBoard:
	# The board knows the_word, the board can take a guess from the player, and the board would know when all the lines have been exhausted!
	def __init__(self, display, xpos, ypos, the_word):
		self._the_word = the_word
		self._wordle_lines = [WordleLine(xpos, ypos + i*….  , the_word, "")   for i in range(6)]
		
	
	def set_line(self, new_word):
		# only checks if you have <= 5 letters
		# sets the current Wordle_Line with the "new_word"
		pass
	
	def submit_word(self):
		# Checks if the current wordle_line text is a valid 5 letter word
		# if it's a valid word, then submits the word to the current wordle_line
		# else display error messages:
		# 	"Not Enough Letters"
		# 	"Not in Word List"
		
	def num_tries_left():
		# returns the num of empty wordle lines
		pass
	
	def rasterize():
		# displays the board
		pass
