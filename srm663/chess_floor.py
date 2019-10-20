class ChessFloor:
	def minimumChanges(self, floor):
		minChanges = len(floor)**2
		tiles = list(set(''.join(floor)))
		if len(tiles) == 1: tiles.append('A')
		for i in range(len(tiles) - 1):
			for j in range(i+1, len(tiles)):
				minFix1, minFix2 = 0, 0
				for k in range(0, len(floor), 2):
					for l in range(len(floor[k])):
						if l % 2 == 0 and floor[k][l] != tiles[i]: minFix1 += 1
						if l % 2 == 1 and floor[k][l] != tiles[j]: minFix1 += 1
						if l % 2 == 0 and floor[k][l] != tiles[j]: minFix2 += 1
						if l % 2 == 1 and floor[k][l] != tiles[i]: minFix2 += 1
					
				for k in range(1, len(floor), 2):
					for l in range(len(floor[k])):
						if l % 2 == 0 and floor[k][l] != tiles[j]: minFix1 += 1
						if l % 2 == 1 and floor[k][l] != tiles[i]: minFix1 += 1
						if l % 2 == 0 and floor[k][l] != tiles[i]: minFix2 += 1
						if l % 2 == 1 and floor[k][l] != tiles[j]: minFix2 += 1
				
				minChanges = min(minChanges, minFix1, minFix2)
		
		return minChanges