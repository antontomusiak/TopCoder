class DivisorDigits:
	def howMany(self, number):
		s = str(number)
		divs = 0
		for num in s:
			if int(num) == 0: continue
			if number % int(num) == 0: divs += 1
		
		return divs