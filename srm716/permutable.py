class Permutiple:
	def isPossible(self, x):
		n = 2
		xs = str(x)
		while len(str(x * n)) == len(xs):
			xs_s = sorted(xs)
			tmp = str(x * n)
			tmp_s = sorted(tmp)
			if xs_s == tmp_s: return "Possible"
			n += 1 
		
		return "Impossible" 
