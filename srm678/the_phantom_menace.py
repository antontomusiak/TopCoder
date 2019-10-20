import math


class ThePhantomMenace:
	def find(self, doors, droids):
		safe = 0
		for i in doors:
			tmp = 101
			for j in droids:
				tmp = min(tmp, abs(i - j))
			
			safe = max(safe, tmp)
		
		return safe