class EightRooks:
	def isCorrect(self, board):
		col = []
		row = []
		for i in range(8):
			for j in range(8):
				if board[i][j] == 'R':  
					if i in row or j in col: return 'Incorrect'
					else:
						col.append(j)
						row.append(i)
			
		if len(col) == 8: return 'Correct'
		return 'Incorrect'