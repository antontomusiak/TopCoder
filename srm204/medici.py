class Medici:
	def winner(self, fame, fortune, secrets): 
		scores = [0 for x in range(len(fame))]
		for i in range(len(scores)):
			scores[i] = min(fame[i], fortune[i], secrets[i])
		
		res = scores.index(max(scores))
		if scores.count(max(scores)) > 1: return -1
		return res