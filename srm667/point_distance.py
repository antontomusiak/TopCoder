import math

class PointDistance:
	def findPoint(self, x1, y1, x2, y2):
		C = []
		for i in range(-100, 101):
			for j in range(-100, 101):
				if math.sqrt((x1 - i)**2 + (y1 - j)**2) > math.sqrt((x2 - i)**2 + (y2 - j)**2):
					C.append(i)
					C.append(j)
					return C