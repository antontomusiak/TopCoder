class CoinFlipsDiv2:
	def countCoins(self, state):
		interesting = 0
		met = False
		for i in range(len(state)-1):
			if state[i] != state[i+1]: 
				if met: interesting += 1
				else:
					interesting += 2
					met = True
			else: met = False
			
		return interesting