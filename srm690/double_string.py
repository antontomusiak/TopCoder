class DoubleString:
	def check(self, S):
		if len(S) % 2 == 1: return "not square"
		elif S[:len(S)/2] == S[len(S)/2:]: return "square"
		else: return "not square"