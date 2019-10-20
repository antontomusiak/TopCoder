class FilipTheFrog:
	def countReachableIslands(self, positions, L):
		islands = set()
		sp = positions[0]
		sp1 = positions[0]
		sp2 = positions[0]
		p_l = sorted(list(positions))
		for el in p_l[p_l.index(sp):]:
			if abs(el - sp1) <= L: 
				islands.add(el)
				sp1 = el
				
		for el in p_l[p_l.index(sp)::-1]:
			if abs(el - sp2) <= L: 
				islands.add(el)
				sp2 = el
		
		return len(islands)