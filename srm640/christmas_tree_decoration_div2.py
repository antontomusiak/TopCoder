class ChristmasTreeDecorationDiv2:
	def solve(self, col, x, y):
		res = 0
		for i in range(len(x)):
			if col[x[i]-1] != col[y[i]-1]: res += 1
		
		return res