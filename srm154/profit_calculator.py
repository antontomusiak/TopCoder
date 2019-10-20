class ProfitCalculator:
	def percent(self, items):
		price, cost = 0, 0
		for s in items:
			price += float(s[:6])
			cost += float(s[7:])
		
		return int((price-cost)/price*100)