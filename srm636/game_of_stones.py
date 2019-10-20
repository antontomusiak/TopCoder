class GameOfStones:
	def count(self, stones):
		s_l = list(stones)
		if sum(stones) % len(stones) != 0: return -1
		average = sum(stones) / len(stones)
		if len(set(stones)) == 1: return 0
		moves = 0
		for i in range(len(stones)):
			if abs(stones[i] - average) % 2 != 0: return -1
			if stones[i] < average: moves += (average - stones[i])/2
		
		return moves