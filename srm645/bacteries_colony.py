class BacteriesColony:
	def performTheExperiment(self, colonies):
		col = list(colonies)
		while True:
			tmp = [0 for x in colonies]
			for i in range(1, len(colonies)-1):
				if col[i-1] > col[i] and col[i+1] > col[i]: 
					tmp[i] = col[i] + 1
					continue
				if col[i-1] < col[i] and col[i+1] < col[i]: 
					tmp[i] = col[i] - 1
					continue
				else: tmp[i] = col[i]
			
			tmp[0] = colonies[0]
			tmp[len(tmp)-1] = colonies[len(colonies)-1]
			if col == tmp: return tmp
			else: 
				col = list(tmp)	