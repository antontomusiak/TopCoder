class FiveRooksDiv2:
	def findMax(self, board):
		res = 0
		for i in range(8):
			count1 = 0
			count2 = 0
			for j in range(8):
				if board[i][j] == 'R': count1 += 1
				if board[j][i] == 'R': count2 += 1
			
			res = max(res, count1)
			res = max(res, count2)
		
		return res