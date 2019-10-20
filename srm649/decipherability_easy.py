class DecipherabilityEasy:
	def check(self, s, t):
		#if len(s) - 1 != len(t): return 'Impossible'
		for i in range(len(s)):
			tmp = list(s)
			tmp.pop(i)
			if ''.join(tmp) == t: return 'Possible'
		
		return 'Impossible'