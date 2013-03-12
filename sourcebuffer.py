

class SourceBuffer:
	"""
	Source and Token storage.
	Token and source storage are tightly coupled, so that the source buffer may
	be mutated both at the text or token level, with the other being updated to
	match.
	"""

	def __init__(self):
		"""
		Constructor
		Initializes the buffer to an empty buffer, ready to have text parsed
		into it, or tokens / text appended to it.
		"""
		self._source = ""
		self._tokens = []
		pass

	def lex_from_source(self, source):
		"""
		Update the buffer to be for a given source string
		"""

		#init state
		sourcelen = len(source)
		self._source = source
		ptr = 0
		line = 1
		char = 0

		def mark():
			#get the current point in the source
			(ptr, line, char)

		def peek():
			#for convinience, define a peek function, which peeks, and will
			#return the empty string if we are at the end of the file.
			if ptr < sourcelen-1:
				return source[ptr+1]
			else:
				return ''

		prevmark = None
		def get():
			#gets the next character, and updates line/char
			prevmark = mark()
			if ptr < sourcelen:
				c = source[ptr]
				if c == '\n':
					line += 1
					char = 0
				else:
					char += 1
				return c
			else:
				return ''

		#main loop
		while ptr < sourcelen:
			#get main char
			c = peek()

			if c.isalpha():
				#identifier
				start = mark()
				get()
				while peek().isalnum():
					get()
				end = mark()




			elif c.isdigit():
				#number

			elif c == '"' or c == "'":
				#string constant


	def __len__(self):
		"""
		Length, defined as the number of tokens
		"""
		return len(self._tokens)

	def __getitem__(self, n):
		"""
		Get the n'th token from the buffer
		"""
		assert(0 <= n < len(self))
		return self._tokens[n]



