class WordleBoard:
	# The board knows the_word, the board can take a guess from the player, and the board would know when all the lines have been exhausted!
	def __init__(self, xpos, ypos, the_word):
		self._the_word = the_word
		self._wordle_lines = [WordleLine(xpos, ypos + i*….  , the_word, "")   for i in range(6)]
	
	def try_word(self, new_word):
		# return True/False if the word is correct
		pass
		
	def num_tries_left():
		# returns the num of empty wordle lines
		pass