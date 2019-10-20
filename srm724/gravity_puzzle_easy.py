class GravityPuzzleEasy:
	def solve(self, board):
		counts = [0 for i in range(len(board[0]))]
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == '#': counts[j] += 1
				
		res = [[] for i in range(len(board))]
		for i in range(len(board)-1, -1, -1):			
			for j in range(len(board[i])):
				if counts[j] > 0:
					res[i].append('#')
					counts[j] -= 1
				else: res[i].append('.')
			res[i] = "".join(res[i])
		
		return res