class FixedPointTheorem:
	def cycleRange(self, R):
		x = 0.25
		min_x, max_x = 10, 0
		n = 200000
		m = n + 1000
		for i in range(n):
			x = R * x * (1 -x)
		
		for i in range(n, m):
			x = R * x * (1 - x)
			min_x = min(min_x, x)
			max_x = max(max_x, x)
		
		return max_x - min_x