class OnLineRank:
	def calcRanks(self, k, scores):
		z = [0 for x in range(k)]
		scores = z + list(scores)
		rank = []
		for i in range(k, len(scores)):
			tmp = 1
			for j in range(i-k, i):
				if scores[i] < scores[j]: tmp += 1
			rank.append(tmp)
		
		return sum(rank)