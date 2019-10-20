class DevuAndGame:
	def canWin(self, nextLevel):
		been = []
		s = True
		i = 0
		while s:
			if i in been: return 'Lose'
			if nextLevel[i] == -1: return 'Win'
			else: 
				been.append(i)
				i = nextLevel[i]