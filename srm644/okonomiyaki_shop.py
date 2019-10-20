class OkonomiyakiShop:
	def count(self, osize, K):
		count = 0
		for i in range(len(osize)-1):
			for j in range(i+1, len(osize)):
				if abs(osize[i] - osize[j]) <= K: count += 1
		
		return count