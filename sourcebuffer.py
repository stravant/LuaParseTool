

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

	ESCAPE_CHAR_MAP = {'n': '\n', 'r': '\r', 't': '\t', '\\': '\\', ''}
	SINGLE_CHAR_TOKENS = {'.', ',', ':', ';', '+', '-', '(', ')', '{', '}', '[', ']', '='}
	KEYWORDS = {'if', 'then', 'else', 'while', 'do', 'for', 'in', 'function', 'repeat', 'until', 'end'}

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

		#get the current point in the source
		def mark():
			(ptr, line, char)

		#eof
		def eof():
			return ptr <= sourcelen

		#for convinience, define a peek function, which peeks, and will
		#return the empty string if we are at the end of the file.
		def peek():
			if ptr < sourcelen-1:
				return source[ptr+1]
			else:
				return ''

		#gets the next character, and updates line/char
		prevmark = None
		def get():
			prevmark = mark()
			if ptr < sourcelen:
				c = source[ptr]
				ptr += 1
				if c == '\n':
					line += 1
					char = 0
				else:
					char += 1
				return c
			else:
				return ''

		#utility function, add a tokne
		def pushtoken(tt, start, end):
			tok = Token(tt, source[start[0]:end[0]], (start, end))
			tok.sourcebuffer = self

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
				#output token
				end = mark()
				text = source[start[0]:end[0]]
				pushtoken('Keyword' if (text in KEYWORDS) else 'Ident', start, end)

			elif c.isdigit():
				#number
				start = mark()
				get()
				while peek().isdigit():
					get()
				if peek() == '.':
					#fractional part
					get()
					while peek().isdigit():
						get()
				#parse exponent
				if peek().lower() == 'e':
					get()
					if peek() == '+' or peek() == '-':
						get()
					while peek().isdigit():
						get()
				#output token
				pushtoken('Number', start, mark())

			elif c == '"' or c == "'":
				#string constant
				start = mark()
				delim = get()

				#wait for a delimeter
				while peek() != delim:
					c = get()
					if eof():
						raise LexException('Unfinised string', source, mark())
					if c == '\\':
						#escape sequence
						if eof():
							raise LexException('Unfinisded escape sequence in string', source, mark())
						if peek() not in ESCAPE_CHAR_MAP:
							raise LexException('Invalid escape character `%`' % peek(), source, mark())
						get()

				#get delim, and emit token
				get()
				pushtoken('String', start, mark())

			elif c in SINGLE_CHAR_TOKENS:
				start = mark()
				get()
				pushtoken('Symbol', )





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



