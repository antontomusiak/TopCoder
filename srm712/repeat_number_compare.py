class RepeatNumberCompare:
	def compare(self, x1, k1, x2, k2):
		
		v1 = str(x1) * k1
		v2 = str(x2) * k2
		
		if len(v1) > len(v2): 
			return "Greater"
		if len(v1) < len(v2):
			return "Less"
		if len(v1) == len(v2):
			for i in range(len(v1)):
				if v1 > v2:
					return "Greater"
				if v1 < v2:
					return "Less"
			
			return "Equal"