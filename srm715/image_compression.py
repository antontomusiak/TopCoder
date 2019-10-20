class ImageCompression:
	def isPossible(self, image, k):
		n = len(image) / k
		m = len(image[0]) / k
		
		for i in range(n):
			for j in range(m):
				s = set()
				for i1 in range(k):
					for j1 in range(k):
						s.add(image[i*k+i1][j*k+j1])
						if len(s) > 1: return "Impossible"
		
		return "Possible"