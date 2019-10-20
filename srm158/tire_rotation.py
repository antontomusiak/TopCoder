class TireRotation:
	def getCycle(self, initial, current):
		r = [[0, 1, 2, 3], [3, 2, 0, 1], [1, 0, 3, 2], [2, 3, 1, 0]]
		for c in r:
			if current == initial[c[0]] + initial[c[1]] + initial[c[2]] + initial[c[3]]: return r.index(c) + 1
		
		return -1