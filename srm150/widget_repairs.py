import math

class WidgetRepairs:
	def days(self, arrivals, numPerDay):
		arrivals = list(arrivals)
		rd = 0
		left = 0
		for i in range(len(arrivals)):
			if arrivals[i] + left > 0:
				rd += 1
				left += arrivals[i] - numPerDay
				if left < 0: left = 0
		
		left = float(left)
		rd += int(math.ceil(left/numPerDay))
		return rd