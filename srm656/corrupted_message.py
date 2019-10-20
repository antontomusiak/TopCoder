class CorruptedMessage:
	def reconstructMessage(self, s, k):
		abc = 'abcdefghigklmnopqrstuvwxyz'
		for letter in s:
			if len(s) - s.count(letter) == k: return letter * len(s)
		
		for letter in abc:
			if letter not in s: return letter * len(s)