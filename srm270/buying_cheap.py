class BuyingCheap:
	def thirdBestPrice(self, prices):
		p_s = set(prices)
		p_s2 = sorted(list(p_s))
		if len(p_s2) < 3: return -1
		return p_s2[2]