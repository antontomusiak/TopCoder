class SymmetryDetection:
	def detect(self, board):
		flag_v = True
		flag_h = True
		for i in board:
			n = len(i) // 2
			for j in range(n):
				if i[j] != i[len(i)-1-j]:
					flag_v = False
					break
			if not flag_v: break
		
		for i in range(len(board)):
			n = len(board) // 2
			if board[i] != board[len(board)-1-i]:
				flag_h = False
				break
		
		if flag_v and flag_h: return "Both"
		elif flag_v: return "Vertically symmetric"
		elif flag_h: return "Horizontally symmetric"
		else: return "Neither"