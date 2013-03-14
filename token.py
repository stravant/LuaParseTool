
class Token:
	TOKEN_TYPES = ['Ident', 'Number', 'String', 'Symbol', 'Keyword']

	def __init__(self, tt, data, loc):
		"""
		Loc: (start, end), where start, end = (ptr, line, char)
		"""
		assert(tt in Token.TOKEN_TYPES)
		self.ttype = tt
		self.data = data
		self.loc = loc
		self.sourcebuffer = None

	def append(self, tokenlist):
		"""
		Add a token after this token in it's sourceBuffer
		"""
		pass

	def prepend(self, tokenlist):
		"""
		Add a token before this token in it's SourceBuffer
		"""
		pass

	def append_text(self, text):
		pass

	def prepend_text(self, text):
		pass



	