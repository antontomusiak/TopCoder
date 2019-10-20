class RelativeHeights:
	def countWays(self, h):
		profs = [[] for i in range(len(h))]
		profs_uniq = []
		for i in range(len(h)):
			tmp = [x for x in h if x != h[i]]
			tmp_rev = sorted(tmp, reverse = True)
			
			for j in range(len(tmp)):
				profs[i].append(tmp.index(tmp_rev[j]))
		
		for k in profs:
			if k not in profs_uniq: profs_uniq.append(k)
		
		return len(profs_uniq)
