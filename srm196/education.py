class Education:
	def minimize(self, desire, tests):
		res = 0
		grades = ['A', 'B', 'C', 'D']
		points = [90, 80, 70, 60]
		total_points = points[grades.index(desire)] * (len(tests) + 1)
		res = total_points - sum(tests)
		if res <= 0: return 0
		elif res > 100: return -1
		return res 