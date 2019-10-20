import math

class SquareMaking:
	def getMinimalPrice(self, a, b, c, d):
		sticks = [a, b, c, d]
		spend = 1000000
		for i in range(min(sticks), max(sticks)+1):
			tmp = 0
			for j in sticks:
				tmp += abs(j - i)
			
			spend = min(tmp, spend)
				
			
		
		return spend