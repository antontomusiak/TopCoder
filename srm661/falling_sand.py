class FallingSand:
	def simulate(self, board):
		dot = '.'
		gr = 'o'
		b = [[x for x in board[i]] for i in range(len(board))]
		for i in range(len(b)-2, -1, -1):
			for j in range(len(b)-2, -1, -1):
				for k in range(len(board[j])):
					if b[j][k] == gr and b[j+1][k] == dot:
						b[j+1][k] = gr
						b[j][k] = dot
		
		for i in range(len(b)):
			b[i] = ''.join(b[i])
		
		return b