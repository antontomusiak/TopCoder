class CutoffRounder:
	def round(self, num, cutoff):
		num = float(num)
		cutoff = float(cutoff)
		if num % 1 > cutoff: return int(num) + 1
		
		return int(num)