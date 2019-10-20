class SafeBetting:
	def minRounds(self, a, b, c):
		bets_count = 0
		while b < c:
			b += b - a
			bets_count += 1
		
		return bets_count