class LiveConcert:
	def maxHappiness(self, h, s):
		h_s = [(h[i], s[i]) for i in range(len(h))]
		h_s.sort(key=lambda x: x[0], reverse = True)
		met = []
		happiness = 0
		for i in range(len(h)):
			if h_s[i][1] not in met: 
				happiness += h_s[i][0]
				met.append(h_s[i][1])
		
		return happiness