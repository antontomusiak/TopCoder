class BettingMoney:
	def moneyMade(self, amounts, centsPerDollar, finalResult):
		win = 0
		for i in range(len(amounts)):
			if i == finalResult:
				win = amounts[i] * centsPerDollar[i] + amounts[i] * 100
				
		return sum(amounts) * 100 - win		