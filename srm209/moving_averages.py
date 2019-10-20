class MovingAverages:
	def calculate(self, times, n):
		av = []
		t = [(int(times[i][:2]) * 3600 + int(times[i][3:5]) * 60 + int(times[i][6:])) for i in range(len(times))]
		for i in range(len(t)-n+1):
			tmp = sum(t[i:i+n]) / n
			av.append(tmp)
		return av