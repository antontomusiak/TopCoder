class StringMult:
	def times(self, sFactor, iFactor):
		if iFactor == 0: return ""
		if iFactor < 0: return sFactor[::-1] * abs(iFactor)		
		return sFactor * iFactor