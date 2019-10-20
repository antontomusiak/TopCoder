class MountainRanges:
	def countPeaks(self, heights):
		peaks = 0
		if len(heights) == 1: return 1
		for i in range(len(heights)-1):
			if i == 0 and heights[i] > heights[i+1]:
				peaks += 1
				continue
			if heights[i] > heights[i+1] and heights[i] > heights[i-1]: peaks += 1
		
		if heights[len(heights)-1] > heights[len(heights)-2]: peaks += 1
		return peaks