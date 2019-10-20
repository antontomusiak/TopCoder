class TreeAndVertex:
	def get(self, tree):
		g = [0 for i in range(len(tree)+1)]
		for i in range(len(tree)):
			g[i+1] += 1
			g[tree[i]] += 1			
		
		return max(g)