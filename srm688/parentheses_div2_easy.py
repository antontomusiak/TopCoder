class ParenthesesDiv2Easy:
	def getDepth(self, s):
		res, counter = 0, 0
		for ch in s:
			if ch == '(': counter +=1
			else: counter -= 1
			res = max(res, counter)
				
	
		return res