class Istr:
	def count(self, s, k):
		s_l = sorted([s.count(i) for i in set(s)], reverse = True)
		while k > 0 and s_l[0] > 0:
			s_l[0] -= 1
			k -= 1
			s_l.sort(reverse = True)
		
		return sum([x*x for x in s_l])