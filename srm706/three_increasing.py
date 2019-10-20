class ThreeIncreasing:
	def minEaten(self, a, b, c):
		if c > b > a: return 0
		if b == 1 and c <= 2: return -1
		min_eaten = 0
		if c <= b: 
			min_eaten = b - c + 1
			b -= min_eaten
		if b < 2: return -1				
		if b <= a:
			min_eaten = min_eaten + a - b + 1
			
		return min_eaten