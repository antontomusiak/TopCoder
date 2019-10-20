class RelationClassifier:
	def isBijection(self, domain, range):
		d_l = list(domain)
		r_l = list(range)
		for el in d_l:
			if d_l.count(el) > 1: return 'Not'
		for el in r_l:
			if r_l.count(el) > 1: return 'Not'
		
		return 'Bijection'