class MakingPairs:
	def get(self, card):
		count = 0
		for i in range(len(card)):
			count += card[i] / 2
		
		return count