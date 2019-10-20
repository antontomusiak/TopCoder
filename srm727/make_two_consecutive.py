class MakeTwoConsecutive:
	def solve(self, S):
		if len(S) <= 2: return "Impossible"
		for i in range((len(S)-2)):
			if ((S[i] == S[i + 1]) or (S[i] == S[i + 2])): return "Possible"
		
		a = len(S) - 1
		b = len(S) - 2
		if S[a] == S[b]: return "Possible"  	
		
		return "Impossible"