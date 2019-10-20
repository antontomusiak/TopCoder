class TaroJiroDividing:
	def getNumber(self, A, B):
		res = 0
		intsT = [A]
		intsJ = [B]
		while A % 2 == 0:
			A /= 2
			intsT.append(A)
		
		while B % 2 == 0:
			B /= 2
			intsJ.append(B)
		
		for num in intsT:
			if num in intsJ: res += 1
			
		return res