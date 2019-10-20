class SetPartialOrder:
	def compareSets(self, a, b):
		if len(a) < len(b) and all([a[i] in b for i in range(len(a))]): return 'LESS'
		if len(a) > len(b) and all([b[i] in a for i in range(len(b))]): return 'GREATER'
		if len(a) == len(b) and all([a[i] in b for i in range(len(a))]): return 'EQUAL'
		return 'INCOMPARABLE'