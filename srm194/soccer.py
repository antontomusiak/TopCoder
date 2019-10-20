class Soccer:
	def maxPoints(self, wins, ties):
		res = 0
		for i in range(len(wins)):
			res = max(res, (wins[i] * 3 + ties[i]))
		
		return res