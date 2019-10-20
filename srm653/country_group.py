class CountryGroup:
	def solve(self, a):
		res = 0
		i = 0
		if any([x > len(a) for x in a]): return -1
		while i < len(a):
			if all([x == a[i] for x in a[i:i+a[i]]]) and len(a[i:i+a[i]]) == a[i]:
				res += 1
				i += a[i]
			else: return -1
		
		return res