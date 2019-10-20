class LevelUp:
	def toNextLevel(self, expNeeded, received):
		for i in range(len(expNeeded)):
			if expNeeded[i] > received: return expNeeded[i] - received