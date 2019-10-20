class DistinctGridEasy:
	def checkGrid(self, n, k, grid):
		for i in range(0, len(grid), n):
			j = i + n
			row = grid[i:j]
			if len(set(row)) != k: return "Bad"
					
		for i in range(n):
			col = [grid[l] for l in range(i, len(grid), n)]
			if len(set(col)) != k: return "Bad"
		
		return "Good"
