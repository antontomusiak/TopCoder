class BichromeBoard:
	def ableToDraw(self, board):
		b, w = 'B?', 'W?'
		minFix1, minFix2 = 0, 0
		for i in range(0, len(board), 2):
			for j in range(len(board[i])):
				if j % 2 == 0 and board[i][j] not in b: minFix1 += 1
				if j % 2 == 1 and board[i][j] not in w: minFix1 += 1
				if j % 2 == 0 and board[i][j] not in w: minFix2 += 1
				if j % 2 == 1 and board[i][j] not in b: minFix2 += 1
		for i in range(1, len(board), 2):
			for j in range(len(board[i])):
				if j % 2 == 0 and board[i][j] not in b: minFix2 += 1
				if j % 2 == 1 and board[i][j] not in w: minFix2 += 1
				if j % 2 == 0 and board[i][j] not in w: minFix1 += 1
				if j % 2 == 1 and board[i][j] not in b: minFix1 += 1
			
		if minFix1 > 0 and minFix2 > 0: return "Impossible"
		return 'Possible'