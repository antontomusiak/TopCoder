class KitayutaMart2:
	def numBought(self, K, T):
		res = 0
		TN = 0
		while TN < T:
			TN += K * (2**res)
			res += 1
		return res	