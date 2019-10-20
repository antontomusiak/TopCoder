class HillClimber:
	def longest(self, height):
		count = 0
		counts = []
		for i in range(len(height)-1):
			if height[i] < height[i+1]: count += 1 
			else:
				counts.append(count)
				count = 0
		
		if counts: return max(max(counts), count)
		else: return count