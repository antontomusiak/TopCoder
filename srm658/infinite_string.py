class InfiniteString:
	def equal(self, s, t):
		if s * len(t) == t * len(s): return 'Equal'
		return 'Not equal'