class Stairs:
	def designs(self, maxHeight, minWidth, totalHeight, totalWidth):
		designs = 0
		for i in range(maxHeight, 0, -1):
			if totalHeight % i == 0 and totalHeight != i:
				if (totalWidth % (totalHeight / i - 1) == 0) and (totalWidth / (totalHeight / i - 1)) >= minWidth:
					designs += 1
					
		return designs