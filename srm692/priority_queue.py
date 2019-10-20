class PriorityQueue:
	def findAnnoyance(self, S, a):
		D = []
		for i in range(len(S)-1):
			tmp = a[i] * S[i+1:len(S)].count("b")
			D.append(tmp)
		
		return sum(D)