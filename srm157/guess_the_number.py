class GuessTheNumber:
	def noGuesses(self, upper, answer):
		low = 1
		count = 1
		while answer != (upper + low)/2:
			if answer > (upper + low) / 2:
				low = (upper + low) / 2 + 1
				count += 1
			else: 
				upper = (upper + low) / 2 - 1
				count += 1
		
		return count