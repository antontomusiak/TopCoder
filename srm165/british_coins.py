class BritishCoins:
	def coins(self, pence):
		pound = pence / 20 / 12
		pence -= (pound * 20 * 12)
		shilling =  pence / 12
		pence -= shilling * 12
		coins = [pound, shilling, pence]
		return coins 