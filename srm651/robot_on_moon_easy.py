class RobotOnMoonEasy:
	def isSafeCommand(self, board, S):
		b_l = [[x for x in board[i]] for i in range(len(board))]
		r = []
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == 'S':
					r.append(i)
					r.append(j)
		
		for s in S:
			if s == 'U':
				if r[0] == 0: return 'Dead'
				if b_l[r[0]-1][r[1]] == '.':
					b_l[r[0]-1][r[1]], b_l[r[0]][r[1]] = 'S', '.'
					r[0] -= 1
			if s == 'D':
				if r[0] == len(b_l) - 1: return 'Dead'
				if b_l[r[0]+1][r[1]] == '.':
					b_l[r[0]+1][r[1]], b_l[r[0]][r[1]] = 'S', '.'
					r[0] += 1
			if s == 'L':
				if r[1] == 0: return 'Dead'
				if b_l[r[0]][r[1]-1] == '.':
					b_l[r[0]][r[1]-1], b_l[r[0]][r[1]] = 'S', '.'
					r[1] -= 1
			if s == 'R':
				if r[1] == len(b_l[0]) - 1: return 'Dead'
				if b_l[r[0]][r[1]+1] == '.':
					b_l[r[0]][r[1]+1], b_l[r[0]][r[1]] = 'S', '.'
					r[1] += 1	
		return 'Alive'