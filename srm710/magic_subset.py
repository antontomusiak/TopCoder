class MagicSubset:
	def findBest(self, values):
		if len(values) == 1: return max(0, values[0] * (-1))
		sum_pos, sum_neg = 0, 0
		for i in range(1, len(values)):
			if values[i] < 0: sum_neg += values[i]
			if values[i] > 0: sum_pos += values[i]
		
		sum_neg = (sum_neg + values[0]) * -1
		
		return max(sum_pos, sum_neg)