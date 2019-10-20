class Swimmers:
	def getSwimTimes(self, distances, speed, current):
		times = [0 for i in range(len(speed))]
		for i in range(len(times)):
			if distances[i] == 0: 
				times[i] = 0
				continue
			if speed[i] - current <= 0: 
				times[i] = -1
				continue
			else:
				times[i] = (float(distances[i]) / (speed[i] + current)) + (float(distances[i]) / (speed[i] - current))
		
		return times