class TransportCounting:
	def countBuses(self, speed, positions, velocities, time):
		res = 0
		d = speed * time
		for i in range(len(positions)):
			if (positions[i] == 0) or (positions[i] + velocities[i] * time) <= d:
				res += 1
		
		return res