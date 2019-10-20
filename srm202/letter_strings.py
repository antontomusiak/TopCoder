class LetterStrings:
	def sum(self, s):
		l = 0
		for i in range(len(s)):
			l += len(s[i]) - s[i].count('-')
		
		return l