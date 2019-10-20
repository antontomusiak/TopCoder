class HalvingEasy:
	def count(self, S, T):
		count = 0
		for i in S:
			while i >= T:
				if i == T: count = count + 1
				i = i//2
		
		return count