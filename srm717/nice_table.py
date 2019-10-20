class NiceTable:
	def isNice(self, t):
		n = len(t)
		m = len(t[0])
		for x in range(2**n):
			x_l = [int(i) for i in list(('0'*n+bin(x)[2:])[::-1][:n])]
			for y in range(2**m):
				y_l = [int(i) for i in list(('0'*m+bin(y)[2:])[::-1][:m])]
				nice = True
				for i in range(n):
					for j in range(m):
						if int(t[i][j]) != x_l[i] ^ y_l[j]:
							nice = False
							continue
					if not nice: break
				
				if nice: return "Nice"
		
		return "Not nice"