class ShortInputException(Exception):
	"""A User defined exception class."""
	def __init__(self, length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = raw_input('Enter Something -----> ')
	if len(text) < 3:
		raise ShortInputException(len(text),3)
except EOFError:
	print "Why did you do an EOF on me? "
except ShortInputException as ex:
	print "ShortInputException: The input was {0} long, expected atleast {1}".format(ex.length,ex.atleast)
else:
	print "No Exception was raised."