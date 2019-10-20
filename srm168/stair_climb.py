import math


class StairClimb:
	def stridesTaken(self, flights, stairsPerStride):
		strides = (len(flights) - 1) * 2
		for flight in flights:
			strides += math.ceil(float(flight)/stairsPerStride)
		
		return strides