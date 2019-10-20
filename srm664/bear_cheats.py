class BearCheats:
	def eyesight(self, A, B):
		count = 0
		a = str(A)
		b = str(B)
		for i in range(len(a)):
			if a[i] != b[i]: count +=1
			if count > 1: return 'glasses'
		
		return 'happy'