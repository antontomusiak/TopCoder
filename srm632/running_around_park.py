class RunningAroundPark:
	def numberOfLap(self, N, d):
		res = 1
		for i in range(len(d)-1):
			if d[i] >= d[i+1]: res += 1
		
		return res