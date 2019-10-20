class YahtzeeScore:
	def maxPoints(self, toss):
		max_points = 0
		for num in toss:
			max_points = max(max_points, (num * toss.count(num)))
		
		return max_points