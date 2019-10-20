import math


class FlightDataRecorder:
	def getDistance(self, heading, distance):
		x, y = 0, 0
		for i in range(len(heading)):
			dx = distance[i] * math.cos(math.pi/180*heading[i])
			dy = distance[i] * math.sin(math.pi/180*heading[i])
			x += dx
			y += dy
		
		return math.sqrt(x*x + y*y)