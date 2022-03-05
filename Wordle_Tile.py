import pygame

pygame.init()

class WordleTile:
	def __init__(self, ...):
		# Replace ... in the function argument with the correct variable 
		# names.
		# Initialize the following member variables:
		'''
		self._xpos
		self._ypos
		self._width
		self._height
		self._color
		self._text
		self._display  # This is the pygame display 
		'''

	def rasterize(self):
		# This method will draw the tile and the text (letter) using self._display
		pass

	@property.setter
	def text(self, the_text):
		self.text_ = the_text

	@property.setter
	def color(self, new_color):
		self._color = new_color

if __name__ == "__main__":
	window_height, window_width = 300, 500
	display = pygame.display.set_mode(window_height, window_width)

	# tile = WordleTile(display, ...)
	# tile.rasterize()
	pygame.display.update()
	