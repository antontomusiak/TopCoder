class Quipu:
	def readKnots(self, knots):
		kd = []
		c = 1
		for i in range(1, len(knots)-1):
			if knots[i] == 'X' and knots[i+1] == 'X': c +=1
			if knots[i] == 'X' and knots[i+1] == '-':
				kd.append(str(c))
				c = 1
			if knots[i] == '-' and knots[i+1] == '-': kd.append(str(0))
		
		return int(''.join(kd))