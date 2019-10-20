class ImageDithering:
	def count(self, dithered, screen):
		res = 0
		for i in range(len(screen)):
			for j in range(len(screen[i])):
				if screen[i][j] in dithered: res += 1
		return res