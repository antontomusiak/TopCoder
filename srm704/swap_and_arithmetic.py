class SwapAndArithmetic:
	def able(self, x):
		if len(set(x)) == 1: return "Possible"
		x_s = sorted(list(x))
		for i in range(1, len(x)-1):
			if (x_s[i] - x_s[i-1]) != (x_s[i+1] - x_s[i]): return "Impossible"
		
		return "Possible"