class SuperUserDo:
	def install(self, A, B):
		count = 0
		list_A = list(A)
		list_B = list(B)
		if len(A) == 1: return (B[0] - A[0] + 1)
		if len(set(B)) == 1 and len(set(A)) == 1 and set(A) == set(B): return 1
		for i in range(len(A)):
			tmp = [x for x in B if x != B[i]]
			if A[i] > max(tmp):
				count +=  B[i] + 1 - A[i]
				list_A.remove(A[i])
				list_B.remove(B[i])
		
		count += max(list_B) - min(list_A) + 1
		return count