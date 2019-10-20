class Multiples:
	def number(self, min, max, factor):
		res = 0
		for num in range(min, min + factor + 1):
			if abs(num) % factor == 0: 
				res = num
				break
		
		res = (max - res) / factor + 1
		
		return res