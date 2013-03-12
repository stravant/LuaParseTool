
class LexException(Exception):
	def __init__(self, err, source, location):
		self.error = err
		self.source = source
		self.location = location