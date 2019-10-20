import math


class BearNSWE:
	def totalDistance(self, a, dir):
		x, y = 0, 0
		for i in range(len(a)):
			if dir[i] == "N": x += a[i]
			if dir[i] == "S": x -= a[i]
			if dir[i] == "W": y += a[i]
			if dir[i] == "E": y -= a[i]
		
		return sum(a) + math.sqrt(x*x +y*y)