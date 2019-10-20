class Cdgame:
	def rescount(self, a, b):
		res = set()
		for i in range(len(a)):
			l1 = list(a)
			l2 = list(b)
			for j in range(len(b)):
				l1[i], l2[j] = l2[j], l1[i]
				res.add(sum(l1) * sum(l2))
		return len(res)