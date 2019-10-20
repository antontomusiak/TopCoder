class RGBColor:
	def getComplement(self, rgb):
		comp = [0, 0, 0]
		if all([((abs(rgb[i] - (255 - rgb[i]))) <= 32) for i in range(3)]):
			for i in range(3):
				if rgb[i] + 128 > 255:
					comp[i] = rgb[i] - 128
				else: comp[i] = rgb[i] + 128
		else: comp = [(255 - rgb[i]) for i in range(3)]
		
		return comp