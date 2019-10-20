class RectangularGrid:
	def countRectangles(self, width, height):
		count = 0
		for i in range(1, width+1):
			for j in range(1, height+1):
				if i != j: count += ((width - i + 1) * (height - j + 1))
		
		return count