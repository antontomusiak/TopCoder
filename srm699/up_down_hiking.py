class UpDownHiking:
	def maxHeight(self, N, A, B):
		for i in range(1, N):
			if N == 2: return min(A,B)
			if (i * A) == (B * (N - i)): return A * i
			if (i * A) > (B * (N - i)): return max((A * ( i - 1)), (B * (N - i))) 
		
		return A * (N - 1)