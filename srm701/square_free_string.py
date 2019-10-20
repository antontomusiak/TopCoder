class SquareFreeString:
	def isSquareFree(self, s):
		n = len(s)
		for l in range(2, n+1, 2):
			for i in range(n - l + 1):
				sub = s[i:l+i]
				if sub[:l/2] == sub[l/2:]: return "not square-free"
		
		return "square-free"