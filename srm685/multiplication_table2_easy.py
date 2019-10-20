from math import sqrt

class MultiplicationTable2Easy:
	def isGoodSet(self, table, t):
		n = int(sqrt(len(table)))
		for i in t:
			for j in t:
				if table[i * n + j] not in t: return 'Not Good'
		
		return 'Good'