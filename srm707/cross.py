class Cross:
	def exist(self, board):
		for i in range(1, len(board)-1):
			for j in range(1, len(board[i])-1):
				if board[i][j] == '#' and board[i][j-1] == '#' and board[i-1][j] == '#' and board[i+1][j] == '#' and board[i][j+1] == '#': return "Exist"
		
		return "Does not exist"