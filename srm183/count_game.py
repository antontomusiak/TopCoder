class CountGame:
	def howMany(self, maxAdd, goal, next):
		res = -1
		for i in range(goal, next, -(maxAdd + 1)):
			if i - next <= maxAdd: res = i - next + 1
		
		return res