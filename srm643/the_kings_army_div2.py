class TheKingsArmyDiv2:
	def getNumber(self, state):
		happy = 0
		for i in range(len(state)-1):
			if 'H' in state[i]: happy = 1
			if 'HH' in state[i]: return 0
			for j in range(len(state[i])):
				if state[i][j] == 'H' and state[i+1][j] == 'H': return 0
		if 'H' in state[len(state)-1]: happy = 1
		if 'HH' in state[len(state)-1]: return 0
		
		return 2 - happy