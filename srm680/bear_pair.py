class BearPair:
	def bigDistance(self, s):
		d = -1
		for i in range(len(s)-1):
			for j in range(len(s)-1, 0, -1):
				if s[i] != s[j]: d = max(d, j-i)
				
		return d 