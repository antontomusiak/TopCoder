class IBEvaluator:
	def getSummary(self, predictedGrades, actualGrades):
		diff = [0 for x in range(7)]
		for i in range(len(predictedGrades)):
			tmp = abs(predictedGrades[i]- actualGrades[i])
			diff[tmp] += 1
		
		n = float(len(predictedGrades))
		for i in range(len(diff)):
			diff[i] = int(diff[i] / n * 100)
		
		return diff 