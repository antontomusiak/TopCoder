import math

class BearPaints:
	def maxArea(self, W, H, M):
		if W * H <= M: return W * H
		side1 = max(W, H)
		side2 = min(W, H)
		res = 0
		for a in range(1, int(math.sqrt(M))+1):
			b = M // a
			a1 = min(a, side2)
			b1 = min(b, side1)
			res = max(res, a1 * b1)
		
		return res