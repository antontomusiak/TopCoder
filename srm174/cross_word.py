class CrossWord:
	def countWords(self, board, size):
		words = []
		for i in range(len(board)):
			tmp = 0
			for j in range(len(board[i])):
				if board[i][j] == '.': tmp += 1
				else:
					words.append(tmp)
					tmp = 0
			words.append(tmp)
		return words.count(size)