class NonDeterministicSubstring:
	def ways(self, A, B):
		if len(B) > len(A): return 0
		matches = []
		for i in range(len(A) - len(B)+1):
			sub = ''
			comp = A[i:i+len(B)]
			for j in range(len(comp)):
				if B[j] == '?': sub += comp[j]
				else: sub += B[j]
			if sub == comp: matches.append(sub)
			
		
		return len(set(matches))


        
        

                
                
