class Inchworm:
	def lunchtime(self, branch, rest, leaf):
		count = 0
		for i in range(0, branch+1, rest):
			if i % leaf == 0: count += 1
		
		return count