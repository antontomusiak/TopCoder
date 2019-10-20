class GolfScore:
	def tally(self, parValues, scoreSheet):
		ts = {"triple bogey": 3, "double bogey": 2, "bogey": 1, "par": 0, 
			"birdie": -1, "eagle": -2, "albatross": -3}
		res = 0
		for i in range(len(parValues)):
			if scoreSheet[i] == "hole in one": res += 1
			else: res += (parValues[i] + ts[scoreSheet[i]])
		
		return res