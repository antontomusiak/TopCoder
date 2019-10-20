class Average:
	def belowAvg(self, math, verbal):
		res = 0
		average = (sum(math) + sum(verbal)) / float(len(math))
		for i in range(len(math)):
			if math[i] + verbal[i] < average: res += 1
		
		return res 