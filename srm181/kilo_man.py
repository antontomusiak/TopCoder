class KiloMan:
	def hitsTaken(self, pattern, jumps):
		res = 0
		for i in range(len(pattern)):
			if (pattern[i] <= 2 and jumps[i] == 'S') or (pattern[i] > 2 and jumps[i] == 'J'): res += 1
		
		return res