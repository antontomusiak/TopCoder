class MagicSquare:
	def missing(self, square):
		mn = 0
		ind = square.index(-1)
		if ind < 3: mn = sum(square[3:6]) - sum(square[0:3]) - 1
		elif ind >= 3 and ind < 6: mn = sum(square[0:3]) - sum(square[3:6]) - 1  
		else: mn = sum(square[0:3]) - sum(square[6:]) - 1
		return mn